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

- --s [width,height]: Tamaño de la ventana
- --l: Modo ligero, esto en caso de necesitar tamaños muy grandes y procesamientos muy pesados
- --d [x,y]: Tamaño la cuadrícula donde se mostrarán las figuras


## Como usar

El programa es interactivo con el usuario, por lo que, para dibujar es necesario que des uno cuantos clicks para que funcione. 

En la pantalla se pueden observar 2 partes. La primera, está ubicada en la parte izquierda de la ventana, es una malla que
finge ser un monitor y cada cuadro corresponde a un pixel de este. El lado derecho se mostrarán las últimas 10 figuras que
hayas pintado, da click encima de las que has creado para recalcar donde se encuentra dicha figura.

**(Siempre que termines de dibujar una figura presiona r, esto debido a un bug que en un futuro se resolverá)**

**Puntos**

Para dibujar un punto solo da click izquierdo (L\_Click) en cualquiera de los pixeles. Para quitar un pixel encendido vuelve 
a presionar encima del mismo pixel.

**Linea** 

Para dibujar lineas es necesario tener dos puntos, presiona la tecla _l_ (L minus). (En caso de que no se muestre es o, por que tienes más de dos puntos cargados
en la memoria en cuyo caso presiona _r_ y vuelve a seleccionar otros dos prixeles y si esto no funciona presiona la tecla _esc_. Esto se debe a un bug
que en un futuro se arreglará)

**Triangulo**

El triangulo requiere tres puntos, presiona la tecla _t_. (En caso de que no se muestre es o, por que tienes más de tres puntos cargados en la memoria 
en cuyo caso presiona _r_ y vuelve a seleccionar otros dos prixeles y si esto no funciona presiona la tecla _esc_. Esto se debe a un bug que en un 
futuro se arreglará)

**Borrar**

Para borrar un pixel encendido solo da click izquierdo encima del pixel.

Para borrar una figura presiona _supr_ (Suprimir) y da click izquierdo sobre el nombre de la figura que quieras borrar que se muestra en el panel de la derecha.
