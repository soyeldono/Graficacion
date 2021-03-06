# Trazado de Lineas

Programa para dibujar en la pantalla lineas y triangulos.


## Instalacion

1. Instala los requirimientos:
- python >= 3.7
 - pywin32==300
 - pygame==2.0.1
 - win32gui==221. 6
2.  Clona el repositorio
```
git clone https://github.com/soyeldono/Graficacion.git
``` 

## Ejecución
```
python main.py [--s|--l|--d]
``` 

## Flags

- --s (width,height): Tamaño de la ventana. Ej "python main.py --s=(500,500)", creará una ventana de 500x500
- --l: Modo ligero, esto en caso de necesitar tamaños muy grandes y procesamientos muy pesados. Ej "python main.py --l=True"
- --d (x,y): Tamaño la cuadrícula donde se mostrarán las figuras. Ej "python main.py --s=(50,50)", creará una cuadrícula de 50x50


## Como usar

El programa es interactivo con el usuario, por lo que, para dibujar es necesario que des uno cuantos clicks para que funcione. 

En la pantalla se pueden observar 2 partes. La primera, está ubicada en la parte izquierda de la ventana, es una malla que
finge ser un monitor y cada cuadro corresponde a un pixel de este. El lado derecho se mostrarán las últimas 10 figuras que
hayas pintado, da click encima de las que has creado para recalcar donde se encuentra dicha figura.

**Puntos**

**IMPORTANTE** el programa recordará todos los pixeles que hayas dado click, ya que con estos calculará y dibujará las figuras
pero NO recordará los pixeles que se enciendan por crear un figura como por ejemplo un triangulo. Para dibujar un punto solo 
da click izquierdo (L\_Click) en cualquiera de los pixeles. Para quitar un pixel encendido vuelve 
a presionar encima del mismo pixel.

![Puntos](https://user-images.githubusercontent.com/38016639/156116219-066757a1-7dfb-4f31-a408-ed4d96c5e602.gif)

**Linea** 

Para dibujar lineas es necesario tener dos puntos, presiona la tecla _l_ (L minus). (En caso de que no se muestre es o, por que 
tienes más de dos puntos cargados en la memoria en cuyo caso presiona _r_ y vuelve a seleccionar otros dos prixeles y si esto no 
funciona presiona la tecla _esc_. Esto se debe a un bug que en un futuro se arreglará)

![Linea](https://user-images.githubusercontent.com/38016639/156116253-d2368f47-f8b6-4d47-bfb6-3dd24fcbc0c7.gif)

**Triangulo**

El triangulo requiere tres puntos, presiona la tecla _t_. (En caso de que no se muestre es o, por que tienes más de tres puntos cargados en la memoria 
en cuyo caso presiona _r_ y vuelve a seleccionar otros dos prixeles y si esto no funciona presiona la tecla _esc_. Esto se debe a un bug que en un 
futuro se arreglará)

![Triangulo](https://user-images.githubusercontent.com/38016639/156116300-38d5e16b-cb20-4b06-8cbc-10c573e2e0ca.gif)

**Borrar**

Para borrar un pixel encendido solo da click izquierdo encima del pixel.

Para borrar una figura presiona _supr_ (Suprimir) y da click izquierdo sobre el nombre de la figura que quieras borrar que se muestra en el panel de la derecha.
Una vez termines de borrar vuelve a presionar _supr_ para desactivar la funcion de borrar al dar click.

![Borrar](https://user-images.githubusercontent.com/38016639/156116347-447ae6ac-2e9b-4bd9-8c6b-c363f4c5b72c.gif)

**Limpiar**

Limpiar/Reiniciar es eliminar TODO lo que tienes en la pantalla. Presiona la tecla _esc_ (Escape).

![Limpiar](https://user-images.githubusercontent.com/38016639/156116370-27775beb-2f72-411c-a6ec-0cd3952ce2e3.gif)
