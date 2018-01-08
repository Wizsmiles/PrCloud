from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import*
from pyspark.sql import*
from pyspark.sql import Row
import string

# Configuracion inicial
conf = SparkConf().setMaster('local').setAppName('codigo')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# Carga de ficheros
RDDDatos06 = sc.textFile("datos06.txt")

# 1. Mapeo de datos y crear dataFrame
datos06 = RDDDatos06.flatMap(lambda l: l.split("\n")).map(lambda l: Row(idEstacion=l[0:8],idParametro=l[8:10], idTecnica=l[10:12], anyo=l[14:16], mes=l[16:18],dia1=l[18:24], dia2=l[24:30], dia3=l[30:36], dia4=l[36:42], dia5=l[42:48],dia6=l[48:54], dia7=l[54:60], dia8=l[60:66], dia9=l[66:72], dia10=l[72:78],dia11=l[78:84], dia12=l[84:90], dia13=l[90:96], dia14=l[96:102], dia15=l[102:108],dia16=l[108:114], dia17=l[114:120], dia18=l[120:126], dia19=l[126:132], dia20=l[132:138],dia21=l[138:144], dia22=l[144:150], dia23=l[150:156], dia24=l[156:162], dia25=l[162:168],dia26=l[168:174], dia27=l[174:180], dia28=l[180:186], dia29=l[186:192], dia30=l[192:198],dia31=l[198:204]))

datos06_schema = sqlContext.createDataFrame(datos06)

# 2. Guardo tabla para ver que tira
datos06_schema.write.csv('tabla_06')
