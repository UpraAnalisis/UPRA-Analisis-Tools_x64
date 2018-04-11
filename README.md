# UPRA Análisis Tools x64

<p align="center">
  <img src="/Images/Logo_Upra_Analisis_Tools.png">
</p>


Es una funcionalidad del tipo Add-in (o extensión) que se incorpora a ArcGIS y permite realizar diversas operaciones orientadas a agilizar el proceso de generación de resultados de los geoprocesos adelantados por los profesionales del grupo de análisis, para dar cumplimiento al objeto misional de la [UPRA].

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

<p align="center">
  <img src="Images\Descarga.PNG">
</p>

La instalación puede realizarse de dos formas:
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
AL finalizar la ejecución del archivo de instalador_auxiliar deberá aparecer una ventana como la mostrada a continuación, indicando que el proceso ha finalizado con éxito.

<p align="center">
  <img src="Images\auxiliar.png">
</p>

### Instalación automatizada

La forma automatizada consiste en ejecutar el instalador que viene por defecto en el Add-in. Para ello se debe ejecutar el archivo `Instalador_UPRA-Analisis-Tools_x64.py`.

<p align="center">
  <img src="Images\ejecutable.png">
</p>

 Al hacerlo una serie de ventanas aparecerán instalando las librerías de Python necesarias y copiando los archivos del Add-in en su directorio local de ArcGis, al finalizar la instalación, se mostrará la siguiente imagen.

  <p align="center">
   <img src="Images\Ventana_Ejecucion.png">
 </p>

### Configuración

 Si al iniciar ArcMap no encuentra el Add-In, debe configurar su visualización dentro de la barra de herramientas. Para ello, haga clic derecho sobre la barra de herramientas y seleccione la opción `customize`. Al hacerlo se activará el menú mostrado en la siguiente imagen en donde se debe seleccionar la barra de herramientas Upra_Análisis_Tools.

<p align="center">
 <img src="/img/activar_menu.png">
</p>

## Uso

La barra de herramientas del Add-in Upra Análisis Tools x64 se compone de dos grupos de funcionalidades: `Herramientas para presentaciones` y `Herramientas para manipular layers`.

<p align="center">
 <img src="Images\barra_de_herramientas.png">
</p>

### Herramientas para presentaciones
Herramientas que preparan de forma masiva los insumos para construir presentaciones con la información resultante de los geoprocesos.

#### Multicortes


<p align="center">
 <img style width="40%" src="Images\logo_multicortes.gif" >
</p>

La funcionalidad de Multicortes permite realizar el corte y las estadísticas de un conjunto de capas teniendo en cuenta unos moldes definidos.

##### ¿Como funciona?
<p></p>
<p align="center">
 <img style src="Images\descripcion_multicortes.png" >
<p></p>
<p align="center">
 <img style src="Images\molde1.png" >
<p></p>
<p align="center">
 <img style src="Images\molde2.png" >
<p></p>

##### Configurar el mxd
Para emplear esta funcionalidad es necesario crear tres dataframes, dos deben llevar de forma obligatoria los nombres : `moldes` y `capas` respectivamente y el tercero puede tener cualquier nombre. A continuación una imagen que ilustra lo descrito.

<p align="center">
 <img src="/img/dataframes.PNG">
</p>

Tenga en cuenta:

Mantenga abierta la consola de python para visualizar los mensajes de error que se muestren en la ejecución de la herramienta.

<p align="center">
 <img src="Images\icono_consola_python.png">
</p>

Recuerde mantener pausada la visualización para mejorar el rendimiento y la estabiidad del addin.

<p align="center">
 <img src="Images\pausar_dibujado.png">
</p>

##### Cargar Capas Necesarias

Las capas necesarias para la operación de este addin son de dos (2) tipos y deben estar separadas en diferentes dataframes de la siguiente forma:

`moldes`: Este dataframe contiene las capas con las cuales se realizarán los cortes.

`capas`: Este dataframe contiene las capas que serán cortadas y sobre las cuales se realizarán las estadísticas.

Si se desea obtener estadísticas a partir de las capas, deben configurarse para cada capa los campos sobre los cuales se van a procesar. Para ello se escribirán dos guiones al final del nombre de cada capa, seguidos del nombre del campo con el cual se van a hacer las estadísticas. `En caso de que muchas capas tengan el mismo nombre de campo, este no debe escribir en el mxd si no, que cuando se vaya a realizar el corte se escribirá como campo opcional`. A continuación una imagen que representa lo anteriormente mencionado.


<p align="center">
 <img src="/img/confi_nombres.png">
</p>



Tal y como se describe la capa `Z_PINA_GENERAL_FINAL_25ha` no tiene asociado ningún campo de estadísticas y esto se debe a que este será suministrado cuando las ventanas emergentes lo soliciten.

<p align="center">
 <img src="Images\campo_estadisticas.png">
</p>

`Tenga en cuenta`:
Al finalizar la configuración de los campos de estadísticas y las capas, es necesario que el usuario active el tercer dataframe donde se alaojaran los resultados.

El mxd totalmente configurado y dispuesto para su ejecución debe lucir de la siguiente forma:

<p align="center">
 <img src="Images\mxd_configurado.png">
</p>


##### Realizar los cortes

Una vez se construyan los dataframes y se adicionen las capas necesarias con su respectivo campo de estadísticas se procederá a realizar el corte. Para hacerlo haga clic sobre el ícono de multicortes localizado en la barra de herramientas en el menú de presentaciones.

Al hacer clic aparecerá un ventana preguntando la ruta de salida de los resultados. Tal y como se muestra en la siguiente imagen.

<p align="center">
 <img src="Images\ruta_de_salida.png">
</p>

Seleccione la carpeta y haga clic en `add`. Una vez seleccionada la ruta de salida aparecerá el menú prinicpal de la herramienta.

<p align="center">
 <img src="Images\tipo_analisis.png">
</p>

Si se selecciona la opción nada, la herraminienta finaliza la ejecución y muestra un mensaje de despedida.

<p align="center">
 <img src="Images\ventana_salida.png">
</p>

###### Corte y estadísticas

Si se selecciona esta opción automaticamente se despliega una nueva ventana preguntando que tipo de operación de corte se efectuará.

<p align="center">
 <img src="Images\tipo_de_corte.png">
</p>

Al seleccionar la operación de corte, aparecerá la ventana solicitando el campo opcional que será usado para hacer las estadísticas sobre las capas que no tengan definido el campo de estadísticas en el mxd.


<p align="center">
 <img src="Images\campo_estadisticas.png">
</p>

Por último, aparecerá una ventana preguntando si el usuario desea continuar con la ejecución. En caso de ser afirmativo la ejecución continua, en caso contrario, aparece el mensaje de despedida antes mostrado.

Al continuar la ejecución una ventana aparece mostrando una animación de procesamiento. Le recomendamos al usuario que tenga paciencia con la ejecución del proceso. Dependiendo de la complejidad y número de capas involocradas el proceso puede demorarse. la ventana de ArcMap quedará inactiva hasta que finalice todos los cortes.  

<p align="center">
 <img src="Images\ventana_proceso.png">
</p>

Una vez finalizado el proceso, los resultados de las capas de corte se cargarán en el dataframe de resultados tal y como se aprecia en la siguientes imagenes.

<p align="center">
 <img src="Images\resultados_corte.png">
</p>

<p align="center">
 <img src="Images\resultados_corte1.png">
</p>

Tal y como lo muestra la última imagen, las capas cortadas apareceran cargadas con el nombre de la capa seguidas de un de una caracter de raya al piso y el nombre del molde. Este nombre es solo el nombre del layer, en la geodatabase de salida los cortes conservan el nombre original de la capa.

A continuación se detallan los resultados









### Herramientas para manipular layers
Herramientas que permiten consultar, filtrar y exportar de forma masiva las capas y tablas cargadas en un mxd.





1. Construir tres dataframes con la estructura mostrada en la siguiente imágen:





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
