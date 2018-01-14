from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import*
from pyspark.sql import*
from pyspark.sql import Row
import string
import sys

# Carga el numero de anyos
year = int(sys.argv[1])

# 0. Configuracion inicial
conf = SparkConf().setMaster('local').setAppName('codigo')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

def loadData(myFile):
    data = myFile.flatMap(lambda l: l.split("\n")).map(lambda l: Row(idEstacion=l[0:8],idParametro=l[8:10], idTecnica=l[10:12], anyo=l[14:16], mes=l[16:18],dia1=float(l[18:23]),dia2=float(l[24:29]),dia3=float(l[30:35]),dia4=float(l[36:41]),dia5=float(l[42:47]),dia6=float(l[48:53]),dia7=float(l[54:59]),dia8=float(l[60:65]),dia9=float(l[66:71]),dia10=float(l[72:77]),dia11=float(l[78:83]),dia12=float(l[84:89]),dia13=float(l[90:95]),dia14=float(l[96:101]),dia15=float(l[102:107]),dia16=float(l[108:113]),dia17=float(l[114:119]),dia18=float(l[120:125]),dia19=float(l[126:131]),dia20=float(l[132:137]),dia21=float(l[138:143]),dia22=float(l[144:149]),dia23=float(l[150:155]),dia24=float(l[156:161]),dia25=float(l[162:167]),dia26=float(l[168:173]),dia27=float(l[174:179]),dia28=float(l[180:185]),dia29=float(l[186:191]),dia30=float(l[192:197]),dia31=float(l[198:203])))
    return data

def loadAVG(myFile):
    data = myFile.flatMap(lambda l: l.split("\n")).map(lambda l: Row(idEstacion=l[0:8],idParametro=l[8:10], idTecnica=l[10:12], anyo=l[14:16], mes=l[16:18],avg=((float(l[18:23])+float(l[24:29])+float(l[30:35])+float(l[36:41])+float(l[42:47])+float(l[48:53])+float(l[54:59])+float(l[60:65])+float(l[66:71])+float(l[72:77])+float(l[78:83])+float(l[84:89])+float(l[90:95])+float(l[96:101])+float(l[102:107])+float(l[108:113])+float(l[114:119])+float(l[120:125])+float(l[126:131])+float(l[132:137])+float(l[138:143])+float(l[144:149])+float(l[150:155])+float(l[156:161])+float(l[162:167])+float(l[168:173])+float(l[174:179])+float(l[180:185])+float(l[186:191])+float(l[192:197])+float(l[198:203]))/31)))
    return data

# 1. Cargo cada dataFrame asociado a un anyo
Schema = []
Schema_avg = []
for i in range(year):
    aux = ""
    aux2 = i+1
    if aux2 < 10:
        aux = "0" + str(aux2)
    else:
        aux = str(aux2)
    Schema.append(sqlContext.createDataFrame(loadData(sc.textFile("datos"+aux+".txt"))))
    Schema_avg.append(sqlContext.createDataFrame(loadAVG(sc.textFile("datos"+aux+".txt"))))

# 2. Realizo la union de todos los dataFrames para obtener uno global
schema_final = None
schema_avg_final = None
for l in range(year):
    if l == 0:
        schema_final = Schema[l]
        schema_avg_final = Schema_avg[l]
    else:
        schema_aux = Schema[l]
        schema_avg_aux = Schema_avg[l]
        schema_final = schema_final.union(schema_aux)
        schema_avg_final = schema_avg_final.union(schema_avg_aux)

schema_final.registerTempTable("tabla")
query = "SELECT idEstacion,idParametro,idTecnica,anyo,mes,dia1,dia2,dia3,dia4,dia5,dia6,dia7,dia8,dia9,dia10,dia11,dia12,dia13,dia14,dia15,dia16,dia17,dia18,dia19,dia20,dia21,dia22,dia23,dia24,dia25,dia26,dia27,dia28,dia29,dia30,dia31 FROM tabla"
table = sqlContext.sql(str(query))
#Transformamos todas las medidas a 10^-6 gr 
query_medida = "UPDATE tabla SET dia1=dia1*1000, dia2=dia2*1000, dia3=dia3*1000, dia4=dia4*1000, dia5=dia5*1000, dia6=dia6*1000, dia7=dia7*1000, dia8=dia8*1000, dia9=dia9*1000, dia10=dia10*1000, dia11=dia11*1000, dia12=dia12*1000, dia13=dia13*1000, dia14=dia14*1000, dia15=dia15*1000, dia16=dia16*1000, dia17=dia17*1000, dia18=dia18*1000, dia19=dia19*1000, dia20=dia20*1000, dia21=dia21*1000, dia22=dia22*1000, dia23=dia23*1000, dia24=dia24*1000, dia25=dia25*1000, dia26=dia26*1000, dia27=dia27*1000, dia28=dia28*1000, dia29=dia29*1000, dia30=dia30*1000, dia31=dia31*1000 WHERE idParametro IN (6,42,43,44)"
table = sqlContext.sql(str(query_medida))

schema_avg_final.registerTempTable("tabla2")
query = "SELECT idEstacion,idParametro,idTecnica,anyo,mes,avg FROM tabla2"
table2 = sqlContext.sql(str(query))
#Transformamos todas las medidas a 10^-6 gr
query_medida = "UPDATE tabla2 SET avg = avg*1000 WHERE idParametro IN (6,42,43,44)"
table2 = sqlContext.sql(str(query_medida))
# 3. Guardo tabla para ver que tira
table.orderBy("anyo").write.csv('tabla_final')
table2.orderBy("anyo").write.csv('tabla_avg')
