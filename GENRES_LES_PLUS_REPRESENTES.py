# On importe les librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import operator    #pour trouver le maximum d'une cles dans un dictionnaire
from operator import itemgetter

path=os.getcwd()
print(path)

def genre_film(df):
    df1 = pd.read_csv(df, sep=',')
    colomn_list = df1['listed_in'].to_list()            #1. convertir la colonne dans une liste

    str_list_0 = ",".join(colomn_list)                             #convertir la liste dans un string
#print(str_list)

    str_list = str_list_0.replace(" ", "")                        #suprimer les espaces dans le string initial (str_list_0)
#print(str_list)

    list_0=[]                                                    #creer une liste vide pour l'incrementation de chaque genre/mot
    list_occurence=[]                                           #liste vide pour stovker les occurence des gendre de film
                                                      #2. transforme la chaîne de caractères dans une liste
    split_list =str_list.split(',')                              # je utilise la methode split qui divise une chaîne dans une liste où chaque mots représent un élément de liste
    #print(split_list)
                                                      #3. je parcours la liste des mots crée et je compte le nrb d'occurence de chaque mots(genre) : i=index/element/ genre de film de la liste
    for i in split_list:
    
        if i not in list_0:                                     #si le genre de filme n'est pas dans la liste_0 je l'ajoute dedans 
            list_0.append(i)                                    #je fait apparaitre l'incrementation pour chaque genre qu'une seule fois dans la liste vide
            compter = split_list.count(i)                       #compte le nrb des occurence pour chaque genre de film
            list_occurence.append(compter)                      #stocker les occurence dans une liste applée list_occurence
        
    dict_from_lists = dict(zip(list_0, list_occurence)) #4. creer un dictionner à partir de deux listes: list_occurence = les genre des filmes et list_0= nrb de repetition  
    sorted_dict_from_lists= sorted(dict_from_lists.items(), key=lambda x: x[1], reverse=True) #on sorte le dictionnare par ordre decroissant
    genre_le_plus_repeté =sorted_dict_from_lists[0:5] #extraire les premieres 5 elements du dictionaires (va servir pour faire le graphique)
    
    df_new = pd.DataFrame(genre_le_plus_repeté) #stocker le dictioner déjà trié dans une nouvelle dataframe 
    df_new=df_new.set_index(0) #supprimer les index de la nouvele dataframe
    return("Dans le catalogue " +str(df)+ ", les genres de films/séries les plus représentés sont:  ", display(df_new))


a= genre_film("amazon_prime_titles.csv")
d= genre_film("disney_plus_titles.csv")
n= genre_film("netflix_titles.csv")

print(a)
print(d)
print(n)



#Graphiques qu'on fait pour avoir les 5 genres les plus présents dans les 3 plateformes confondues
# Dataframe Concat obtenue en concatenant les trois dataframes
data_Netflix = pd.read_csv("netflix_titles.csv", sep=',')
data_Disney = pd.read_csv("disney_plus_titles.csv", sep=',')
data_Amazon = pd.read_csv("amazon_prime_titles.csv", sep=',')
df_concat= pd.concat([data_Netflix,data_Disney,data_Amazon]) # On concatène les 3 df 





#Graphique General
plateformes = ['Amazon Prime','Disney','Netflix']
nbr_pays = [3687,602,2752]
colors = ['red', 'magenta', 'yellow']
plt.bar(plateformes, nbr_pays, color=colors)
plt.title("Graphique 1: Genres de films&séries les plus représentés sur chaque plateforme de streaming")
plt.xlabel("Plateformes")
plt.ylabel("Nombre de genres de films/séries")
plt.show()

#Graphique Amazon
genre_films = ['Drama', 'Comedy', 'Action', 'Suspense', 'Kids']
nbr_pays = [3687,2099,1657,1501,1085]
fig = plt.figure(figsize=(5,5))
colors = "yellow"
plt.bar(genre_films, nbr_pays, color=colors)
plt.title("Graphique 2: Genres de films&séries les plus représentés sur Amazon Prime")
plt.xlabel("Genre de films/series")
plt.ylabel("Nombre de genres de films/séries")
plt.xticks(rotation=45)
plt.show()

#Graphique Disney
genre_films = ['International Movies', 'Dramas', 'Comedies', 'InternationalTVShows', 'Documentaries']
nbr_pays = [2752, 2427,1674, 1351, 869]
colors = "red"
fig = plt.figure(figsize=(5,5))
plt.bar(genre_films, nbr_pays, color=colors)
plt.title("Graphique 3 : Genres de films&séries les plus représentés sur Netflix")
plt.xlabel("Genre de films/series")
plt.ylabel("Nombre de genres de films/séries")
plt.xticks(rotation=45)
plt.show()

#Graphique Netflix
genre_films = ['Family', 'Animation', 'Comedies', 'Action-Adventure', 'Comingof Age']
nbr_pays = [602, 516,497,438, 199]
fig = plt.figure(figsize=(5,5))
plt.bar(genre_films, nbr_pays, color='magenta')
plt.title("Graphique 4 : Genres de films&séries les plus représentés sur Disney")
plt.xlabel("Genre de films/series")
plt.ylabel("Nombre de genres de films/séries")
plt.xticks(rotation=45)
plt.show()


def GenreParType_FouS(df):
    df1 = pd.read_csv(df, sep=',')
    
    df1['type'].unique()#on cherche tous les types d'oeuvre cinématographique. On obtient une liste avec Movie et TV Show normalement
    #print(df1['type'].unique())
    WorkList=df1['type'].unique()#on nomme cette liste WorkList
    #print(WorkList)
    if WorkList[0]=='Movie' and WorkList[1]=='TV Show' and len(WorkList)==2:#on vérifie qu'il n'y a que deux types, et que les deux types sont des films et séries (puisque c'est une liste, les éléments sont ordonnés, donc Movie sera toujours en permière position avant TV Show)
        dff=df1[df1['type'] == "Movie" ]#avec ces deux lignes, on sépare le dataframe df en deux, avec d'un côté un dataframe rempli de film et de l'autre un df rempli de séries
        dfs=df1[df1['type'] == "TV Show" ]
        #print("Comme prévu, il n'y a que deux types d'oeuvres, film ou série")
    else:
        print("Il n'y a pas que des films/séries")
    
    #pour le dataframe DFF, donc celui avec les films seulement
    colomn_listF = dff['listed_in'].to_list()            #1. convertir la colonne dans une liste
    str_list_0F = ",".join(colomn_listF)                             #convertir la liste dans un string
    #print(str_listF)

    str_listF = str_list_0F.replace(" ", "")                        #suprimer les espaces dans le string initial (str_list_0)
    #print(str_listF)

    list_0F=[]                                                    #creer une liste vide pour l'incrementation de chaque genre/mot
    list_occurenceF=[]                                           #liste vide pour stovker les occurence des gendre de film
                                                      #2. transforme la chaîne de caractères dans une liste
    split_listF =str_listF.split(',')                              # je utilise la methode split qui divise une chaîne dans une liste où chaque mots représent un élément de liste
    #print(split_listF)
                                    
    for i in split_listF:#3. je parcours la liste des mots crée et je compte le nrb d'occurence de chaque mots(genre) : i=index/element/ genre de film de la liste
        if i not in list_0F:                                     #si le genre de filme n'est pas dans la liste_0 je l'ajoute dedans 
            list_0F.append(i)                                    #je fait apparaitre l'incrementation pour chaque genre qu'une seule fois dans la liste vide
            compterF = split_listF.count(i)                       #compte le nrb des occurence pour chaque genre de film
            list_occurenceF.append(compterF)                      #stocker les occurence dans une liste applée list_occurence
        
    dict_from_listsF = dict(zip(list_0F, list_occurenceF)) #4. creer un dictionner à partir de deux listes: list_occurence = les genre des filmes et list_0= nrb de repetition  
    sorted_dict_from_listsF= sorted(dict_from_listsF.items(), key=lambda x: x[1], reverse=True) #on sorte le dictionnare par ordre decroissant
    genre_le_plus_repetéF =sorted_dict_from_listsF[0:5] #extraire les premieres 5 elements du dictionaires (va servir pour faire le graphique)
    
    df_newF = pd.DataFrame(genre_le_plus_repetéF) #stocker le dictioner déjà trié dans une nouvelle dataframe 
    df_newF=df_newF.set_index(0) #supprimer les index de la nouvele dataframe
    
    #pour le dataframe DFS, donc celui avec les séries seulement
    colomn_listS = dfs['listed_in'].to_list()            #1. convertir la colonne dans une liste
    str_list_0S = ",".join(colomn_listS)                             #convertir la liste dans un string
    #print(str_listS)

    str_listS = str_list_0S.replace(" ", "")                        #suprimer les espaces dans le string initial (str_list_0)
    #print(str_list)

    list_0S=[]                                                    #creer une liste vide pour l'incrementation de chaque genre/mot
    list_occurenceS=[]                                           #liste vide pour stovker les occurence des gendre de film
                                                      #2. transforme la chaîne de caractères dans une liste
    split_listS =str_listS.split(',')                              # je utilise la methode split qui divise une chaîne dans une liste où chaque mots représent un élément de liste
    #print(split_list)
                                    
    for i in split_listS:#3. je parcours la liste des mots crée et je compte le nrb d'occurence de chaque mots(genre) : i=index/element/ genre de film de la liste
        if i not in list_0S:                                     #si le genre de filme n'est pas dans la liste_0 je l'ajoute dedans 
            list_0S.append(i)                                    #je fait apparaitre l'incrementation pour chaque genre qu'une seule fois dans la liste vide
            compterS = split_listS.count(i)                       #compte le nrb des occurence pour chaque genre de film
            list_occurenceS.append(compterS)                      #stocker les occurence dans une liste applée list_occurence
        
    dict_from_listsS = dict(zip(list_0S, list_occurenceS)) #4. creer un dictionner à partir de deux listes: list_occurence = les genre des filmes et list_0= nrb de repetition  
    sorted_dict_from_listsS= sorted(dict_from_listsS.items(), key=lambda x: x[1], reverse=True) #on sorte le dictionnare par ordre decroissant
    genre_le_plus_repetéS =sorted_dict_from_listsS[0:5] #extraire les premieres 5 elements du dictionaires (va servir pour faire le graphique)
    
    df_newS = pd.DataFrame(genre_le_plus_repetéS) #stocker le dictioner déjà trié dans une nouvelle dataframe 
    df_newS=df_newS.set_index(0)
    
    #On trace les graphiques avec nos deux dataframes obtenus
    fig, axes = plt.subplots(1,2,figsize=(15, 5))
    df_newF.plot(kind='bar', title='Graphiques 5: Les genres de films sur : ' + df, xlabel='Genres de film', ylabel='Nombre de films', rot=45, ax=axes[0], color="skyblue")
    df_newS.plot(kind='bar', title='Graphiques 6 : Les genres de séries sur : ' + df, xlabel='Genres de film', ylabel='Nombre de films', rot=45, ax=axes[1], color="lightcoral" )
    plt.show()
    
    return()


a=GenreParType_FouS("amazon_prime_titles.csv")
d=GenreParType_FouS("disney_plus_titles.csv")
n=GenreParType_FouS("netflix_titles.csv")

print(a)
print(d)
print(n)

#puis on APPLIQUE LA FONCTION GENRE_FILM MAIS SANS LA PREMIERE LIGNE QUI SERT A LIRE UN FICHIER CSV (ON A DEJA LE DF DE PRET)
# question 1.3 PARTIE 1

def genre_filmDfPret(df1):
    colomn_list = df1['listed_in'].to_list()            #1. convertir la colonne dans une liste

    str_list_0 = ",".join(colomn_list)                             #convertir la liste dans un string
#print(str_list)

    str_list = str_list_0.replace(" ", "")                        #suprimer les espaces dans le string initial (str_list_0)
#print(str_list)

    list_0=[]                                                    #creer une liste vide pour l'incrementation de chaque genre/mot
    list_occurence=[]                                           #liste vide pour stovker les occurence des gendre de film
                                                      #2. transforme la chaîne de caractères dans une liste
    split_list =str_list.split(',')                              # je utilise la methode split qui divise une chaîne dans une liste où chaque mots représent un élément de liste
    #print(split_list)

                                                      #3. je parcours la liste des mots crée et je compte le nrb d'occurence de chaque mots(genre) : i=index/element/ genre de film de la liste
    for i in split_list:
    
        if i not in list_0:                                     #si le genre de filme n'est pas dans la liste_0 je l'ajoute dedans 
            list_0.append(i)                                    #je fait apparaitre l'incrementation pour chaque genre qu'une seule fois dans la liste vide
            compter = split_list.count(i)                       #compte le nrb des occurence pour chaque genre de film
            list_occurence.append(compter)                      #stocker les occurence dans une liste applée list_occurence
        
    
    dict_from_lists = dict(zip(list_0, list_occurence)) #4. creer un dictionner à partir de deux listes: list_occurence = les genre des filmes et list_0= nrb de repetition  
    sorted_dict_from_lists= sorted(dict_from_lists.items(), key=lambda x: x[1], reverse=True) #on sorte le dictionnare par ordre decroissant
    genre_le_plus_repeté =sorted_dict_from_lists[0:10] #extraire les premieres 5 elements du dictionaires (va servir pour faire le graphique)
    
    df_new = pd.DataFrame(genre_le_plus_repeté) #stocker le dictioner déjà trié dans une nouvelle dataframe 
    df_new.columns =['Genres', 'Nombre de  films&séries']
    df_new=df_new.set_index('Genres') #supprimer les index de la nouvele dataframe
    return(df_new)

C = genre_filmDfPret(df_concat)

#print(C)
#Enfin on trace le graphique
C.plot.barh(title="Graphique 7 : Les  genres les plus nombreux sur l'ensemble des trois plateformes", xlabel='Genres ', rot=45)
