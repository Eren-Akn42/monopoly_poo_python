from Plateau import Plateau
from Joueur import Joueur

class Partie : 

    def __init__(self, nb_joueur, joueurs):
        """
            Entrée : nb_joueur -> Entier
                     joueurs -> tableau d'objet de classe Joueur

            Constructeur de la classe Partie
        """
        self.p = Plateau()
        self.nb_joueur = nb_joueur
        self.joueurs = joueurs
        self.joueur_actif = joueurs[0]

    def choix_action(self):
        """
            Proposer 3 choix au joueur actif
                - lancer le dé
                - Consulter solde
                - Voir position
        """
        print("Quelle action souhaitez vous faire? \n Lancer le dé(1) \n Consulter votre solde(2) \n Voir votre position (3)\n")
        reponse = int(input("Saisissez votre choix : "))
        de = 0
        while reponse != 1:
            if reponse == 1 :
                de = self.joueur_actif.lancer_de()
                self.joueur_actif.deplacement(de)
            elif reponse == 2 :
                print("Votre solde est de  :", self.joueur_actif.argent)
            else :
                print("Vous êtes sur la case ", self.p.cases[self.joueur_actif.position].nom)

    def deplacement(self):

        return
    def tour(self):

        return
    def joueur_faillite(self):

        return