import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 📌 1. DONNÉES
# ==============================

data = {
    "Produit": ["Tel", "PC", "Tel", "TV", "PC", "Tel"],
    "Prix": [50000, 300000, 50000, 200000, 300000, 50000],
    "Ventes": [10, 5, 8, 2, 3, 12],
    "Ville": ["Lome", "Kara", "Lome", "Sokode", "Kara", "Lome"]
}

df = pd.DataFrame(data)

print("📊 DONNÉES INITIALES")
print(df)


# ==============================
# 🧹 2. NETTOYAGE DES DONNÉES
# ==============================

# Vérifier les infos du dataset
print("\n🔍 INFO DATASET")
print(df.info())

# Vérifier les valeurs manquantes
print("\n🔍 VALEURS MANQUANTES")
print(df.isnull().sum())

# Supprimer les doublons (sécurité data)
df = df.drop_duplicates()

print("\n🧹 APRÈS NETTOYAGE")
print(df)


# ==============================
# 📊 3. ANALYSE BUSINESS
# ==============================

# 🏆 Produit le plus vendu (IMPORTANT)
# On additionne toutes les ventes par produit puis on prend le max
produits_ventes = df.groupby("Produit")["Ventes"].sum()

print("\n🏆 VENTES PAR PRODUIT")
print(produits_ventes)

# 👉 Meilleur produit (solution propre avec idxmax)
meilleur_produit = produits_ventes.idxmax()
print("\n🥇 MEILLEUR PRODUIT :", meilleur_produit)


# 🌍 Ville la plus active
ventes_par_ville = df.groupby("Ville")["Ventes"].sum()

print("\n🌍 VENTES PAR VILLE")
print(ventes_par_ville)

meilleure_ville = ventes_par_ville.idxmax()
print("\n🏙️ VILLE LA PLUS ACTIVE :", meilleure_ville)


# ==============================
# 💰 4. CALCUL DU REVENU
# ==============================

# Le revenu = Prix × Ventes
df["Revenu"] = df["Prix"] * df["Ventes"]

print("\n💰 DATA AVEC REVENU")
print(df)

# Revenu total de l'entreprise
revenu_total = df["Revenu"].sum()
print("\n💰 REVENU TOTAL :", revenu_total)


# ==============================
# 📈 5. VISUALISATION (DATA ANALYST)
# ==============================

# 📊 Ventes par produit (bar chart)
df.groupby("Produit")["Ventes"].sum().plot(kind="bar")
plt.title("Ventes par produit")
plt.xlabel("Produit")
plt.ylabel("Ventes")
plt.show()


# 📊 Revenus par produit
df.groupby("Produit")["Revenu"].sum().plot(kind="bar")
plt.title("Revenus par produit")
plt.xlabel("Produit")
plt.ylabel("Revenu")
plt.show()


# ==============================
# 🧠 6. INSIGHTS (INTERPRÉTATION)
# ==============================

print("\n🧠 INSIGHTS BUSINESS")

print("- Produit le plus vendu :", meilleur_produit)
print("- Ville la plus active :", meilleure_ville)
print("- Revenu total :", revenu_total)

print("\n📌 CONCLUSION :")
print("Le produit Tel est le plus performant en volume de ventes.")