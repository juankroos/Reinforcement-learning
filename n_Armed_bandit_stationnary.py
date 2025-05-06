import numpy as np
import matplotlib.pyplot as plt
from random import random


# classe representant un bras avec une distribution de récompenses
class Bras:
    def __init__(self, m, e):
        self.moy = m
        self.ecart = e

    def generer_recompense(self):
        return np.random.normal(loc=self.moy, scale=self.ecart)

    def update_moyenne(self, nouvelle_moy):
        self.moy = nouvelle_moy


# classe de base pour la strategie Factory

class Strategy:
    def __init__(self, T, strategy_type):
        self.T = T
        self.strategy_type = strategy_type
        self.esp = 0.1 if strategy_type == "greedy" else 0.0


# classe pour l'algorithme d'apprentissage
class AlgorithmLearn(Strategy):
    def __init__(self, T, strategy_type, bras_list, alpha=0.1, non_stationnaire=False):
        super().__init__(T, strategy_type)
        self.bras_list = bras_list
        self.alpha = alpha
        self.non_stationnaire = non_stationnaire
        self.count = [0, 0]
        self.aver_estim = [0.0, 0.0]
        self.rt = []
        self.choice = []
        self.rec_c = 0.0
        self.regret_c = 0.0
        self.rec_c_list = []
        self.regret_c_list = []  # regret cumule a chaque tour

    def Tirage(self):
        """execute la simulation pour T tours."""
        # forcer un tirage initial pour chaque bras pour eviter des estimations indéfinies
        for t in range(1, 3):
            # bras 1 au tour 1, bras 2 au tour 2
            c = t  
            self._effectuer_tirage(t, c)

        # boucle principale pour les tours restants
        for t in range(3, self.T + 1):
            # exploration (epsilon) ou exploitation (1-epsilon)
            p = random()
            if p < self.esp:
                # exploration : choisir un bras au hasard
                c = 1 if random() < 0.5 else 2
            else:
                # exploitation : choisir le bras avec la meilleure estimation
                c = 2 if self.aver_estim[1] > self.aver_estim[0] else 1

            self._effectuer_tirage(t, c)

    def _effectuer_tirage(self, t, c):
        """effectue un tirage pour le bras c au tour t."""
        # generer la récompense
        r_t = self.bras_list[c - 1].generer_recompense()


        # mise a jour pour le cas non stationnaire (à t=501)
        if self.non_stationnaire and t == 501:
            self.bras_list[0].update_moyenne(5.5)  # μ_1 = 5.5
            self.bras_list[1].update_moyenne(3.0)  # μ_2 = 3.0

        # mettre a jour les métriques
        self.choice.append(c)
        self.rt.append(r_t)
        self.count[c - 1] += 1
        # mise a jour de l'estimation de la moyenne
        if self.non_stationnaire:
            # moyenne ponderee
            self.aver_estim[c - 1] = (1 - self.alpha) * self.aver_estim[c - 1] + self.alpha * r_t
        else:
            # moyenne classique
            if self.count[c - 1] == 1:
                self.aver_estim[c - 1] = r_t
            else:
                self.aver_estim[c - 1] += (r_t - self.aver_estim[c - 1]) / self.count[c - 1]

        # mettre a jour la recompense cumulee
        self.rec_c += r_t
        self.rec_c_list.append(self.rec_c)

        # mettre a jour le regret cumule
        # meilleure moyenne
        max_mu = max([bras.moy for bras in self.bras_list])  
        regret_t = max_mu - r_t
        self.regret_c += regret_t
        self.regret_c_list.append(self.regret_c)



if __name__ == "__main__":
    # Creer les bras
    bras_1 = Bras(m=4.0, e=1.0)
    bras_2 = Bras(m=6.0, e=1.0)
    bras_3 = Bras(m=2.0, e=1.0)
    bras_4 = Bras(m=1.0, e=1.0)
    bras_5 = Bras(m=3.0, e=1.0)
    bras_6 = Bras(m=4.0, e=1.0)
    bras_list = [bras_1, bras_2, bras_3, bras_4, bras_5, bras_6]

    # tester le cas stationnaire
    algo_stationnaire = AlgorithmLearn(
        T=1000,
        strategy_type="greedy",
        bras_list=bras_list,
        alpha=0.1,
        non_stationnaire=False
    )
    algo_stationnaire.Tirage()

    '''
    # tester le cas non stationnaire
    algo_non_stationnaire = AlgorithmLearn(
        T=1000,
        strategy_type="greedy",
        bras_list=[Bras(m=4.0, e=1.0), Bras(m=6.0, e=1.0), Bras(m=2.0, e=1.0), Bras(m=1.0, e=1.0), Bras(m=3.0, e=1.0), Bras(m=4.0, e=1.0)],
        alpha=0.1,
        non_stationnaire=True
    )
    algo_non_stationnaire.Tirage()
    '''
    # afficher les resultats
    print("___cas stationnaire___")
    print(f"Récompense cumulée: {algo_stationnaire.rec_c:.2f}")
    print(f"Regret cumulé: {algo_stationnaire.regret_c:.2f}")
    print(f"Compteurs: {algo_stationnaire.count}")
    print(f"Estimations: {algo_stationnaire.aver_estim}")

    '''
    print("\n__cas non stationnaire__")
    print(f"recompense cumulee: {algo_non_stationnaire.rec_c:.2f}")
    print(f"regret cumule: {algo_non_stationnaire.regret_c:.2f}")
    print(f"compteurs: {algo_non_stationnaire.count}")
    print(f"estimations: {algo_non_stationnaire.aver_estim}")
    '''


    plt.figure(figsize=(12, 8))

    # recompense cumulee
    plt.subplot(2, 1, 1)
    plt.plot(range(1, 1001), algo_stationnaire.rec_c_list, label="Stationnaire")
    #plt.plot(range(1, 1001), algo_non_stationnaire.rec_c_list, label="Non Stationnaire")
    plt.xlabel("tour (t)")
    plt.ylabel("recompense Cumulee")
    plt.title("evolution de la Récompense Cumulee")
    plt.legend()
    plt.grid(True)

    # regret cumulee
    plt.subplot(2, 1, 2)
    plt.plot(range(1, 1001), algo_stationnaire.regret_c_list, label="stationnaire")
    #plt.plot(range(1, 1001), algo_non_stationnaire.regret_c_list, label="non Stationnaire")
    plt.xlabel("tour (t)")
    plt.ylabel("regret Cumule")
    plt.title("volution du Regret Cumule")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("bandit_results.png")
    plt.show()