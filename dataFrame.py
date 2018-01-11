from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import*
from pyspark.sql import*
from pyspark.sql import Row
import string

# Cambiar con el anyo
year = 17

# 0. Configuracion inicial
conf = SparkConf().setMaster('local').setAppName('codigo')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

def loadData(myFile):
    data = myFile.flatMap(lambda l: l.split("\n")).map(lambda l: Row(idEstacion=l[0:8],idParametro=l[8:10], idTecnica=l[10:12], anyo=l[14:16], mes=l[16:18],dia1=float(l[18:23]),dia2=float(l[24:29]),dia3=float(l[30:35]),dia4=float(l[36:41]),dia5=float(l[42:47]),dia6=float(l[48:53]),dia7=float(l[54:59]),dia8=float(l[60:65]),dia9=float(l[66:71]),dia10=float(l[72:77]),dia11=float(l[78:83]),dia12=float(l[84:89]),dia13=float(l[90:95]),dia14=float(l[96:101]),dia15=float(l[102:107]),dia16=float(l[108:113]),dia17=float(l[114:119]),dia18=float(l[120:125]),dia19=float(l[126:131]),dia20=float(l[132:137]),dia21=float(l[138:143]),dia22=float(l[144:149]),dia23=float(l[150:155]),dia24=float(l[156:161]),dia25=float(l[162:167]),dia26=float(l[168:173]),dia27=float(l[174:179]),dia28=float(l[180:185]),dia29=float(l[186:191]),dia30=float(l[192:197]),dia31=float(l[198:203])))
    return data

# 1. Cargo cada dataFrame asociado a un anyo

Schema = []
Schema_Average = []
for i in range(year):
    aux = ""
    aux2 = i+1
    if aux2 < 10:
        aux = "0" + str(aux2)
    else:
        aux = str(aux2)
<<<<<<< HEAD
    RDDs.append(sc.textFile("datos"+aux+".txt"))

# 1. Mapeo de datos y crear dataFrame

for j in range(year):
    Data.append(loadData(RDDs[j]))

for k in range(year):
    Schema.append(sqlContext.createDataFrame(Data[z]))

schema_final
=======
    Schema.append(sqlContext.createDataFrame(loadData(sc.textFile("datos"+aux+".txt"))))

# 2. Realizo la union de todos los dataFrames para obtener uno global
schema_final = None

>>>>>>> origin/master
for l in range(year):
    if l == 0:
        schema_final = Schema[l]
    else:
        schema_aux = Schema[l]
        schema_final = schema_final.union(schema_aux)

# 3. Guardo tabla para ver que tira
schema_final.write.csv('tabla_final')
