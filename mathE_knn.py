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

df=pd.read_csv("mathE-data.csv",sep=";", encoding='cp1252')
#suppression de la colonne Keywords
#df = df.drop('Keywords', axis=1)
df = df.drop('Student ID', axis=1)
df = df.drop('Question ID', axis=1)
