from bt_sql import update_score
import tkinter as tk
from tkinter.constants import DISABLED, NORMAL
import bt_utilitaire as u
import time
from threading import Thread

class AsyncTimer(Thread):
    ''' Classe Héritant de Thread
    
        Utilisée pour lancer un timer (countdown)
    '''
    def __init__(self, label):
        """ Constructeur
        """
        super().__init__()

        self.timer = 30
        self.label = label

    def run(self):
        ''' Calcul du temps restant et affichage réactualisé.
        '''
        self.timer = 30
        while self.timer > 0 :
            self.label.config(text=str(self.timer))
            time.sleep(1)
            self.timer = self.timer - 1


    def setTimer(self, n):
        ''' Modification de valeur du timer.
            Entrée : n -> Entier
        '''
        self.timer=n


class App(tk.Tk):
    ''' Classe de l'application graphique
    '''
    def __init__(self):
        ''' Constructeur

            Initialisation des variables:
                - Compteur et t -> Gestion des threads
                - Création des différents widgets(labels, boutons, etc)
        '''
        tk.Tk.__init__(self)
        self.compteur = 0
        self.t = []

        self.main_app = tk.Canvas(self, width = 800, height = 600,  relief = 'raised')
        self.main_app.pack()

        self.lbl_title = tk.Label(self, text='Blind Test')
        self.lbl_title.config(font=('helvetica', 14))
        self.main_app.create_window(400, 50, window=self.lbl_title)

        self.lbl_timer = tk.Label(self, text="30")
        self.lbl_timer.config(font=('helvetica', 70))
        self.main_app.create_window(400, 170, window=self.lbl_timer)

        self.lbl_todo = tk.Label(self, text='Saisissez l\'interprète :')
        self.lbl_todo.config(font=('helvetica', 10))
        self.main_app.create_window(200, 300, window=self.lbl_todo)

        self.in_author_name = tk.Text(self, width=30, height=2, font=("Bold",14)) 
        self.main_app.create_window(200, 340, window=self.in_author_name)

        self.lbl_todo2 = tk.Label(self, text='Saisissez le titre:')
        self.lbl_todo2.config(font=('helvetica', 10))
        self.main_app.create_window(600, 300, window=self.lbl_todo2)

        self.in_song_name = tk.Text(self, width=30, height=2, font=("Bold",14)) 
        self.main_app.create_window(600, 340, window=self.in_song_name)

        self.lbl_score = tk.Label(self, text='Score : 0', bg='brown', fg='white',  font=('helvetica', 25, 'bold'))
        self.main_app.create_window(700, 50, window=self.lbl_score)

        self.button_new_game = tk.Button(text='Nouvelle Partie', command=self.new_game, bg='black', fg='white', font=('helvetica', 9, 'bold'))
        self.main_app.create_window(80, 50, window=self.button_new_game)

        self.button_validate = tk.Button(text='Valider', command=self.validate, bg='brown', fg='white', font=('helvetica', 25, 'bold'))
        self.main_app.create_window(400, 400, window=self.button_validate)

        self.button_next = tk.Button(text='Chanson Suivante', command=self.nextSongButton, bg='darkblue', fg='white', font=('helvetica', 25, 'bold'))
        self.main_app.create_window(400, 460, window=self.button_next)

        self.button_quit = tk.Button(text="QUITTER", bg='black', fg="white", font=('helvetica', 9, 'bold'), command=self.destroy)
        self.main_app.create_window(760, 580, window = self.button_quit)      
       

        #TODO : Créer différents boutons pour les catégories que l'on souhaite pouvoir jouer:
        # ...
        # Exemples :
        #   - Années 2000
        #   - Variété française
        #   - Rap
        #   - ...
        # ...
        # Puis les associer à la fonction new_game avec les paramètres nécessaires

    def new_game(self, arg = 0, ch = ""):
        ''' Initialisation d'une nouvelle partie :
                - Initialisation du score
                - Initialisation des booléens de contrôle
                - Initiation d'une liste de threads
                - Nettoyage des données de parties précédentes
        '''
        global game
        game=u.Game(arg, ch)
        self.update_score(0)
        self.upd_score = False
        self.changer = True
        self.clear_thread()
        self.t.clear()
        self.compteur = 0
        self.handle_countdown()

    def validate(self):
        ''' Fonction de mise à jour du score.

            Appels : 
                - game.try_test()  -> Calcul
                - update_score() -> Affichage
        '''
        if not self.upd_score:
            score = game.try_test(self.in_author_name.get("1.0",'end-1c'), self.in_song_name.get("1.0", 'end-1c'))
            self.update_score(score)
            #Booléen de contrôle
            self.upd_score = True

    def update_score(self, s):
        ''' Mise à jour visuelle du score
        '''
        self.lbl_score["text"] = "Score : "+str(s)+""



    def nextSongButton(self):
        ''' Changement de musique au clic d'un utilisateur

            Appel : nextSong() -> Fonction de changement de musique générale.
        '''
        # Désactivation du bouton, en attendant la mise à jour du thread précédent
        self.button_next.config(state = DISABLED)
        self.changer = True
        self.nextSong()

    def nextSong(self):
        ''' Changement de musique

            Nettoyage de la liste de musique, mise à jour timer

            Appel : handle_coutdown() -> Gestion du timer
        '''
        game.next()
        self.upd_score = False
        self.in_author_name.delete('1.0', 'end')
        self.in_song_name.delete('1.0', 'end')
        self.lbl_timer.config(text="30")
        self.handle_countdown()

    

    def handle_countdown(self):
        ''' Gestion des threads de decompte.

            Mise à jour des threads précédents.

            Initialisation d'un nouveau thread.

            Incrémentation compteur.

            Appel : monitor() -> Gestion de fin de thread
        '''
        for item in range(self.compteur):
            self.t[item].setTimer(0)

        self.t.append(AsyncTimer(self.lbl_timer))
        self.t[self.compteur].setTimer(30)
        self.t[self.compteur].daemon = True
        self.t[self.compteur].start()

        self.compteur+=1
        self.monitor(self.t[self.compteur-1])  

    def clear_thread(self):
        ''' Nettoyage de thread en début de partie
        '''
        for item in range(self.compteur):
            self.t[item].setTimer(0)

    def monitor(self, thread):
        ''' Gestion de threads:
                - Fin du compteur.
                - Changement de musique manuel.
        '''
        # Cas d'une demande utilisateur
        if not thread.is_alive():
            if self.changer == False:
               self.nextSong()
            else:
                self.changer = False
                self.button_next.config(state=NORMAL)
        # Vérifie l'état du thread (100ms loop)
        else:
            self.after(100, lambda: self.monitor(thread))
        


if __name__ == "__main__":
    app = App()
    app.title("Blind Test")
    app.mainloop()