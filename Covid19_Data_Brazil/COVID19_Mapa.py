#!/usr/bin/env python
# coding: utf-8

# import pandas as pd
# import numpy as np
# 
# import folium
# from folium import plugins

# **GERANDO MAPA EM SVG**
# 

# In[73]:


mapa = folium.Map(
        width = 800, height = 600,
        location = [-15.77972, -47.92972],
        zoom_start = 4
)


# In[74]:


mapa


# In[75]:


mapa.save('covid-19.html')


# In[76]:


df = pd.read_csv('https://raw.githubusercontent.com/nelsonbjr/Covid19_Crisis/master/covid19-032bf512dadc43c2a4ae81337e96de96.csv')

df.head()


# In[77]:


estados = df.loc[df.place_type == 'state', ['state', 'confirmed', 'deaths', 'is_last']]
estados.head()


# In[78]:


estados.isnull().sum()


# In[79]:


estados.loc[estados.deaths.isnull(), 'deaths'] = 0


# In[80]:


estados.isnull().sum()


# In[81]:


ultimas = estados.loc[estados.is_last == True, ['state', 'confirmed', 'deaths']]


# In[82]:


ultimas['log_confirmed'] = np.log(ultimas['confirmed']+1)
ultimas['log_deaths']    = np.log(ultimas['deaths']+1)


# In[83]:


ultimas


# In[84]:


ultimas.head()


# In[85]:


import json

br_estados = 'br_states.json'
geo_json_data = json.load(open(br_estados))


# In[86]:


geo_json_data


# In[87]:


mapa.choropleth(
    geo_data = geo_json_data,
    name = "CASOS",
    data = ultimas,
    columns = ['state', 'log_confirmed'],
    key_on = 'feature.id',
    fill_color = 'Reds',
    fill_opacity = 0.8,
    line_color = 'white',
    line_opacity = 0.8,
    show = True,
    legend_name = 'Log de Casos de COVID-19 no Brasil',
    
)


# In[88]:


mapa


# In[89]:


mapa.save('covid-19_casos.html')


# In[92]:


mapa.choropleth(
    geo_data = geo_json_data,
    name = "MORTES",
    data = ultimas,
    columns = ['state', 'log_deaths'],
    key_on = 'feature.id',
    fill_color = 'GnBu',
    fill_opacity = 0.8,
    line_color = 'white',
    line_opacity = 0.8,
    show = False,
    legend_name = 'Log de Mortes de COVID-19 no Brasil',
    
)


# In[93]:


mapa


# In[94]:


mapa.save('covid-19_mortes.html')

