import pandas as pd
import numpy as np

# On créé un dataframe avec les notes présentes dans le fichier CSV
# On garde 2 colonnes
# On met les titres en minuscules

df_note = pd.read_csv("movies_ratings_IMDB.csv", sep=',') 
df_note = df_note[["title","avg_vote"]]
df_note["title"] = df_note["title"].str.lower()

# On créé un dataframe avec les titres de chacunes des plateformes
# On rajoute une colonne contenant le nom de la plateforme dans chacun des 3 df.
# On garde certaines colonnes
# On met les titres en minuscules
# On fusionne les films avec leurs notes s'ils en ont une (left)
#On trie les df en fonction de l'année de réalisation du film
# On passe certaines colonnes en string et on rajoute une ligne à chaque fois qu'un film a plusieurs genres/pays/acteurs pour pouvoir les prendre à part ensuite

data_Amazon = pd.read_csv("amazon_prime_titles.csv", sep=',') 
data_Amazon = data_Amazon.assign(plateforme="Amazon prime")
data_Amazon = data_Amazon[["title","type","listed_in","country","plateforme","release_year","description","cast"]]
data_Amazon["title"] = data_Amazon["title"].str.lower()
data_Amazon = pd.merge(data_Amazon,df_note, on='title', how='left')
data_Amazon = data_Amazon.sort_values(by=['release_year'],ascending=False) 
data_Amazon["cast"] = data_Amazon["cast"].map(str).str.split(",")
data_Amazon_explode_cast = data_Amazon.explode("cast")
data_Amazon["country"] = data_Amazon["country"].map(str).str.split(",")
data_Amazon_explode_country = data_Amazon.explode("country")
data_Amazon["listed_in"] = data_Amazon["listed_in"].map(str).str.split(",")
data_Amazon_explode_listed_in = data_Amazon.explode("listed_in")

data_Disney = pd.read_csv("disney_plus_titles.csv", sep=',') 
data_Disney = data_Disney.assign(plateforme="Disney plus")
data_Disney = data_Disney[["title","type","listed_in","country","plateforme","release_year","description","cast"]]
data_Disney["title"] = data_Disney["title"].str.lower()
data_Disney = pd.merge(data_Disney,df_note, on='title', how='left')
data_Disney = data_Disney.sort_values(by=['release_year'],ascending=False) 
data_Disney["cast"] = data_Disney["cast"].map(str).str.split(",")
data_Disney_explode_cast = data_Disney.explode("cast")
data_Disney["country"] = data_Disney["country"].map(str).str.split(",")
data_Disney_explode_country = data_Disney.explode("country")
data_Disney["listed_in"] = data_Disney["listed_in"].map(str).str.split(",")
data_Disney_explode_listed_in = data_Disney.explode("listed_in")

data_Netflix = pd.read_csv("netflix_titles.csv", sep=',') 
data_Netflix = data_Netflix.assign(plateforme="Netflix")
data_Netflix = data_Netflix[["title","type","listed_in","country","plateforme","release_year","description","cast"]]
data_Netflix["title"] = data_Netflix["title"].str.lower()
data_Netflix = pd.merge(data_Netflix,df_note, on='title', how='left')
data_Netflix = data_Netflix.sort_values(by=['release_year'],ascending=False) 
data_Netflix["cast"] = data_Netflix["cast"].map(str).str.split(",")
data_Netflix_explode_cast = data_Netflix.explode("cast")
data_Netflix["country"] = data_Netflix["country"].map(str).str.split(",")
data_Netflix_explode_country = data_Netflix.explode("country")
data_Netflix["listed_in"] = data_Netflix["listed_in"].map(str).str.split(",")
data_Netflix_explode_listed_in = data_Netflix.explode("listed_in")


# On créé une fonction avec les préférences
def préférences_search(type_search, listed_in_search, avg_vote_search, country_search, cast_search):

    # On créé une fonction avec les types
    def type_search(type_search_A,type_search_D,type_search_N):

        def type_search_A(type):
            col_type=[x for x in data_Amazon["type"]]
            if type in col_type:
                return(display((data_Amazon.loc[data_Amazon["type"]== type].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        type_search_A("TV Show") 
        def type_search_D(type):
            col_type=[x for x in data_Disney["type"]]
            if type in col_type:
                return(display((data_Disney.loc[data_Disney["type"]== type].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        type_search_D("TV Show")
        def type_search_N(type):
            col_type=[x for x in data_Netflix["type"]]
            if type in col_type:
                return(display((data_Netflix.loc[data_Netflix["type"]== type].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        type_search_N("TV Show")

    type_search("TV Show","TV Show","TV Show")

    # On créé une fonction avec les genres
    def listed_in_search(listed_in_search_A,listed_in_search_D,listed_in_search_N):

    # On créé une fonction où l'utilisateur renseigne un genre de contenu et la fonction retourne du contenu correspondant à sa recherche

        def listed_in_search_A(listed_in):
            col_explode_listed_in=[x for x in data_Amazon_explode_listed_in["listed_in"]]
            if listed_in in col_explode_listed_in:
                return(display((data_Amazon_explode_listed_in.loc[data_Amazon_explode_listed_in["listed_in"] == listed_in].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        listed_in_search_A("Comedy")
        def listed_in_search_D(listed_in):
            col_explode_listed_in=[x for x in data_Disney_explode_listed_in["listed_in"]]
            if listed_in in col_explode_listed_in:
                return(display((data_Disney_explode_listed_in.loc[data_Disney_explode_listed_in["listed_in"] == listed_in].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        listed_in_search_D("Comedy")
        def listed_in_search_C(listed_in):
            col_explode_listed_in=[x for x in data_Netflix_explode_listed_in["listed_in"]]
            if listed_in in col_explode_listed_in:
                return(display((data_Netflix_explode_listed_in.loc[data_Netflix_explode_listed_in["listed_in"] == listed_in].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        listed_in_search_C("Comedies")

    listed_in_search("Comedy","Comedy","Comedies")

    # On créé une fonction avec les acteurs
    def avg_vote_search(avg_vote_A,avg_vote_D,avg_vote_N):

        def avg_vote_search_A(avg_vote):    
            col_avg_vote=[x for x in data_Amazon["avg_vote"]]
            if avg_vote in col_avg_vote:
                return(display((data_Amazon.loc[data_Amazon["avg_vote"] >= avg_vote].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        avg_vote_search_A(8)
        def avg_vote_search_D(avg_vote):    
            col_avg_vote=[x for x in data_Disney["avg_vote"]]
            if avg_vote in col_avg_vote:
                return(display((data_Disney.loc[data_Disney["avg_vote"] >= avg_vote].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        avg_vote_search_D(8)
        def avg_vote_search_N(avg_vote):    
            col_avg_vote=[x for x in data_Netflix["avg_vote"]]
            if avg_vote in col_avg_vote:
                return(display((data_Netflix.loc[data_Netflix["avg_vote"] >= avg_vote].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        avg_vote_search_N(8)

    avg_vote_search(8,8,8)
    
    # On créé une fonction avec les pays
    def country_search(country_search_A,country_search_D,country_search_N):

    # On créé une fonction où l'utilisateur renseigne un pays où le film a été tourné et la fonction retourne du contenu correspondant à sa recherche

        def country_search_A(country):
            col_explode_country=[x for x in data_Amazon_explode_country["country"]]
            if country in col_explode_country:
                return(display((data_Amazon_explode_country.loc[data_Amazon_explode_country["country"] == country].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        country_search_A("France")
        def country_search_D(country):
            col_explode_country=[x for x in data_Disney_explode_country["country"]]
            if country in col_explode_country:
                return(display((data_Disney_explode_country.loc[data_Disney_explode_country["country"] == country].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        country_search_D("France")
        def country_search_N(country):
            col_explode_country=[x for x in data_Netflix_explode_country["country"]]
            if country in col_explode_country:
                return(display((data_Netflix_explode_country.loc[data_Netflix_explode_country["country"] == country].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        country_search_N("France")

    country_search("France","France","France")
    
    # On créé une fonction avec les acteurs
    def cast_search(cast_search_A,cast_search_D,cast_search_N):

        # On créé une fonction où l'utilisateur renseigne le nom d'un acteur et la fonction retourne du contenu correspondant à sa recherche

        def cast_search_A(cast):
            col_explode_cast=[x for x in data_Amazon_explode_cast["cast"]]
            if cast in col_explode_cast:
                return(display((data_Amazon_explode_cast.loc[data_Amazon_explode_cast["cast"] == cast].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        cast_search_A("Kheiron")
        def cast_search_D(cast):
            col_explode_cast=[x for x in data_Disney_explode_cast["cast"]]
            if cast in col_explode_cast:
                return(display((data_Disney_explode_cast.loc[data_Disney_explode_cast["cast"] == cast].head(5))))
            else:
                return("Aucun résultat pour ce type de contenu")
        cast_search_D("Kheiron")
        def cast_search_N(cast):
            col_explode_cast=[x for x in data_Netflix_explode_cast["cast"]]
            if cast in col_explode_cast:
                return(display((data_Netflix_explode_cast.loc[data_Netflix_explode_cast["cast"] == cast].head(1))))
            else:
                return("Aucun résultat pour ce type de contenu")
        cast_search_N("Kheiron")

    cast_search("Kheiron","Kheiron","Kheiron")
    
préférences_search("TV Show","Comedy",8,"France","Kheiron")