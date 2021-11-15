#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print(os.getcwd())


# In[2]:


#1. Importez le fichier de données “coeur” dans dans votre notebook à l’aide de pandas et stockez le dans un objet appelé “data”.

data = pd.read_excel('C:/Users/yakri/Downloads/Coeur.xlsx')


# In[3]:


#2. Faites une copie de l’objet “data” dans un nouvel objet appelé “df”.
df = pd.DataFrame(data)
df


# In[4]:


#3. Ecrire une fonction qui reçoit en entrée un DataFrame et qui nous retourne deux listes ; une liste avec le nom des colonnes et une liste avec le type de chaque colonne
def get_column(dataframe):
    x=dataframe.columns.values
    y=dataframe.dtypes
    return list(x),list(y)
columetype=get_column(df)
columetype


# In[7]:


#4. Ecrire une fonction qui permet de recoder la variable catégorielle sexe. 
def recodage_variable_sex(dataframe,homme,femme):
    dic = {"homme" : homme, "femme" : femme}
    dataframe['SEXE'].replace(dic, inplace=True)
    return dataframe
nvdata=recodage_variable_sex(df,homme=1,femme=0)
nvdata


# In[8]:


#5. Ecrire une fonction qui permet de recoder toutes les variables catégorielles du DataFrame
pd.get_dummies(df)
#def recodage_all_variable(dataframe)


# In[9]:


#6. Créer un DataFrame dénommé “df_2” qui contient uniquement les hommes qui ont une maladie cardiaque en utilisant la fonction “groupby”
df2=df.groupby(["SEXE", "CŒUR"]).get_group((1, 1))
df2


# In[10]:


#7. Faites un tableau de contingence entre la variable “SEXE” et la variable “COEUR”
data_crosstab = pd.crosstab(df['SEXE'],df['CŒUR'], margins = False)
data_crosstab


# In[11]:


#8. Afficher l’histogramme de la variable " AGE"
histogram_age=df["AGE"].hist()


# In[12]:


#8. 9. Afficher l’histogramme de la variable " AGE" pour chaque modalité de la variable “COEUR”

histogram_age_coeur=df["AGE"].hist(df['CŒUR'])


# In[31]:


#10. Affichez le nuage de point entre la variable " AGE" et la variable "DÉPRESSION" puis utiliser la variable ‘COEUR” pour la couleur des points

nuage_de_point=df.plot(x='AGE',y='DEPRESSION',s=5,c=np.where(df['CŒUR']==1, 'r', 'k'), kind="scatter")


# In[21]:


nuage_de_point=df.plot.scatter(x='AGE',y='DEPRESSION',style="CŒUR")


# In[28]:


#11. Stockez dans "liste qual" les noms des variables qualitatives et dans “liste_quant” celles des variables quantitatives.
qual=["SEXE","TDT","GAJ","ECG","ANGINE","PENTE",'CŒUR']
quant=["AGE","PAR","CHOLESTEROL","FCMAX","DEPRESSION"]


# In[40]:


#12. En utilisant “liste_quant”, faites une représentation graphique de chaque variable quantitative en utilisant une boucle for.
for x in range(len(quant)):    
    df[quant[x]].hist()


# In[38]:


#13. En utilisant “liste_qual”, faites une représentation graphique de chaque variable quantitative en utilisant une boucle for.
for x in range(len(qual)):    
    df[qual[x]].hist()


# In[ ]:




