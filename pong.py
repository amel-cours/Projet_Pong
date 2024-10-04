from tkinter import*

def deplacement():
    global dx, dy
    #On deplace la balle :
    can.move(balle1,dx,dy)
    #On repete cette fonction
    tk.after(20,deplacement)

#Deplacement de la balle au départ:
dx=5
dy=18

#création d'une fenêtre graphique et d'un canevas

fen=Tk()
tk=Tk()
fen.title("pong")
fen.geometry('600x500+100+100')
Largeur=600
Hauteur=500
can= Canvas(fen,width=Largeur, height=Hauteur ,bg='white')
can.pack(padx=0,pady=0)

#Creation  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

#On cree une balle:
balle1 = can.create_oval(10,10,30,30,fill='pink')

deplacement()

#On lance la boucle principale:
fen.mainloop()






















































