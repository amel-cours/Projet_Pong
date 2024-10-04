
from tkinter import*
#création d'une fenêtre graphique
fen=Tk()
tk=Tk()
fen.title("pong")
fen.geometry('600x500+100+100')
Largeur=600
Hauteur=500
can= Canvas(fen,width=Largeur, height=Hauteur ,bg='white')
can.pack(padx=0,pady=0)

#Une fonction pour le deplacement vers la droite et la gauche:
def droite(event):
    can.move(raquette,10,0)
    tk.after(5,deplacement)

def gauche(event):
    can.move(raquette,-10,0)
    tk.after(5,deplacement)


    #On cree une raquette:
raquette = can.create_rectangle(200,380,300,390,fill='red')

#On associe la touche droite du clavier a la fonction droite et pareil avec la gauche():
can.bind_all('<Right>', droite)
can.bind_all('<Left>',gauche)

def deplacement():
    global dx, dy
    if can.coords(balle1)[3]>400:
        dy=-1*dy
    #On deplace la balle :
    can.move(balle1,dx,dy)
    #On repete cette fonction
    tk.after(20,deplacement)

#Coordonnees de la balle:
Pos_X=60
Pos_Y=10
dx=0
dy=5



#On cree une balle:
balle1 = can.create_oval(Pos_X,Pos_Y,Pos_X+20,Pos_Y+20,fill='silver')

deplacement()

fen.mainloop()