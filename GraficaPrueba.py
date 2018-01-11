
# coding: utf-8

# In[56]:


import csv, operator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('D:\Documentos\GitHub\PrCloud\dataFrame_prueba') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    ar = []
    for reg in entrada:
        ar.append(reg)
    lista = np.array(ar)
    columnas = ['idEstacion','idParametro','idTecnica','anyo','mes','dia1','dia2','dia3','dia4','dia5','dia6','dia7','dia8','dia9','dia10','dia11','dia12','dia13','dia14','dia15','dia16','dia17','dia18','dia19','dia20','dia21','dia22','dia23','dia24','dia25','dia26','dia27','dia28','dia29','dia30','dia31']
    filas = range(len(lista))
    df = pd.DataFrame(data = lista, columns = columnas, index = filas)
    
    '''
    alternativa 
    df = pd.DataFrame.from_csv('D:\Documentos\GitHub\PrCloud\dataFrame_prueba')
    print(df)
    '''
    
    plt.plot(df.dia29.values, df.dia28.values)
    plt.show()


        

