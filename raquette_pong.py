from tkinter import*

#Une fonction pour le deplacement vers la droite :
def droite(event):
    can.move(raquette,10,0)
def gauche(event):
    can.move(raquette,-10,-0.5)

fen=Tk()
tk=Tk()
fen.title("pong")
fen.geometry('600x500+100+100')
Largeur=600
Hauteur=500
can= Canvas(fen,width=Largeur, height=Hauteur ,bg='white')
can.pack(padx=0,pady=0)


#Création  d'un bouton "Quitter":
Bouton_Quitter=Button(tk, text ='Quitter', command = tk.destroy)
#On ajoute l'affichage du bouton dans la fenêtre tk:
Bouton_Quitter.pack()

#On cree une raquette:
raquette = can.create_rectangle(200,380,300,390,fill='red')

#On associe la touche droite du clavier a la fonction droite():
can.bind_all('<Right>', droite)
can.bind_all('<Left>',gauche)


fen.mainloop()