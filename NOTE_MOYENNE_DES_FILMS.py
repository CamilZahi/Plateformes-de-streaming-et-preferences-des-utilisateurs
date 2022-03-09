# On importe les librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# On créé un dataframe avec les notes des films données par les utilisateurs des plateformes
data_movies_ratings = pd.read_csv("movies_ratings_IMDb.csv",sep=',')

# On garde seulement les colonnes "title" et "avg_vote"
data_movies_ratings = data_movies_ratings.drop(['original_title','year','date_published','duration','language','director','writer','production_company','actors','description','total_votes','median_vote','country','genre'], axis=1)

# On regarde le nombre de lignes et de colonnes de ce dataframe
data_movies_ratings.shape

# On y fait une description rapide pour obtenir quelques stats
data_movies_ratings.describe()

# On créé un dataframe avec les titres de Amazon Prime Video où on ne garde que certaines colonnes et on ajoute une nouvelle colonne
data_Amazon = pd.read_csv("amazon_prime_titles.csv", 
                          sep=',')
data_Amazon = data_Amazon.drop(['show_id','director','cast','date_added','release_year','rating','duration','description','country'], axis=1)
data_Amazon = data_Amazon.assign(plateforme="Amazon")

# On créé un nouveau dataframe qui assemble les 2 dataframes en fonction du tite et qui ne garde que les films ayant une note
dfA = pd.merge(data_Amazon,data_movies_ratings, on='title', how='inner')

# On transforme la colonne "listed_in" en chaine de caractère et on duplique la ligne si le film a plusieurs genres pour pouvoir commpter sa note dans chaque des genres
dfA["listed_in"] = dfA["listed_in"].map(str)
dfA["listed_in"] = dfA["listed_in"].str.split(",")
dfA_explode = dfA.explode("listed_in")

# On affiche la moyenne des notes sur Amazon pour les films
liste_genres = ["Drama","Comedy","Action","Suspense","Kids"]
for i in liste_genres:
    mean = dfA_explode[dfA_explode['listed_in'] == i].mean()
    print("Sur Amazon Prime video, les films du genre", i, "ont une note moyenne de",mean)
    
# On créé un dataframe avec les titres de Disney où on ne garde que certaines colonnes et on ajoute une nouvelle colonne
data_Disney = pd.read_csv("disney_plus_titles.csv", 
                          sep=',')
data_Disney = data_Disney.drop(['show_id','director','cast','date_added','release_year','rating','duration','description'], axis=1)
data_Disney = data_Disney.assign(plateforme="Disney plus")

# On créé un nouveau dataframe qui assemble les 2 dataframes en fonction du tite et qui ne garde que les films ayant une note
dfD = pd.merge(data_Disney,data_movies_ratings, on='title', how='inner')

# On transforme la colonne "listed_in" en chaine de caractère et on duplique la ligne si le film a plusieurs genres pour pouvoir commpter sa note dans chaque des genres
dfD["listed_in"] = dfD["listed_in"].map(str)
dfD["listed_in"] = dfD["listed_in"].str.split(",")
dfD_explode = dfD.explode("listed_in")

# On affiche la moyenne des notes sur Disney pour les films
liste_genres = ["Family","Animation","Comedy","Action-Adventure","Comingof Age"]
for i in liste_genres:
    mean = dfD_explode[dfD_explode['listed_in'] == i].mean()
    print("Sur Disney +, les films du genre", i, "ont une note moyenne de",mean)
    
# On créé un dataframe avec les titres de Netflix où on ne garde que certaines colonnes et on ajoute une nouvelle colonne
data_Netflix = pd.read_csv("netflix_titles.csv", 
                          sep=',')
data_Netflix = data_Netflix.drop(['show_id','director','cast','date_added','release_year','rating','duration','description'], axis=1)
data_Netflix = data_Netflix.assign(plateforme="Netflix")
# On créé un nouveau dataframe qui assemble les 2 dataframes en fonction du tite et qui ne garde que les films ayant une note
dfN = pd.merge(data_Netflix,data_movies_ratings, on='title', how='inner')
# On transforme la colonne "listed_in" en chaine de caractère et on duplique la ligne si le film a plusieurs genres pour pouvoir commpter sa note dans chaque des genres
dfN["listed_in"] = dfN["listed_in"].map(str)
dfN["listed_in"] = dfN["listed_in"].str.split(",")
dfN_explode = dfN.explode("listed_in")

# On affiche la moyenne des notes sur Netflix pour les films
liste_genres = ["International Movies","Dramas","Comedies","Documentaries","Action & Adventure"]
for i in liste_genres:
    mean = dfN_explode[dfN_explode['listed_in'] == i].mean()
    print("Sur Netflix, les films du genre", i, "ont une note moyenne de",mean)
    
Genre = ["Drama","Comedy","Action","Suspense","Kids"]
Moyenne = [5.952701,5.718415,5.459028,5.572308,5.2375]
plt.bar(Genre, Moyenne, color="skyblue") # on crée un diagramme, qui mettra en absisses les genres et en ordonnés la moyenne associée
plt.title("Notes moyennes des films par genres sur Amazon") #titre
plt.xlabel("Genre") # axe des abscisses
plt.ylabel("Moyenne") # axe des ordonnés
plt.xticks(rotation=45) #rotation sur les données de l'axe X
plt.ylim(0,10) # l'axe des ordonnées va de 0 à 10
plt.show() # affichage du graphique

Genre = ["Family","Animation","Comedy","Action-Adventure"]
Moyenne = [5.133333,6.235417,5.98,6.205]
plt.bar(Genre, Moyenne, color="lightcoral") # on crée un diagramme, qui mettra en absisses les genres et en ordonnés la moyenne associée
plt.title("Notes moyennes des films par genres sur Disney") #titre
plt.xlabel("Genre") # axe des abscisses
plt.ylabel("Moyenne") # axe des ordonnés
plt.xticks(rotation=45) #rotation sur les données de l'axe X
plt.ylim(0,10) # l'axe des ordonnées va de 0 à 10
plt.show() # affichage du graphique

Genre = ["InternationalMovies","Dramas","Comedies","Action & Adventure","Documentaries"]
Moyenne = [5.6,6.238129,5.886082,5.901068,5.498039]
plt.bar(Genre, Moyenne, color="lightgreen") # on crée un diagramme, qui mettra en absisses les genres et en ordonnés la moyenne associée
plt.title("Notes moyennes des films par genres sur Netflix") # titre
plt.xlabel("Genre") # axe des abscisses
plt.ylabel("Moyenne") # axe des ordonnés
plt.xticks(rotation=45) #rotation sur les données de l'axe X
plt.ylim(0,10) # l'axe des ordonnées va de 0 à 10
plt.show() # affichage du graphique