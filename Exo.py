import pandas as pd

# ==============================
# 📌 1. DONNÉES BRUTES
# ==============================

data = {
    "Nom": ["Ayo", "Kossi", "Ama", "Ama", "Ruth", "Kodjo", "Emmanuel"],
    "Age": [24, None, 22, 22, 25, 30, None],
    "Salaire": [150000, 200000, None, 120000, 160000, 180000, 250000],
    "Departement": ["IT", "RH", "IT", "IT", "Marketing", "Finance", "IT"]
}

df = pd.DataFrame(data)

print("📊 DONNÉES INITIALES")
print(df)


# ==============================
# 🧹 2. NETTOYAGE DES DONNÉES
# ==============================

# 🔍 Vérifier les valeurs manquantes
print("\n🔍 Valeurs manquantes par colonne :")
print(df.isnull().sum())

# 🔄 Remplacer les valeurs manquantes dans Age par la moyenne
age_moyenne = df["Age"].mean()
df["Age"] = df["Age"].fillna(age_moyenne)

# 🔄 Remplacer les valeurs manquantes dans Salaire par la moyenne
salaire_moyenne = df["Salaire"].mean()
df["Salaire"] = df["Salaire"].fillna(salaire_moyenne)

# 🔁 Supprimer les doublons
df = df.drop_duplicates()

print("\n🧹 DONNÉES APRÈS NETTOYAGE")
print(df)


# ==============================
# 📊 3. STATISTIQUES GLOBALES
# ==============================

print("\n📊 STATISTIQUES")

# Moyenne des salaires
print("Salaire moyen :", df["Salaire"].mean())

# Salaire maximum
print("Salaire maximum :", df["Salaire"].max())

# Salaire minimum
print("Salaire minimum :", df["Salaire"].min())

# Total des salaires
print("Total des salaires :", df["Salaire"].sum())


# ==============================
# 🏢 4. ANALYSE BUSINESS
# ==============================

print("\n🏢 ANALYSE PAR DÉPARTEMENT")

# Salaire moyen par département
print(df.groupby("Departement")["Salaire"].mean())

# Nombre d'employés par département
print("\n👥 Nombre d'employés :")
print(df["Departement"].value_counts())

# Classement des départements
print("\n🏆 Classement des départements (salaire moyen) :")
print(df.groupby("Departement")["Salaire"].mean().sort_values(ascending=False))


# ==============================
# 🔄 5. TRANSFORMATION DES DONNÉES
# ==============================

# Création d'une catégorie de salaire
df["Categorie_Salaire"] = df["Salaire"].apply(
    lambda x: "Eleve" if x > 170000 else "Moyen"
)

print("\n📊 DONNÉES FINALES AVEC CATÉGORIE")
print(df)