
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


columnas = ['idEstacion','idParametro','idTecnica','anyo','mes','dia1','dia2','dia3','dia4','dia5','dia6','dia7','dia8','dia9','dia10','dia11','dia12','dia13','dia14','dia15','dia16','dia17','dia18','dia19','dia20','dia21','dia22','dia23','dia24','dia25','dia26','dia27','dia28','dia29','dia30','dia31']  
data = pd.read_csv('https://raw.githubusercontent.com/Wizsmiles/PrCloud/master/tablaFinal', header = None, names = columnas)
print(data)
    

plt.plot(data.idParametro.values, data.idTecnica.values)
plt.show()


        

