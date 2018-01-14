import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys

'''
Argumentos:
argv1 -> idEstacion
argv2 -> idParametro
argv3 -> m/a para ver meses o años
(opcional)argv4 -> si m el año para ver los meses
'''

#Declaraciones iniciales
columnas = ['idEstacion','idParametro','idTecnica','anyo','mes','dia1','dia2','dia3','dia4','dia5','dia6','dia7','dia8','dia9','dia10','dia11','dia12','dia13','dia14','dia15','dia16','dia17','dia18','dia19','dia20','dia21','dia22','dia23','dia24','dia25','dia26','dia27','dia28','dia29','dia30','dia31']
columnasMensuales = ['idEstacion','idParametro','idTecnica','anyo','mes','AVG']
columnasAnuales = ['idEstacion','idParametro','idTecnica','anyo','AVG']

Parametros = {"1":"Dioxido de Azufre",
              "6":"Monoxido de Carbono",
              "7":"Monoxido de Nitrogeno",
              "8":"Dioxido de Nitrogeno",
              "9":"Particulas < 2.5 pm",
              "10":"Particulas < 10 pm",
              "12":"Oxidos de Nitrogeno",
              "14":"Ozono",
              "20":"Tolueno",
              "30":"Benceno",
              "35":"Etilbenceno",
              "37":"Metaxileno",
              "38":"Paraxileno",
              "39":"Ortoxileno",
              "42":"Hidrocarburos totales",
              "43":"Metano",
              "44":"Hidrocarburos no metanicos"}

Meses = {"1":"Enero",
         "2":"Febrero",
         "3":"Marzo",
         "4":"Abril",
         "5":"Mayo",
         "6":"Junio",
         "7":"Julio",
         "8":"Agosto",
         "9":"Septiembre",
         "10":"Octubre",
         "11":"Noviembre",
         "12":"Diciembre"}



# Get current size
fig_size = plt.rcParams["figure.figsize"]

# Set figure width to 12 and height to 9
fig_size[0] = 12
fig_size[1] = 9



if(sys.argv[3] == "m"):
    #Cargamos los datos
    data = pd.read_csv('tablaAVG', header = None, names = columnasMensuales)
    data = data.loc[data['idEstacion'] == int(sys.argv[1])]
    data = data.loc[data['idParametro'] == int(sys.argv[2])]
    data = data.loc[data['anyo'] == int(sys.argv[4])]
    #Descomponemos los meses en un array sin repeticiones
    ar = np.unique(data.mes.values)



    plt.plot(data.mes.values, data.AVG.values, label=sys.argv[1])
    plt.xlabel('Meses')
    plt.title('Grafica Mensual')


else:
  #Cargamos los datos
    data = pd.read_csv('tablaAVGAnyo', header = None, names = columnasAnuales)
    data = data.loc[data['idEstacion'] == int(sys.argv[1])]
    data = data.loc[data['idParametro'] == int(sys.argv[2])]
    #Descomponemos los meses en un array sin repeticiones
    ar = np.unique(data.anyo.values)



    plt.plot(data.anyo.values, data.AVG.values, label=sys.argv[1])
    plt.xlabel('Años')
    plt.title('Grafica Anual')


plt.ylabel(Parametros[str(sys.argv[2])])
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
