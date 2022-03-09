import pandas as pd
import numpy as np

# On rajoute une colonne contenant le nom de la plateforme dans chacun des 3 df.

data_Amazon = pd.read_csv("amazon_prime_titles.csv", sep=',')
data_Amazon= data_Amazon.assign(plateforme="Amazon prime")
data_Disney = pd.read_csv("disney_plus_titles.csv", sep=',')
data_Disney= data_Disney.assign(plateforme="Disney plus")
data_Netflix = pd.read_csv("netflix_titles.csv", sep=',')#lecture des fichiers CVS, création des dataframes
data_Netflix = data_Netflix.assign(plateforme="Netflix")#Ajout d'une colonne avec le nom de la plateforme à chaque ligne

#séparation des trois dataframes en deux à chaque fois, selon le type de contenu : film ou série

groupsA = data_Amazon.groupby(data_Amazon.type)
Movie_Amazon= groupsA.get_group("Movie")
TV_Amazon=groupsA.get_group("TV Show")

groupsD = data_Disney.groupby(data_Disney.type)
Movie_Disney= groupsD.get_group("Movie")
TV_Disney=groupsD.get_group("TV Show")

groupsN = data_Netflix.groupby(data_Netflix.type)
Movie_Netflix= groupsN.get_group("Movie")
TV_Netflix=groupsN.get_group("TV Show")


def searchbyTG(Type, Genre):       

    
    """
    Input: (type: str) La focntion prend en entrée le type de contenu voulu (série ou film) et le genre
    
    Output: La fonction ressort le nombre de résultat qui satisfont les deux critères et 3 exemples de  
    """
    if Type=='Film':#Boucle qui vérifie que le type entré en input est valable. En plus, il renomme le type en anglais pour s'accorder avec le dataframe
        Type='Movie'
    elif Type=='Série':
        Type='TV Show'
    else:
        Type='Nada'
        #print('Vous avez mal écrit le type, veuillez saisir Film ou Série.')
        
    if Type=='Movie':#Boucle qui attribue les dataframes correctes selon le type entré par l'utilisateur
        dfA=Movie_Amazon
        dfD=Movie_Disney
        dfN=Movie_Netflix
    elif Type=='TV Show' :
        dfA=TV_Amazon
        dfD=TV_Disney
        dfN=TV_Netflix

    elif Type=='Nada':#sinon les dataframes sont vide
        dfA = pd.DataFrame(columns=['show_id','type','title','director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'plateforme'])
        dfD = pd.DataFrame(columns=['show_id','type','title','director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'plateforme'])
        dfN = pd.DataFrame(columns=['show_id','type','title','director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'plateforme'])
    
    #On recherche une liste propre avec chaque genre qui existe
    ClistA=dfA['listed_in'].to_list() #Convertir les trois colonnes de genre dans une liste
    ClistD=dfD['listed_in'].to_list()
    ClistN=dfN['listed_in'].to_list() 

    str_list_0A = ",".join(ClistA) #Convertir les listes en strings
    str_list_0D = ",".join(ClistD)
    str_list_0N = ",".join(ClistN)
 

    str_list_0Tot = str_list_0A+ str_list_0D+str_list_0N #concaténer les trois strings
    str_list_0Tot = str_list_0Tot.replace(" ", "")#suprimer les espaces dans le string total
    outputTotal=str_list_0Tot.split(',')#On retransforme le string total en liste 
    setGenres=set(outputTotal)#puis en set pour obtenir des valeurs uniques - sans répétitions
    
    if Genre in setGenres: #si le genre rentré en input existe dans le set des genres, alors on définit notre dataframe (dans lequel on recherchera nos films) comme le dataframe d'une plateforme où le genre est respecté
        dfA=dfA[dfA['listed_in'].str.contains(Genre)] #ça nous donne un dataframe de tous les films avec le genre demandé
        dfD=dfD[dfD['listed_in'].str.contains(Genre)]
        dfN=dfN[dfN['listed_in'].str.contains(Genre)]
        

    else:#sinon, on obtient un dataframe vide car aucun genre ne correspond à l'input
        # ! print("Le genre renseigné n'existe pas !" )
        dfA = pd.DataFrame(columns=['show_id','type','title','director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'plateforme'])
        dfD = pd.DataFrame(columns=['show_id','type','title','director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'plateforme'])
        dfN = pd.DataFrame(columns=['show_id','type','title','director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description', 'plateforme'])
    
    nbrowsA = dfA.shape[0] #on compte le nombre de ligne de chaque dataframe. Ca nous donne le nombre de films qui correspondent aux deux critères (type + genre)
    nbrowsD = dfD.shape[0]
    nbrowsN = dfN.shape[0]

    SnbrowsA = str(nbrowsA) #le nombre de film converti en str pour l'afficher ensuite
    SnbrowsD = str(nbrowsD)
    SnbrowsN = str(nbrowsN)

    if Type=='Movie':#Boucle qui attribue les dataframes corrects selon le type entré par l'utilisateur
        print ("Il y a " + SnbrowsA + " films qui correspondent à vos attentes sur Amazon Prime, " + SnbrowsD + " films sur Disney+ et " + SnbrowsN + " films sur Netflix. ")
    elif Type=='TV Show' :
        print ("Il y a " + SnbrowsA + " séries qui correspondent à vos attentes sur Amazon Prime, "+ SnbrowsD + " séries sur Disney+ et " + SnbrowsN + " séries sur Netflix.")
    #trie des dataframes par la colonne de date de sortie des films, des plus récents aux plus anciens
    dfA=dfA.sort_values(by=['release_year'],ascending=False) #grâce à ça on obtient un dataframe trié avec les films les plus récent en haut du dataframe
    dfD=dfD.sort_values(by=['release_year'],ascending=False)
    dfN=dfN.sort_values(by=['release_year'],ascending=False)


    if Genre in setGenres:
        return(display(dfA.head(3)),display(dfD.head(3)), display(dfN.head(3)))#on return les 3 films les plus récents qui correspondent aux deux crières, sachant qu'ils se trouvent au niveau des trois premières lignes des dataframes
    else:
        return("\n Nous sommes désolés, mais il n'existe aucune donnée correspondante à vos attentes :( " )
    