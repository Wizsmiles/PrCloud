
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


columnas = ['idEstacion','idParametro','idTecnica','anyo','mes','dia1','dia2','dia3','dia4','dia5','dia6','dia7','dia8','dia9','dia10','dia11','dia12','dia13','dia14','dia15','dia16','dia17','dia18','dia19','dia20','dia21','dia22','dia23','dia24','dia25','dia26','dia27','dia28','dia29','dia30','dia31']
columnasAVG = ['idEstacion','idParametro','idTecnica','anyo','mes','AVG']

data = pd.read_csv('https://raw.githubusercontent.com/Wizsmiles/PrCloud/master/tablaAVG', header = None, names = columnasAVG)

data2 = data.loc[data['anyo'] == 2]
data2 = data2.loc[data2['idParametro'] == 1]

ar = np.unique(data2.idEstacion.values)
print(ar)
# Get current size
fig_size = plt.rcParams["figure.figsize"]

# Set figure width to 12 and height to 9
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size

for aux in ar:
    data3 = data2.loc[data2['idEstacion'] == aux]
    print(data3)
    plt.plot(data3.mes.values, data3.AVG.values, label=aux)


plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
