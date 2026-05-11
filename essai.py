import pandas as pd

Etudiants_data = {
    "Nom": ["Gedeon", "Joseph", "Emmanuel", "Augustin", "Ruth"],
    "Age": [21, 21, 22, 20, 19],
    "Notes": [18, 16, 17, 14, 19]
}

df = pd.DataFrame(Etudiants_data)

print("Voici le Tableau :")
print(df)

# Affiche étudiants avec note >= 15
Etudiants_Sup_quinze = df[df["Notes"] >= 15]
print("\nÉtudiants avec note >= 15 :")
print(Etudiants_Sup_quinze)

# Affiche les étudiants de moins de 20 ans
Etudiants_Moins20ans = df[df["Age"] < 20]
print("\nÉtudiants de moins de 20 ans :")
print(Etudiants_Moins20ans)

# Affiche seulement les noms et les notes
Noms_Notes = df[["Nom", "Notes"]]
print("\nNoms et Notes :")
print(Noms_Notes)

#Affiche notes superieur a 15 avec .loc
print(df.loc[df["Notes"] >= 15])

#Affiche seulement Noms et notes avec .loc
print(df.loc[df["Notes"]>=15,["Nom","Notes"]])

#Afiche des trois premieres ligne avec .iloc[]

print(df.iloc[0:3])
#Affiche uniquement la premiere colonne

print(df.iloc[:,0])
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)