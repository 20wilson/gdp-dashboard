import streamlit as st
import pandas as pd
import numpy as np

# Affichage de l'uploader dans l'application Streamlit
file = st.file_uploader("Importer vos données ici", type=["csv"])

# Vérification si un fichier a été téléchargé
if file is not None:
    # Traitement du fichier téléchargé (par exemple, afficher les 5 premières lignes d'un DataFrame Pandas)
    df = pd.read_csv(file)
    st.dataframe(df)

# Affichage du graphique à barres avec st.bar_chart
st.line_chart(df)
st.bar_chart(df)