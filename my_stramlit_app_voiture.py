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

st.markdown("Description des variables :  \n  \n  - ___mpg___ (miles per gallon) : la consommation d'essence d'une voiture.  \n Attention, en France, nous comptons la consommation en nombre de litres pour 100 km. Plus une voiture consomme et plus elle a une valeur élevée de litres pour faire 100 km. Aux USA, ils comptent la consommation en miles (environ 1.6 km) par gallon (environ 4.55 litres). Plus une voiture consomme et moins elle a une valeur élevée de mpg.  \n - ___cylinders___ : le nombre de cylindres du moteur.  \n - ___cubicinches___ (cylindrée): le volume interne du moteur à combustion (souvent en cm3).  \n - ___hp___ (horsepower) : la puissance du moteur en chevaux.  \n - ___weightlbs___ : le poids de la voiture.  \n - ___time-to-60___ (accélération) : la durée en seconde pour passer de l'arrêt (0 km/h) à 60 mph (environ 97 km/h).  \n - ___year___ : l'année de production du modèle.  \n - ___continent___ : origine des constructeurs.")



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
  
st.markdown("La voiture la plus puissante a une puissance de 230.  \n Une grande partie de voitures a une puissance comprise entre 60 et 110." )
   
st.title('Graphique de corrélations filtré par région')

st.subheader("Carte de chaleur par continent:")


plt.figure(figsize=(10, 6))
hm_cars = sns.heatmap(df_filtre.corr(numeric_only=True),annot=True, center=0, cmap=sns.color_palette("vlag", as_cmap=True) )
st.pyplot(hm_cars.figure)


st.markdown("Les variables corrélées positivement sont : cylindrée/horsepower, cylindrée/poids.  \n Les variables corrélées négativement sont : mpg/puissance, mpg/poids.  \n Les variables qui ne semblent pas ou très peu corrélées sont : poids/année du modèle, acceleration/année du modèle.")






