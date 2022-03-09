
# On importe les librairies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df1 = pd.read_csv('amazon_prime_titles.csv',sep=',')
df1.name = 'Amazon Prime'

df2 = pd.read_csv('disney_plus_titles.csv',sep=',')
df2.name = 'Disney+'

df3 = pd.read_csv('netflix_titles.csv',sep=',')
df3.name = 'Netflix'

df4 = pd.read_csv('movies_ratings_IMDB.csv',sep=',')
df4.name = 'Notes'

def evolution1 (df):
    """
    la colonne Date_added est composée de str et d'int, donc on sépare en deux colonnes celle-ci grâce à la virgule 
    (exemple :"September 24, 2021" devient d'une part "September 24" dans la colonne To erase et d'autre part "2001" 
    dans la colonne Year_added) 
    """
    df[['To erase', 'year_added']] = df['date_added'].str.split(',', 1, expand=True)
    
    #pour avoir un graphique coloré
    if "Amazon" in df.name:
        mycolor='yellow'
    elif "Disney" in df.name:
        mycolor='magenta'
    elif "Netflix" in df.name:
        mycolor='red'
    else:
        mycolor=blue
       
    df['year_added'].value_counts(dropna=False).plot(kind='bar', color=mycolor)#on compte les occurrences, en comptant aussi les NaN avec dropna=False
    plt.title("Graphique 1 : graphiques en barres sans retirer les valeurs manquantes de la colonne d'intérêt - "+df.name)
    plt.show()#on plot, et on se rend compte qu'il manque bcp de données pour la colonne year_added pour le premier dataframe

evolution1(df1)
evolution1(df2)
evolution1(df3)
#Conclusion: pas la peine d'approfondir l'analyse graphique sur df1(Amazon Prime) car il y beaucoup trop de valeurs manquantes

def evolutionMarginale(df):
    #comme auparavant, on sépare la colonne date_added en deux, pour ne garder que l'année
    df[['To erase', 'year_added']] = df['date_added'].str.split(',', 1, expand=True)
    #print(df)
    #création d'une liste avec les années qui sont les index dans la fonctions value_counts
    List1=df["year_added"].value_counts().index.tolist()
    #création d'une liste avec l'occurrence de chaque année
    List2=df['year_added'].value_counts().tolist()
    #print(List1)
    #print(List2)

    #On va rasssembler les deux liste dans un dataframe pour le trier dans l'ordre chronologique et tracer son graphique
    dfQ2 = pd.DataFrame()  
    #print(dfQ2)
    # A partir d'un dictionnaire composé des deux listes, on remplit le dataframe
    dico = {'Année': List1, 'films/séries ajoutés chaque année': List2}
    dfQ2 = pd.DataFrame(dico) 
    #print(dfQ2)
    
    #on trie le dataframe par ordre croissant donc chronologique puisqu'il s'agit des années
    dfQ2=dfQ2.sort_values(by=['Année'])
    #print(dfQ2)
    
    #je retire les années pendant lesquelles moins de 5 films/séries ont été ajoutés à la plateforme
    finaldfQ2=dfQ2.loc[dfQ2["films/séries ajoutés chaque année"]>=5]
    #print(finaldfQ2)
    
    #pour choisir la couleur du graphique on regarde si Amazon, Disney ou Netflix figure dans le nom du df(le nom a été défini au tout début)
    if "Amazon" in df.name:
        mycolor='yellow'
    elif "Disney" in df.name:
        mycolor='magenta'
    elif "Netflix" in df.name:
        mycolor='red'
    else:
        mycolor='blue'
    
    
    #tracer le graphique avec seulement les années pendant lesquelles plus de 4 films/séries ont été ajoutés à la plateforme 
    finaldfQ2.plot(x ='Année', y='films/séries ajoutés chaque année', kind = 'bar',color=mycolor)
    plt.xticks(x='Année', rotation='horizontal')
    plt.title("Graphique 2 : Evolution marginale par année - "+df.name)
    plt.show()
evolutionMarginale(df2)
evolutionMarginale(df3)

#Je veux une évolution de stock pas de flux comme les graphiques de la fonction 'evolution2'
#je refais la même fonction mais ici on va empiler les barres d'une année à l'autre pour avoir l'évolution du stock de film


def evolutionBrute (df):
    #comme auparavant, on sépare la colonne date_added en deux, pour ne garder que l'année
    df[['To erase', 'year_added']] = df['date_added'].str.split(',', 1, expand=True)
    #print(df)
    #création d'une liste avec les années qui sont les index dans la fonctions value_counts
    List1=df["year_added"].value_counts().index.tolist()
    #création d'une liste avec l'occurrence de chaque année
    List2=df['year_added'].value_counts().tolist()
    #print(List1)
    #print(List2)

    #On va rasssembler les deux liste dans un dataframe pour le trier dans l'ordre chronologique et tracer son graphique
    #On rassemble dans deux listes du dessus dans un dictionnaire. 
    dico = {'Année': List1, 'films/séries ajoutés chaque année': List2}
    dfQ2 = pd.DataFrame()#On crée le dataframe à partir du dictionnaire
    dfQ2 = pd.DataFrame(dico) 
    #print(dfQ2)
    
    #on trie le dataframe par ordre croissant donc chronologique puisqu'il s'agit des années
    dfQ2=dfQ2.sort_values(by=['Année'], ascending=True)
    #print(dfQ2)    
    dfQ2=dfQ2.reset_index()
    # print(dfQ2)
    for i in range(1,len(dfQ2['Année'])):
        dfQ2['films/séries ajoutés chaque année'][i]=dfQ2['films/séries ajoutés chaque année'][i]+dfQ2['films/séries ajoutés chaque année'][i-1]
    #print(dfQ2)

    if "Amazon" in df.name:
        mycolor='yellow'
    elif "Disney" in df.name:
        mycolor='magenta'
    elif "Netflix" in df.name:
        mycolor='red'
    else:
        mycolor='blue'
    #je retire les années pendant lesquels moins de 5 films/séries ont été ajoutés à la plateforme
    dfQ2=dfQ2.loc[dfQ2["films/séries ajoutés chaque année"]>=5]
      
    #tracer le graphique avec seulement les années pendant lesquelles plus de 4 films/séries ont été ajoutés à la plateforme 
    dfQ2.plot(x ='Année', y='films/séries ajoutés chaque année', kind = 'bar',color=mycolor, rot=45)
    plt.xticks(x='Année', rotation='horizontal')
    plt.title("Graphique 3 : Evolution cumulée par année - "+df.name)
    plt.show()
evolutionBrute(df2)
evolutionBrute(df3)

def AnalyseDesSorties (DF, LancementPlateforme):
    
    ListToMin=DF['release_year'].value_counts().index.tolist()#liste pour trouver la date de parution du plus vieux film
    #print(ListToMin)
    Min=ListToMin[0]
    for i in range (len(ListToMin)):#début d'une boucle pour trouver le minimum
        if Min>ListToMin[i]:
            Min=ListToMin[i]
    #print ("Min=" , Min)

    Duree=2021-LancementPlateforme#calcul de la période entre le lancement de la plateforme et aujourd'hui
    #print(Duree)
    BinsNumber=(2021-Min)/Duree#permet de savoir en combien de catégories on veut couper notre échantillon avec l'argument Bins dans la fonctions Value_counts
    #print('BinsNumber=',BinsNumber)
    BinsNumeric=round(BinsNumber)#BinsNumeric est la période (arrondie) en année pour découper le temps...
    #print('BinsNumeric=',BinsNumeric)
    
    #On crée une liste des valeurs(année) qui séparent chaque période. le but est d'utiliser celle-ci pour l'argument Bins 
    binsList = []
    X=2021
    while X>Min:
        binsList.append(X)
        X=X-BinsNumeric
    #print('binsList=',binsList)
    Ascending = sorted(binsList, reverse=False)#pour avoir la liste des années binsList triée par ordre chronologique
    print('Ascending=',Ascending)
    
    if "Amazon" in DF.name:#boucle pour définir une couleur adaptée pour les graphiques
        mycolor='yellow'
    elif "Disney" in DF.name:
        mycolor='magenta'
    elif "Netflix" in DF.name:
        mycolor='red'
    else:
        mycolor=blue
    
    #le moment de tracer le graphique, en calculant le nombre de films parus entre deux dates
    DF['release_year'].value_counts(ascending=True, bins=Ascending).plot(kind='bar',rot=45, color=mycolor)
    plt.title('Graphique 4 : Nombre des films/séries, avec les films/séries classés par période de sortie en salle - '+DF.name)
    plt.show()
    
AnalyseDesSorties(df1,2016)
AnalyseDesSorties(df2,2017)
AnalyseDesSorties(df3,2007)

def partype(df):
    df['type'].unique()#on cherche tous les types d'oeuvre cinématographique. On obtient une liste avec Movie et TV Show normalement
    #print(df['type'].unique())
    
    WorkList=df['type'].unique()#on nomme cette liste WorkList
    if WorkList[0]=='Movie' and WorkList[1]=='TV Show' and len(WorkList)==2:#on vérifie qu'il n'y a que deux types, et que les deux types sont des films et séries (puisque c'est une liste, les éléments sont ordonnés, donc Movie sera toujours en permière position avant TV Show)
        dff=df[df['type'] == "Movie" ]#avec ces deux lignes, on sépare le dataframe df en deux, avec d'un côté un dataframe rempli de film et de l'autre un df rempli de séries
        dfs=df[df['type'] == "TV Show" ]
        #print("Comme prévu, il n'y a que deux types d'oeuvres, film ou série")
    """else:
        print("Il n'y a pas que des films/séries")"""
    
    #étape de vérification intermédiaire des données
    """if len(dff)+len(dfs)==len(df):#si la somme des lignes des deux dataframes est égale au nombre de ligne de mon premier dataframe alors
        print('Chaque film/série du dataframe en question est associé à un type')#On a bien gardé tous les oeuvres
    else:
        print("Il semble y avoir un problème, on devrait avoir autant de films/séries dans nos deux df que dans le premier"""
    
    #comme auparavant, on sépare la colonne date_added en deux, pour ne garder que l'année
    dff[['To erase', 'year_added']] = dff['date_added'].str.split(',', 1, expand=True)
    dfs[['To erase', 'year_added']] = dfs['date_added'].str.split(',', 1, expand=True)

    #création d'une liste avec les années qui sont les index dans la fonctions value_counts
    List1f=dff["year_added"].value_counts().index.tolist()
    List1s=dfs["year_added"].value_counts().index.tolist()
    #création d'une liste avec l'occurrence de chaque année
    List2f=dff['year_added'].value_counts().tolist()
    List2s=dfs['year_added'].value_counts().tolist()
    """print(len(List1f))
    print(len(List2f))
    print(len(List1s))
    print(len(List2s))"""
    

    
    if len(List1f)==len(List1s):#On va rasssembler les deux listes dans un dataframe pour le trier dans l'ordre chronologique et tracer son graphique
        dfQFS = pd.DataFrame()  
        # A partir d'un dictionnaire composé des deux listes à la fois, on remplit le dataframe
        dicoFS = {'Année': List1f, 'films ajoutés chaque année': List2f, 'séries ajoutées chaque année': List2s}
        dfQFS = pd.DataFrame(dicoFS) 
        #on trie le dataframe par ordre croissant donc chronologique puisqu'il s'agit des années
        dfQFS=dfQFS.sort_values(by=['Année'])    
        #Ce nouveau dataframe nous permet de tracer les graphiques
        print("Graphiques 5: " +df.name +"Evolution marginale selon le type de contenu. Même nombre de lignes dans les dataframes films/séries <=> le premier film est a été ajouté la même année que la première série. On peut rassembler tout dans un seul graphique:")
        dfQFS.plot(x ='Année', y=['films ajoutés chaque année', 'séries ajoutées chaque année'], kind = 'bar',color=['skyblue', 'lightcoral'])
        plt.xticks(rotation=30)
        plt.show()
        
    else:#on ne rassemble pas les deux listes en un seul dataframe car il n'y a pas autant d'années dans les deux listes
        dfQF = pd.DataFrame()  
        dfQS = pd.DataFrame()
        # A partir d'un dictionnaire composé des deux listes, on remplit le dataframe
        dicoF = {'Année': List1f, 'films ajoutés chaque année': List2f}
        #print(dicoF)
        dfQF = pd.DataFrame(dicoF) 
        dicoS = {'Année': List1s, 'séries ajoutées chaque année': List2s}
        dfQS = pd.DataFrame(dicoS) 
        #on trie le dataframe par ordre croissant donc chronologique puisqu'il s'agit des années
        dfQF=dfQF.sort_values(by=['Année'])
        dfQS=dfQS.sort_values(by=['Année'])
        #print(dfQF)
        #Tracer les deux graphiques côte à côte
        print("Graphiques 5: " +df.name +"Evolution marginale selon le type de contenu. Nombre différent de lignes dans les dataframes films/séries <=> le premier film est n'a pas été ajouté la même année que la première série. On préfère ne pas rassembler tout dans un seul graphique:")
        fig, axes = plt.subplots(1,2, figsize=(15,5))
        dfQF.plot(x ='Année', y='films ajoutés chaque année', kind = 'bar',ax=axes[0], color='skyblue')
        dfQS.plot(x ='Année', y='séries ajoutées chaque année', kind = 'bar',ax=axes[1], color='lightcoral')
        plt.show()
partype(df2)
partype(df3)
