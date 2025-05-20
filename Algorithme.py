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


#add feature like the agent can check the reward in advance before step in the cell
