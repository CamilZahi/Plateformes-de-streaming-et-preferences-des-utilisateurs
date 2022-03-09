# On importe les librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# On créé un dataframe avec les titres de Amazon Prime Video
data_Amazon = pd.read_csv("amazon_prime_titles.csv",
                          sep=',')
# On créé un dataframe avec les titres de Disney+
data_Disney = pd.read_csv("disney_plus_titles.csv",
                          sep=',')
# On créé un dataframe avec les titres de Netflix
data_Netflix = pd.read_csv("netflix_titles.csv",
                          sep=',')

def country_origin(df):
    '''
    Input: (type:str) La fonction prend en entrée le nom de la base de donnée d'une des plateforme
    Output: La fonction retourne le nombre de titres différents dans le catalogue de la plateforme choisie
   
    '''
    col_country=[x for x in pd.read_csv(df, sep=',')["country"]] # on crée une liste qui prend toute la colonne Country du dataframe
    newlist = [x for x in col_country if pd.isnull(x) == False and x != 'nan'] #on enlève les données manquantes caractérisés 'nan'
    newlist=",".join(newlist) #on transforme la liste en chaine de caratère pour effectuter des modifications
    list_split = [x.strip() for x in newlist.split(',')] # On retransaforme la chaine de caratère en liste avec la fonction strip() en précisant le séparateur
   
   #On crée ensuite un ditionaire qui va associer à chaque pays les nombres de films/séries existant afin de pouvoir ensuite compter le nombre de pays (clés)
    dico={}
    for i in range(len(list_split)) :      
        if not list_split[i] in dico:
            dico[list_split[i]]=1
       
        else:
            dico[list_split[i]]+=1  
    #On crée donc un compteur qui va ajouté 1 à sa valeur à chaque clé du dictionnaire (correspondant à un pays)        
    compteur=0
    for i in range(len(dico)):
        compteur+=1
    return("Dans le catalogue " + str(df) + ", il y a un nombre de titres issue de " + str(compteur) + " pays différents")


#On entre chaque base de donnée dans la fonction pour ensuite construire le diagramme.

netflix=country_origin("netflix_titles.csv")
print(netflix)
amazon=country_origin("amazon_prime_titles.csv")
print(amazon)
disney=country_origin("disney_plus_titles.csv")
print(disney)


# On crée ensuite le diagramme

plateformes = ["Netflix","Amazon Prime","Disney Plus"]
nbr_pays = [123,45,47]

plt.bar(plateformes, nbr_pays)
plt.title("Diagramme du nombre de pays représentés par plateforme")
plt.xlabel("Plateformes")
plt.ylabel("Nombre de pays représentés")
plt.show()