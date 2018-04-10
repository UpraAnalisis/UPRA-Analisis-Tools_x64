# UPRA Análisis Tools x64

<p align="center">
  <img src="/Images/Logo_Upra_Analisis_Tools.png">
</p>


Es una funcionalidad del tipo Add-in (o extensión) que se incorpora a ArcGIS y permite realizar diversas operaciones orientadas a agilizar el proceso de generación de resultados de los geoprocesos adelantados por los profesionales del grupo de análisis, para dar cumplimiento al objeto misional de la [UPRA]. Estas herrramientas se dividen en dos grandes grupos:
### Herramientas para presentaciones
Herramientas que preparan de forma másiva los insumos para construir presentaciones con la información resultante de los geoprocesos.
### Herramientas para manipular layers
Herramientas que permiten consultar, filtrar y exportar de forma masiva las capas y tablas cargadas en un mxd.

## Requisitos de instalación


Antes de instalar el Add-in Upra_Analisis_Tools_x64 verifique lo siguiente:

+ Que tenga permisos de escritura sobre la carpeta de Python en su pc. Para habilitar los permisos de escritura diríjase a la unidad C: de su pc,  haga clic derecho sobre la carpeta Python27 y seleccione propiedades. Una ventana como la mostrada a continuación aparecerá. Cerciórese de que el botón de solo lectura este deseleccionado.

<p align="center">
  <img src="Images\Carpeta_python.png">
</p>

 + Que tenga instalada la extensión de Geoprocesamiento en segundo plano (64 bits), Background Geoprocessing (64-bit). Para verificar diríjase a la siguiente ruta: C:\Python27 compruebe que en la carpeta de Python de su equipo existen dos carpetas similares a las mostradas en la siguiente imagen.

<p align="center">
  <img src="Images\ruta_python.png">
</p>


+ En caso de existir la carpeta que comienza por `ArcGISx64`, usted tendrá instalado el Geoprocesamiento en segundo plano (64 bits), en caso contrario comuníquese con el administrador para realizar la respectiva instalación.

## Instalación

El proceso de descarga e instalación es el siguiente:

### Descargar del AddIn:

Para descargar el Add-in haga clic en el link de `Download ZIP` tal como lo muestra la siguiente imagen.

![descarga](Images/Descarga.png)

la instalación puede realizarse de dos formas :
Manual y automatizada.

### Instalación manual

La forma manual consiste en copiar los archivos: `clipx64_aux.py`, `fillable_box.py`, `identityx64_aux.py` y `UPRA-Analisis-Tools_x64.esriaddin` en el directorio de Add-ins de arcgis tal y como se muestra en la siguiente imagen.

<p align="center">
  <img src="Images\Copia_manual.png">
</p>

En el paso anterior se copiaron los archivos necesarios que componen el Add-in, sin embargo, es necesario instalar librerias de python auxiliares para su correcto funcionamiento. Para llevar a cabo esta tarea se deben ejecutar los archivos `get-pip.py`e `instalador_auxiliar.py`, en el respectivo orden empleando la versión de Python de 32 bits.

Para realizar la ejecución a 32 bits copie la ruta del ejecutable de 32 bits de Python de ArcGis en un bloc de notas seguido de un espacio, luego escriba la ruta del archivo `get-pip.py`, tal como lo indica la imagen.

<p align="center">
  <img src="Images\ejecucion_getpip.png">
</p>

Posteriormente, copie el texto del bloc de notas, presione las teclas `Windows` `+` `E` y pegue el texto en la ventana de ejecución de la siguiente forma.


<p align="center">
  <img src="Images\ejecutar_get_pip.png">
</p>


Para ejecutar el archivo de  `instalador_auxiliar.py` repita el procedimiento anterior.

 AL finalizar la ejecución del archivo de instalador_auxiliar deberá aparecer un ventana como la mostrada a continuación, inidicando que el proceso ha finalizado con exito.

<p align="center">
  <img src="Images\auxiliar.png">
</p>

### Instalación automatizada

La forma automatizada consiste en ejecutar el instalador que viene por defecto en el Add-in. Para ello se debe ejecutar el archivo `Instalador_UPRA-Analisis-Tools_x64.py`.

<p align="center">
  <img src="Images\ejecutable.png">
</p>

 Al hacerlo una serie de ventanas aparecerán instalando las librerías de Python necesarias y copiando los archivos del Add-in en su directorio local de ArcGis, al finalizar la instalación, se mostrará la siguiente imagen:

  <p align="center">
   <img src="Images\Ventana_Ejecucion.png">
 </p>



## Configuración

Si al iniciar ArcMap no encuentra el Add-In debe configurar su visualización dentro de la barra de herramientas. Para ello, haga clic derecho sobre la barra de herramientas y seleccione la opción customize. Al hacerlo se mostrará el menú mostrado en la siguiente imágen en donde debe seleccionar la barra de herramientas Upra_Análisis_Tools.

![Dataframes](/img/activar_menu.png)

## Uso
### Configurar el mxd
1. Construir tres dataframes con la estructura mostrada en la siguiente imágen:

![Dataframes](/img/dataframes.PNG)

Recuerde mantener pausada la visualización para mejorar el rendimiento y la estabiidad del addin.

### Cargar Capas Necesarias

1. Las capas necesarias para la operación de este addin son de dos (2) tipos y deben estar separadas en diferentes dataframes de la siguiente forma:

moldes: Este dataframe contiene las capas con las cuales se realizarán los cortes.

capas: Este dataframe contiene las capas que serán cortadas y sobre las cuales se realizarán las estadísticas.

2. Si se desea obetener estadísticas a partir de las capas, deben configurarse para cada capa los campos sobre los cuales se van a procesar. Para ello se escribirán dos guiones al final del nombre de cada capa, seguidos del nombre del campo con el cual se van a hacer las estadísticas. A continuación una imagen que representa lo anteriormente mencionado.

![Dataframes](/img/confi_nombres.png)

### Procesar los Cortes Multiples

1. Lo primero que hay que seleccionar es la ruta del folder donde se almacenarán los datos del proceso.



### Selección criterio

1. Contruir tres dataframes con la estrutura mostrada en la siguiente imágen:

![Select Herramienta](/img/selherr.PNG)

2. Dar Click en el punto de interés que se desea consultar

    ![Dataframes](/img/dataframes.PNG)

### Selección Variables

Una vez realizado el proceso anterior el Add-In consulta en la gdb con las variables aquellas que corresponden a el criterio de interés, luego de eso carga los nombre en el menú desplegable y estan listas para ser adicionadas a la visualización del mapa.

1. Seleccione variable a cargar en el en el menú desplegable

    ![Select Variable](/img/seleccvar.png)

2. Mensaje advierte que la variable se está cargando, pulse OK

    ![Cargar Variable](/img/carvar.PNG)

### Generación Reporte

1. Se carga la variable y mensaje Advierte si quiere generar reporte. (Reporte es Opcional)

    ![Generar Report](/img/genrep.PNG)

2. Si decide generar reporte seleccione donde lo desea guardar.

    ![Salvar Report](/img/savrep.PNG)

3. De no generar reporte los datos quedan en un layer temporal llamado data y ahí los puede consultar.

    ![Capa Cargada](/img/capcar.PNG)

4. El reporte aparece en excel de la siguiente forma:

    ![report](/img/rep.PNG)
