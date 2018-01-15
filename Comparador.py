import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys

'''
Argumentos:
argv1 -> idEstacion1
argv2 -> idEstacion2
argv3 -> idParametro
argv4 ->m/a meses o años
(opcional)argv5 -> año para mostrar los meses
'''

#Declaraciones iniciales
#columnas = ['idEstacion','idParametro','idTecnica','anyo','mes','dia1','dia2','dia3','dia4','dia5','dia6','dia7','dia8','dia9','dia10','dia11','dia12','dia13','dia14','dia15','dia16','dia17','dia18','dia19','dia20','dia21','dia22','dia23','dia24','dia25','dia26','dia27','dia28','dia29','dia30','dia31']
columnasMensuales = ['idEstacion','idParametro','idTecnica','anyo','mes','AVG']
columnasAnuales = ['idEstacion','idParametro','idTecnica','anyo','AVG']

Parametros = {"1":"Dioxido de Azufre (µg/m³)",
              "6":"Monoxido de Carbono (mg/m³)",
              "7":"Monoxido de Nitrogeno (µg/m³)",
              "8":"Dioxido de Nitrogeno (µg/m³)",
              "9":"Particulas < 2.5 pm (µg/m³)",
              "10":"Particulas < 10 pm (µg/m³)",
              "12":"Oxidos de Nitrogeno (µg/m³)",
              "14":"Ozono (µg/m³)",
              "20":"Tolueno (µg/m³)",
              "30":"Benceno (µg/m³)",
              "35":"Etilbenceno (µg/m³)",
              "37":"Metaxileno (µg/m³)",
              "38":"Paraxileno (µg/m³)",
              "39":"Ortoxileno (µg/m³)",
              "42":"Hidrocarburos totales (mg/m³)",
              "43":"Metano (mg/m³)",
              "44":"Hidrocarburos no metanicos (mg/m³)"}

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



if(sys.argv[4] == "m"):
    #Cargamos los datos
    data = pd.read_csv('tablaAVG', header = None, names = columnasMensuales)
    data = data.loc[data['idParametro'] == int(sys.argv[3])]
    data2 = data.loc[data['idEstacion'] == int(sys.argv[1])]
    data2 = data2.loc[data['anyo'] == int(sys.argv[5])]
    data3 = data.loc[data['idEstacion'] == int(sys.argv[2])]
    data3 = data3.loc[data['anyo'] == int(sys.argv[5])]
    #Descomponemos los meses en un array sin repeticiones
    ar = np.unique(data.mes.values)



    plt.plot(data2.mes.values, data2.AVG.values, label=sys.argv[1])
    plt.plot(data3.mes.values, data3.AVG.values, label=sys.argv[2])
    plt.xlabel('Meses')
    plt.title('Grafica Mensual')


else:
  #Cargamos los datos
    data = pd.read_csv('tablaAVGAnyo', header = None, names = columnasAnuales)
    data = data.loc[data['idParametro'] == int(sys.argv[3])]
    data2 = data.loc[data['idEstacion'] == int(sys.argv[1])]
    data3 = data.loc[data['idEstacion'] == int(sys.argv[2])]
    #Descomponemos los meses en un array sin repeticiones
    ar = np.unique(data.anyo.values)



    plt.plot(data2.anyo.values, data2.AVG.values, label=sys.argv[1])
    plt.plot(data3.anyo.values, data3.AVG.values, label=sys.argv[2])
    plt.xlabel('Años')
    plt.title('Grafica Anual')


plt.ylabel(Parametros[str(sys.argv[3])])
plt.grid(True)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
