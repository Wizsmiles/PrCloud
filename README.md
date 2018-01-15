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

**Descripción:**

1. La aplicación hace uso de un cluster Spark alojado en amazon AWS para recopilar los DataSet previamente explicados, y crear un DataFrame global. 

2. El DataFrame se desglosa en tres archivos principales: 
  *TablaFinal: Es la unión de todos los DataSet en una única tabla procesada con los datos de interés.
  *TablaAVG: Es la tabla que contiene la media de cada mes de los distintos valores.
  *TablaAVGAnyo: Contiene la media anual de los distintos valores.

3. Hay 3 scripts adicionales, cuyas funciones son: 
  *GraficaEstacion.py (Ejecución en local): A través de las directrices introducidas por el usuario, genera una gráfica acorde para una estación, un gas, un periodo de tiempo, y un formato dados.
  *Comparador.py (Ejecución en local): Compara las gráficas de dos estaciones introducidas por el usuario.
  *InfoEstacion.py (Ejecución en amazon AWS con Spark): Obtiene los tipos de gases medidos por una estación a lo largo del tiempo.  

**Interpretación de las gráficas:**

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

## Datos interesantes aprendidos en el desarrollo de la aplicación

## Mejoras posibles para la aplicación

## Conclusiones del desarrollo de la aplicación

