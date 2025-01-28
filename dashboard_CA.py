import streamlit as st
import pandas as pd

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
    ca = st.number_input(f"CA pour {month} (€)", min_value=0, step=100, key=month)
    data[month] = ca

# Afficher les données sous forme de tableau
st.subheader("Données saisies")
df = pd.DataFrame(list(data.items()), columns=["Mois", "Chiffre d'Affaires (€)"])
st.dataframe(df)

# Visualiser les données avec un graphique
if st.button("Afficher le graphique"):
    st.subheader("Graphique du Chiffre d'Affaires")
    st.bar_chart(df.set_index("Mois"))
