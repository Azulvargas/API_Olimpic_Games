# %% [markdown]
# # Notebook de desarrollo 
# ## API juegos olimpicos

# %%
# importando librerias
import pandas as pd
import numpy as np
from fastapi import FastAPI

# %% [markdown]
# - instanciando Fastapi

# %%
app = FastAPI()

# %% [markdown]
# ### Cargar Datasets

# %%
df = pd.read_parquet('Data/Dataset.parquet')

# %% [markdown]
# ## Funciones
# - Función inicio

# %%
app.get("/")
def index(): 
    return {"API:online"}

# %% [markdown]
# Función Medals

# %%
app.get("/medals")
def medals():
    medals = df['Medal'].value_counts()
    return {medals.index[0]:medals.values[0],medals.index[1]:medals.values[1],medals.index[2]:medals.values[2]}

# %%
@app.get("/medals{medal}")
def medals():
    medal = df['Medal'].value_counts()
    dic={}
    for i in range(len(medal)):
        dic[medal.index[i]]=medal.values[i]

# %% [markdown]
# ## Función medal_country(país)

# %%
@app.get("/medals_country/{pais}")
def medals_country(pais:str):
    filtro = df[df['Team'] == pais]
    medallas = filtro['Medal'].value_counts()
    dic = {}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic

# %%
medals_country('Italy')

# %%
@app.get("/medal_year/{year}")
def medal_year(year:int):
    filtro = df[df['Year'] == year]
    medallas = filtro['Medal'].value_counts()
    dic = {}
    for i in range(len(medallas)):
        dic[medallas.index[i]]=int(medallas.values[i])
    return dic

# %%
@app.get("/athletes/{nombre}")
def athletes (nombre:str):
    filtro = df[df['Name'] == nombre]
    dic={}
    if filtro.empty:
        return{'Error':'Revise los datos ingresados'}
    dic['Nombre']=nombre
    dic['sexo']=filtro['Sex'].values[0]
    dic['Edad']=int(filtro['Age'].values[0])
    dic['Pais']=list(filtro['Team'].value_counts().index)
    dic['Juegos']=list(filtro['Games'].value_counts().index)
    dic['Evento']=list(filtro['Event'].value_counts().index)
    medallas={}
    for i in range(len(filtro['Medal'].value_counts())):
        medallas[filtro['Medal'].value_counts().index[i]]=int(filtro['Medal'].value_counts().values[i])
    dic['Medallas']=medallas
    return dic

# %%
athletes('Edgar Lindenau Aabye')


