import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns 



st.title('Hello Wilders, bienvenue sur cette web app !')
st.title('Analysons le dataset des voitures !')

st.subheader("Importons d'abord le dataset:")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

st.title('Graphique interactif de distribution')

df_cars['continent'] = df_cars['continent'].apply(lambda x : x.replace('.', ''))
option = st.selectbox(label= 'veuillez séléctionner un continent.', options= df_cars['continent'].unique())

st.subheader("Graphique d'histogramme par continent:")

df_filtre = df_cars[df_cars["continent"]== option]


plt.figure(figsize=(10, 6))
viz_correlation = sns.histplot(data=df_cars, 
                                x=df_filtre["hp"],
                                hue=df_filtre["continent"])
st.pyplot(viz_correlation.figure)

   
st.title('Graphique de corrélations filtré par région')

st.subheader("Carte de chaleur par continent:")


plt.figure(figsize=(10, 6))
hm_cars = sns.heatmap(df_filtre.corr(numeric_only=True),annot=True, center=0, cmap=sns.color_palette("vlag", as_cmap=True) )
st.pyplot(hm_cars.figure)




