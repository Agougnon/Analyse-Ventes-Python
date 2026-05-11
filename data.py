# Creation de dataframe
import pandas as pd
data={
    "Nom":["Ayo","Kossi","Ama","Kodjo","Ruth"],
    "Age":[18,20,19,22,21],
    "Notes":[15,12,18,9,17]
}
df=pd.DataFrame(data)
print("Le dataframe est:",df)

# Exercice:2 Exploration
# Afficher les 3premieres lignes
print("Les 3 premieres lignes du tableau:",df.iloc[0:3])
#Afficher les 2 premieres lignes
print("Les 2 premieres lignes du tableau :",df.iloc[0:2])
#Afficher les infos generales du dataset
print("Les infos generales du dataset sont:",df.info())
#La Taille du dataset
print("La taille du dataset est :",df.shape)

#Exercice:3
#Afficher uniquement noms
print("Affichage uniquement noms:",df["Nom"])
#Afficher uniquement Noms et Notes
print("Affichage uniquement Noms et Notes:",df[["Nom","Notes"]])
#Afficher la derniere ligne
print("La derniere ligne:",df.iloc[-1])

#Exercice:4
#Afficher les etudiants avec notes >=15
print("Les etudiants avec notes>=15:",df[df["Notes"]>=15])
#Afficher les etudiants avec age>20
print("Les etudiants avec Age>20:",df[df["Age"]>20])
#Afficher les etudiants avec notes entre 12 et 18
print("Les etudiants avec notes entre 12 et 18:",df[df(["Notes"]>=12)&df(["Notes"]<=18)])

