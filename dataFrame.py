from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import*
from pyspark.sql import*
from pyspark.sql import Row
import string

year = 17

# Configuracion inicial
conf = SparkConf().setMaster('local').setAppName('codigo')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

def loadData(file):
    dataText = sc.textFile(file)
    return dataText.flatMap(lambda l: l.split("\n")).map(lambda l: Row(idEstacion=l[0:8],idParametro=l[8:10], idTecnica=l[10:12], anyo=l[14:16], mes=l[16:18],dia1=l[18:24], dia2=l[24:30], dia3=l[30:36], dia4=l[36:42], dia5=l[42:48],dia6=l[48:54], dia7=l[54:60], dia8=l[60:66], dia9=l[66:72], dia10=l[72:78],dia11=l[78:84], dia12=l[84:90], dia13=l[90:96], dia14=l[96:102], dia15=l[102:108],dia16=l[108:114], dia17=l[114:120], dia18=l[120:126], dia19=l[126:132], dia20=l[132:138],dia21=l[138:144], dia22=l[144:150], dia23=l[150:156], dia24=l[156:162], dia25=l[162:168],dia26=l[168:174], dia27=l[174:180], dia28=l[180:186], dia29=l[186:192], dia30=l[192:198],dia31=l[198:204]))

RDDs = []
Data = []
Schema = []

for i in range(year):
    aux = ""
    aux2 = i+1
    if aux2 < 10:
        aux = "0" + str(aux2)
    else:
        aux = str(aux2)
    RDDs.append(sc.textFile("datos"+aux+".txt"))

# Carga de ficheros
'''
RDDDatos01 = sc.textFile("datos01.txt")
RDDDatos02 = sc.textFile("datos02.txt")
RDDDatos03 = sc.textFile("datos03.txt")
RDDDatos04 = sc.textFile("datos04.txt")
RDDDatos05 = sc.textFile("datos05.txt")
RDDDatos06 = sc.textFile("datos06.txt")
RDDDatos07 = sc.textFile("datos07.txt")
RDDDatos08 = sc.textFile("datos08.txt")
RDDDatos09 = sc.textFile("datos09.txt")
RDDDatos10 = sc.textFile("datos10.txt")
RDDDatos11 = sc.textFile("datos11.txt")
RDDDatos12 = sc.textFile("datos12.txt")
RDDDatos13 = sc.textFile("datos13.txt")
RDDDatos14 = sc.textFile("datos14.txt")
RDDDatos15 = sc.textFile("datos15.txt")
RDDDatos16 = sc.textFile("datos16.txt")
RDDDatos17 = sc.textFile("datos17.txt")
'''
# 1. Mapeo de datos y crear dataFrame

for j in range(year):
    Data.append(loadData(RDDs[j]))

'''
datos01 = loadData(RDDDatos01)
datos02 = loadData(RDDDatos02)
datos03 = loadData(RDDDatos03)
datos04 = loadData(RDDDatos04)
datos05 = loadData(RDDDatos05)
datos06 = loadData(RDDDatos06)
datos07 = loadData(RDDDatos07)
datos08 = loadData(RDDDatos08)
datos09 = loadData(RDDDatos09)
datos10 = loadData(RDDDatos10)
datos11 = loadData(RDDDatos11)
datos12 = loadData(RDDDatos12)
datos13 = loadData(RDDDatos13)
datos14 = loadData(RDDDatos14)
datos15 = loadData(RDDDatos15)
datos16 = loadData(RDDDatos16)
datos17 = loadData(RDDDatos17)
'''

for k in range(year):
    Schema.append(sqlContext.createDataFrame(Data[z]))

'''
datos01_schema = sqlContext.createDataFrame(datos01)
datos02_schema = sqlContext.createDataFrame(datos02)
datos03_schema = sqlContext.createDataFrame(datos03)
datos04_schema = sqlContext.createDataFrame(datos04)
datos05_schema = sqlContext.createDataFrame(datos05)
datos06_schema = sqlContext.createDataFrame(datos06)
datos07_schema = sqlContext.createDataFrame(datos07)
datos08_schema = sqlContext.createDataFrame(datos08)
datos09_schema = sqlContext.createDataFrame(datos09)
datos10_schema = sqlContext.createDataFrame(datos10)
datos11_schema = sqlContext.createDataFrame(datos11)
datos12_schema = sqlContext.createDataFrame(datos12)
datos13_schema = sqlContext.createDataFrame(datos13)
datos14_schema = sqlContext.createDataFrame(datos14)
datos15_schema = sqlContext.createDataFrame(datos15)
datos16_schema = sqlContext.createDataFrame(datos16)
datos17_schema = sqlContext.createDataFrame(datos17)
'''

schema_final
for l in range(year):
    if l == 0:
        schema_final = Schema[l]
    else:
        schema_aux = Schema[l]
        schema_final = schema_final.union(schema_aux)

# 2. Guardo tabla para ver que tira
schema_final.write.csv('tabla_final')
