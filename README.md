# TAREA3_SIS_DISTRIBUIDO
INTEGRANTES: Jairo Morales &amp; Javier Ahumada

## Descripción del sistema

En este proyecto, se implementó un buscador utilizando tecnologías de sistemas distribuidos, como Hadoop, MapReduce, y un índice invertido. Se recopilaron datos de 30 docs de Wikipedia, se procesaron utilizando Hadoop MapReduce para generar un índice invertido de frecuencia de palabras en los documentos. Además, se diseñó un buscador que utiliza este índice para recuperar y mostrar los 5 mejores resultados basados en coincidencias de palabras. Cabe mencionar que la estructura de este sistema fue obtenida del siguiente repositorio [Repositorio](https://github.com/Naikelin/map-reduce-hadoop) .

### Enlace del vídeo del funcionamiento del Sistema

[video](https://vimeo.com/888285545/d9176d6688?share=copy)

## ANTES DE DOCKER: Obteniendo 30 Docs con la API de Wikipedia

Antes de levantar el contenedor donde procesaremos los datos, hay que obtener estos. Esto se realiza pocisionandose en la carpeta examples/Wikipedia y ejecutando el script de python: obtenerwiki.py. 
Luego de finalizar la ejecución tendremos los 30 docs para procesarlos divididos en 2 carpetas: carpetaUno & carpetaDos.

Ahora pasemos a la parte de levantar el contendor y procesar los datos dentro de este.


## Levantar contenedor

Para crear la imagen usando el Dockerfile de este repositorio:
```sh
sudo docker build -t hadoop .
```
Para poder levantar el contenedor:
```sh
docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```
***Nota**: asegúrese que los puertos que está exponiendo se encuentran libres: **9864**, **9870**, **8088**, **9000***

## Entrar al contenedor
```sh
docker exec -it hadoop bash
```
## Copiar los 30 docs dentro del contenedor
Ya dentro de contendedor aplicamos los siquientes comandos para copiar los docs a la carpeta /tmp.
```sh
cp  /home/hduser/examples/Wikipedia/carpetaUno/* /tmp/
cp  /home/hduser/examples/Wikipedia/carpetaDos/* /tmp/
```
## Crear carpetas en el sistema de archivos de Hadoop

Hadoop posee su propio sistema de archivos distribuido: *HDFS*. 
Debemos crear algunas carpetas dentro del contenedor de Hadoop antes de levantar código en Hadoop:
```sh
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input	
```

## Crear carpetas para los txt de wikipedia dentro del contenedor hadoop
```sh
hdfs dfs -mkdir /user/hduser/input/Uno
hdfs dfs -mkdir /user/hduser/input/Dos
```
## Copiar archivos txt al HDFS
Nos posicionamos en donde están los 30 docs:
```sh
cd /tmp/
```
Copiamos los primeros 15 doc para posicionarlos en las carpeta de HDFS creada:
```sh
hdfs dfs -put Daddy_Yankee.txt Héctor_el_Father.txt J_Álvarez.txt Ñengo_Flow.txt Cosculluela.txt Julio_Voltio.txt Ñejo_y_Dálmata.txt Arcángel_y_De_la_Ghetto.txt Don_Omar.txt Tego_Calderón.txt a.txt b.txt c.txt d.txt e.txt input/Uno
```
Copiamos los segundo 15 doc para posicionarlos en las carpeta de HDFS creada:
```sh
hdfs dfs -put  f.txt g.txt h.txt i.txt j.txt 1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt input/Dos
```

## Encontrar path al archivo 'hadoop-streaming.jar' dentro de hadoop
```sh
find / -name 'hadoop-streaming*.jar'
```

## Ejecutar mapreduce para cada txt (10)
```sh
hadoop jar /home/hduser/hadoop-3.3.4/share/hadoop/tools/lib/hadoop-streaming-3.3.4.jar -file /home/hduser/mapper.py -mapper mapper.py -file /home/hduser/reducer.py -reducer reducer.py -input /user/hduser/input/Uno/a.txt -input /user/hduser/input/Uno/b.txt -input /user/hduser/input/Uno/c.txt -input /user/hduser/input/Uno/d.txt -input /user/hduser/input/Uno/f.txt -input /user/hduser/input/Dos/g.txt -input /user/hduser/input/Dos/h.txt -input /user/hduser/input/Dos/j.txt -input /user/hduser/input/Dos/k.txt -input /user/hduser/input/Dos/l.txt -output /user/hduser/output
```
## Copiar output (part-00000) desde HDFS al contenedor 
Se copia en carpeta donde esta el scrip que convertirá el output a JSON:
```sh
hdfs dfs -get /user/hduser/output/part-00000 /home/hduser/example/convertir_a_JSON
```

## Convertimos a JSON
```sh
 cd /home/hduser/example/convertir_a_JSON
python3 convertir_a_json.py
```

## Ejecutamos el buscador para realizar las consultas
```sh
cd ../buscador
python3 buscador.py
```
