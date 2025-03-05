import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

st.title("visualisation et prédiction des types de reponse")
left_column,middle,right_column = st.columns(3)
left_column.button('Visualisation')
middle.write('Dataset mathE')
#chargement des données
df=pd.read_csv("mathE-data.csv",sep=";", encoding='cp1252')
#suppression de la colonne Keywords
#df = df.drop('Student ID', axis=1)

# Titre de l'application
st.title("Visualisation des données MathE")

# Afficher le tableau de données
st.subheader("Tableau de données")
st.dataframe(df)

# Statistiques descriptives
st.subheader("Statistiques descriptives")
st.write(df.describe())

# Histogramme
st.subheader("Histogramme des pays")
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(df['Student Country'], bins=20)
st.pyplot(fig_hist)

# Graphique de dispersion
st.subheader("Graphique de dispersion Student Country vs Question Level")
fig_scatter, ax_scatter = plt.subplots()
ax_scatter.scatter(df['Student Country'], df['Question Level'])
ax_scatter.set_xlabel("Student Country")
ax_scatter.set_ylabel("Question Level")
st.pyplot(fig_scatter)

#prétaitement des données
#application du frequency encoding of student country
freq=df['Student Country'].value_counts()
df['Student Country']=df['Student Country'].map(freq/df.shape[0])
#application du frequency encoding of Topic
freq2=df['Topic'].value_counts()
df['Topic']=df['Topic'].map(freq2/df.shape[0])
#application du frequency encoding of Subtopic
freq2=df['Topic'].value_counts()
df['Topic']=df['Topic'].map(freq2/df.shape[0])
