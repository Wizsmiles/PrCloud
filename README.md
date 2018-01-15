# Análisis de la calidad del aire en Madrid - Cloud y Big Data

![tierra](http://www.designerspics.com/wp-content/uploads/2014/05/globe_america_large_free_photo.jpg)

En esta página se aloja una práctica realizada para la asignatura Cloud y Big Data (CLO) de la Universidad Complutense. 

## Propósito del proyecto

Este proyecto trata de hacer accesibles y manejables datos sobre la calidad del aire en Madrid.

Nuestro objetivo es:

1. Tratar el DataSet obtenido para su futuro procesado.
2. Procesar los datos mediante técnicas de Big Data.
3. Generar gráficas en función de distintos parámetros.

## DataSet en profundidad

El DataSet que se ha utilizado, es facilitado por la [comunidad de Madrid](http://datos.madrid.es). Este DataSet a analizar contiene información sobre el aire (actualizada diariamente desde 2001 hasta la actualidad), generada por estaciones que están situadas en distintos puntos de Madrid.

El formato es el siguiente:

![DataSet1](https://raw.githubusercontent.com/Wizsmiles/PrCloud/master/resources/dataSet1.PNG)

- Estación: máquina física que toma las medidas.
- Magnitud: tipo de gas.
- Técnica: técnica que se ha usado para medir el gas.
- Dato diario: informa si es un dato horario o diario (es omitido en el procesado).
- Año: Año de la medición.
- Mes: Mes de la medición.
- Día 1 - Día 31: Datos obtenidos cada día. Todos los meses son considerados con 31 días.

## Descripción y uso de la aplicación

### Descripción:

1. La aplicación hace uso de un cluster Spark alojado en amazon AWS para recopilar los DataSet previamente explicados, y crear un DataFrame global. 

2. El DataFrame se desglosa en tres archivos principales: 
  *TablaFinal: Es la unión de todos los DataSet en una única tabla procesada con los datos de interés.
  *TablaAVG: Es la tabla que contiene la media de cada mes de los distintos valores.
  *TablaAVGAnyo: Contiene la media anual de los distintos valores.

3. Hay 3 scripts adicionales, cuyas funciones son: 
  *GraficaEstacion.py (Ejecución en local): A través de las directrices introducidas por el usuario, genera una gráfica acorde para una estación, un gas, un periodo de tiempo, y un formato dados.
  *Comparador.py (Ejecución en local): Compara las gráficas de dos estaciones introducidas por el usuario.
  *infoEstacion.py (Ejecución en amazon AWS con Spark): Obtiene los tipos de gases medidos por una estación a lo largo del tiempo.  

### Interpretación de las gráficas:

* Gráfica mensual:

![GraficaMensual](https://raw.githubusercontent.com/Wizsmiles/PrCloud/master/resources/GraficaMensual.png)

- Eje Y: valores del gas.
- Eje X: meses.

* Gráfica anual:

![GraficaAnual](https://raw.githubusercontent.com/Wizsmiles/PrCloud/master/resources/GraficaAnual.png)

- Eje Y: valores del gas.
- Eje X: años.

* Comparativa gráficas:

![ComparativaGraficas](https://raw.githubusercontent.com/Wizsmiles/PrCloud/master/resources/comparativa.png)

- Eje Y: valores del gas. 
- Eje X: meses o años. 
- Color1: datos para la estación 1.
- Color2: datos para la estación 2.

### Uso de la aplicación:

**Recomendación:** Para usar la aplicación, lo más recomendable es descargar el repositorio con los datos ya formateados. 

1. En caso de que se quiera realizar el proceso desde cero:

1.1. Descargar DataSet y crear cluster Spark en amazon AWS.
1.2. Usar los scripts auxiliares QuitaCeros.py y QuitaCaracteres.py. El proceso se repite tantas veces como años se quieran procesar. Ejemplo (XX se sustituye por el año a procesar):

```
 python QuitaCeros.py datosXX.txt.
```

1.3. Cargar el número de años a estudiar en Spark (XX se sustituye por el año a procesar). El proceso se repite tantas veces como años se quiera cargar:

```
 hadoop fs -put datosXX.txt
```

1.4. Crear el dataframe (X se sustituye por el número de años a procesar):

```
spark-submit dataFrame.py X
```

1.5. Generar los archivos TablaFinal, TablaAVG y TablaAVGAnyo:

```
hadoop fs -get tabla_final
hadoop fs -get tabla_avg
hadoop fs -get tabla_avg_anyo
```

Genera carpetas con los archivos que componen las tablas fragmentados.

```
cat tabla_final/* > TablaFinal
cat tabla_avg/* > TablaAVG
cat tabla_avg_anyo > TablaAVGAnyo
```
**Es importante que los ficheros finales se tengan el nombre indicado, ya que es el que reconocen los posteriores scripts.**


2. En caso de seguir la recomendación o haber realizado el punto 1 completo:

2.1. Generar gráficas de una única estación:

El script usado es **GraficaEstacion.py**.

```
python GraficaEstacion.py idEstacion idParámetro intervalo (año) tipoGrafica
```

- idEstacion: id de la estación de la que se quieren obtener los datos.
- idParámetro: id que representa el gas medido.
- intervalo: "m" para los meses de un año dado. "a" para mostrar todos los años desde 2001 hasta la actualidad.
- año (opcional): en caso de haber elegido "m" en el anterior argumento, se debe especificar el año a medir.
- tipoGrafica (opcional): "plot" gráfica de puntos unida por líneas (predeterminada), "bar" gráfica de barras. 

**Ejemplo mensual:**

```
python GraficaEstacion.py 28079056 6 m 17 bar
```

**Ejemplo anual:**

```
python GraficaEstacion.py 28079056 6 a plot
```

**Importante: Si en el intervalo seleccionado no hay datos, las gráficas saldrán vacías.**

2.2. Generar gráficas comparativas:

El script usado es **Comparador.py**

```
python Comparador.py idEstacion1 idEstacion2 idParametro intervalo (año)
```

- idEstacion1: id de la primera estación a comparar.
- idEstacion2: id de la segunda estación a comparar.
- idParametro: id que representa el gas medido.
- intervalo: "m" para los meses de un año dado. "a" para mostrar todos los años desde 2001 hasta la actualidad.
- año (opcional): en caso de haber elegido "m" en el anterior argumento, se debe especificar el año a medir.

**Ejemplo: **

```
python Comparador.py 28079056 28079056 6 a 
```

**Importante: Si en el intervalo seleccionado no hay datos, las gráficas saldrán vacías.**

2.3. (Opcional) Consultar gases disponibles para una estación:

El script usado es **infoEstacion.py**. Es necesario usarlo en un cluster Spark de amazon AWS y haber cargado TablaAVG (punto 1.5.)

```
spark-submit infoEstacion.py idEstacion
```
- idEstacion: id de la estación de la que se quieren consultar los gases.

Genera un archivo llamado idEstacion_parametros, en el que se detallan los gases medidos por periodo.

**Ejemplo:**

```
spark-submit infoEstacion.py 28079056
```

## Datos interesantes aprendidos en el desarrollo de la aplicación

## Mejoras posibles para la aplicación

## Conclusiones del desarrollo de la aplicación

