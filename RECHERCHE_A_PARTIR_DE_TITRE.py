import pandas as pd
import numpy as np
# On rajoute une colonne contenant le nom de la plateforme dans chacun des 3 df. Ensuite on met en minuscule tous les titres
# afin de simplifier la recherche par la suite.

data_Amazon = pd.read_csv("amazon_prime_titles.csv", sep=',')
data_Amazon= data_Amazon.assign(plateforme="Amazon prime")
data_Amazon["title"]=data_Amazon["title"].str.lower()

data_Disney = pd.read_csv("disney_plus_titles.csv", sep=',')
data_Disney= data_Disney.assign(plateforme="Disney plus")
data_Disney["title"]=data_Disney["title"].str.lower()

data_Netflix = pd.read_csv("netflix_titles.csv", sep=',')
data_Netflix = data_Netflix.assign(plateforme="Netflix")
data_Netflix["title"]=data_Netflix["title"].str.lower()

df_note = pd.read_csv("movies_ratings_IMDB.csv", sep=',')
df_note["title"]=df_note["title"].str.lower()

df_concat= pd.concat([data_Amazon,data_Disney,data_Netflix]) # On concatène les 3 df

# On crée 2 sous dataframes avec les variables d'intérets qui nous intéressent (pour le df IMDb on s'intéresse qu'aux notes)
df_concat_col = df_concat[["title","plateforme","date_added","description","listed_in","cast","listed_in"]]
df_note_col = df_note[["title","avg_vote"]]
df_global=pd.merge(df_concat_col,df_note_col, on="title", how="left") # On conactène les 2 df de manière à avoir une colonne note qui affichera la note des films si elle existe sur IMDb

def title_search(title):
   
    """
    Input: (type: str) La focntion prend en entrée le titre d'une série ou d'un film
   
    Output: La fonction ressort le dataframe avec la/les ligne(s) associés au titre (quand il existe) avec les variabes d'intérets
    ainsi que la ligne du dataframe IMDb avec la note du titre si c'est est un film
     """
#On crée une fonction qui permet de changer systématiquement les caratères du titre en minuscule pour ne pas avoir de problème
# liés aux majuscules et minuscule afin de chercher dans les liste de titres qui sont également en minuscule.
    def transfo_minuscul(title):
        liste=[]
        for i in title:
            liste.append(i)
        liste=''.join(liste)
        liste=liste.lower()
        return(liste)

# On crée donc une liste avec tous les titres contenu dans le dataframe concaténé des 3 plateformes avec les variables d'intérets (df_concat_col).
# On fait également une liste avec tous les films contenu dans IMDb (df_note_col )

    col_title=[x for x in df_global["title"]]
    liste_title_note= [x for x in df_note_col["title"]]
   
# Si le titre entré est contenu dans dans la liste de titre du df concaténé ainsi que celle des films de IMDb,
# on affiche le dataframe avec les variables qui nous intéresses

    if transfo_minuscul(title) in col_title:
        return(display(df_global.loc[df_global["title"]== transfo_minuscul(title)]))
                 
# Si le titre n'est pas contenu dans le df concaténé mais qu'il est dans IMDb, c'est un film qui n'est sur aucune plateforme,
# si il n'est contenu dans aucun des 2 df, on affiche que la série ou le film n'existe pas sur les plateformes

    else:
        if transfo_minuscul(title) in liste_title_note :
            return("Le film n'existe pas sur la plateforme")
                   
        else:
            return("Le titre n'existe sur auncune plateforme")