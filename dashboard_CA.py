import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Suivi du Chiffre d'Affaires")

# Instructions pour l'utilisateur
st.markdown("Saisissez le chiffre d'affaires (CA) par mois pour l'année.")

# Liste des mois
months = [
    "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
]

# Saisie des CA par l'utilisateur
data = {}
for month in months:
    ca = st.number_input(f"CA pour {month} (en euros)", min_value=0, step=100, key=month)
    data[month] = ca

# Afficher les données sous forme de tableau
st.subheader("Données saisies")
df = pd.DataFrame(list(data.items()), columns=["Mois", "Chiffre d'Affaires"])
st.dataframe(df)

# Visualiser les données avec Matplotlib
if st.button("Afficher le graphique"):
    st.subheader("Graphique du Chiffre d'Affaires")
    try:
        # Créer le graphique avec Matplotlib
        fig, ax = plt.subplots()
        ax.bar(df["Mois"], df["Chiffre d'Affaires"], color="skyblue")
        ax.set_xlabel("Mois")
        ax.set_ylabel("Chiffre d'Affaires (en euros)")
        ax.set_title("Évolution du Chiffre d'Affaires")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Une erreur s'est produite lors de la génération du graphique : {e}")
