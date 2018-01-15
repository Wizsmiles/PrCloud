from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import*
from pyspark.sql import*
from pyspark.sql import Row
import string
import sys

# Carga la estacion
station = sys.argv[1]

# 0. Configuracion inicial
conf = SparkConf().setMaster('local').setAppName('codigo')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

RDDvar = sc.textFile("tablaAVGAnyo")

# Mapeo de datos
station_lines = RDDvar.flatMap(lambda l: l.split("\n"))
aux = station_lines.map(lambda l: Row(idEstacion=l.split(",")[0],anyo=int(l.split(",")[3]),idParametro=int(l.split(",")[1])))

station_schema = sqlContext.createDataFrame(aux)
station_schema.registerTempTable("m")
query = "SELECT anyo, idParametro FROM m WHERE idEstacion = " + str(station)
table = sqlContext.sql(str(query))
table.orderBy("anyo").write.csv(station+"_parametros")
