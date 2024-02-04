class ClasseMere:
    def __init__(self, parametre):
        self.parametre = parametre

class ClasseEnfant(ClasseMere):
    def __init__(self, parametre, autre_parametre):
        super().__init__(parametre)
        self.autre_parametre = autre_parametre
