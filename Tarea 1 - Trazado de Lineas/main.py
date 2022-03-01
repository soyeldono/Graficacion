import pygame as pg
from pygame.locals import *
from sklearn.linear_model import PassiveAggressiveClassifier
from sympy import arg
from win32api import GetSystemMetrics
import Objects
from Objects.line import Line
from Objects.triangle import Triangle
from screen import *
import sys
import time
from copy import copy
import random as rd
import logging
import argparse

W = GetSystemMetrics(0) - 500
H = GetSystemMetrics(1) - 400

x,y = (20,20)
esc_x = 0.7
esc_y = 1

parser = argparse.ArgumentParser()

parser.add_argument('--s',type=str,default=(W,H),help="Tamaño de la pantalla")
parser.add_argument('--l',type=bool,default=False,help="Inicio en modo ligero para ahorrar recursos de la pc a cambio de ser un poco mas lento")
parser.add_argument('--d',type=str,default=(x,y),help="Tamaño de la maya de los pixeles")
args = parser.parse_args()

W = int(args.s.split(',')[0][1:]) if isinstance(args.s,str) else args.s[0]
H = int(args.s.split(',')[1][:-1]) if isinstance(args.s,str) else args.s[1]

_light = args.l

x = int(args.d.split(',')[0][1:]) if isinstance(args.d,str) else args.d[0]
y = int(args.d.split(',')[1][:-1]) if isinstance(args.d,str) else args.d[1]

G = Grid((W,H),(x,y),(esc_x,esc_y),light=_light)
P = Panel([],W*0.75,H*0.1,W*0.20,H*0.8)

pg.init()
screen = pg.display.set_mode((W,H))
pg.display.set_caption('DDA')

POINTS = []
TO_DRAW = []
FIGURES = []
MARK = []
ADDED = []

FOCUS = None
DEL = False

print(W,H)

logging.basicConfig(filename="Graficacion.log",format='%(asctime)s %(message)s',filemode="w")
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info(f"Se ha iniciado el programa. Tamanho de la ventana:({W},{H})")

while True:
    screen.fill((0,0,0))

    # ------------ DIBUJAR LOS BOTONES
    pg.draw.rect(screen,(255,255,255),pg.Rect(0,0,int(W*esc_x),int(H*esc_y)))

    if x*y <= 10000: #si las dimensiones de la pantalla son tan grandes, las lineas no se van a ver por lo que no tiene sentido dibujarlas
        for Y in range(y):
            for X in range(x):
                pg.draw.line(screen,(0,0,0),(X*W*esc_x/x,0),(X*W*esc_x/x,H),2)
                pg.draw.line(screen,(0,0,0),(0,Y*H*esc_y/y),(W,Y*H*esc_y/y),2)

    # ------------ LA LISTA DE LAS FIGURAS
    P.draw(screen)

    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            logger.info("Se termino de ejecutar el programa")
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_l:
                try:
                    if 1 < len(POINTS) < 3:
                        L = Line(POINTS[0],POINTS[1])
                        L.calculate()
                        P.add_object(L)
                        for j in L.points:
                            if abs(j[1]-y)*x+j[0] not in TO_DRAW:
                                TO_DRAW.append(abs(j[1]-y)*x+j[0])
                                if G.light and abs(j[1]-y)*x+j[0] not in G.grid:
                                    G.add_pixel(j[0],abs(j[1]-y)*x)
                                G.grid[abs(j[1]-y)*x+j[0]].click()
                        logger.info(f"Se ha creado la linea del Punto 1:{POINTS[0]} al Punto 2:{POINTS[1]}")
                        POINTS = []
                        del L
                    else:
                        logger.info(f"Hay {len(POINTS)} puntos en el tablero, cuando solo debe de haber 2")
                except Exception as e:
                    logger.exception(e)

            elif event.key == pg.K_t:
                try:
                    if 2 < len(POINTS) < 4:
                        T = Triangle(POINTS[0],POINTS[1],POINTS[2])
                        T.calculate()
                        P.add_object(T)
                        for j in T.points:
                            if abs(j[1]-y)*x+j[0] not in TO_DRAW:
                                TO_DRAW.append(abs(j[1]-y)*x+j[0])
                                if G.light and abs(j[1]-y)*x+j[0] not in G.grid:
                                    G.add_pixel(j[0],abs(j[1]-y)*x)
                                G.grid[abs(j[1]-y)*x+j[0]].click()
                        logger.info(f"Se ha creado el triangulo Punto 1:{POINTS[0]}, Punto 2:{POINTS[1]}, Punto 3:{POINTS[2]}")
                        POINTS = []
                        del T
                except Exception as e:
                    logger.exception(e)
            
            elif event.key == pg.K_DELETE:
                DEL = not DEL
            
            elif event.key == pg.K_r:
                POINTS = []

            elif event.key == pg.K_ESCAPE:
                for i in TO_DRAW:
                    G.grid[i].state = False
                POINTS = []
                TO_DRAW = []
                FIGURES = []
                MARK = []
                P.list_buttons = []
                P.last_clicked = None
                P.objects = []
                logger.info("Se ha reiniciado la pantalla")

        if event.type == pg.MOUSEBUTTONDOWN:# and pg.mouse.get_pressed()[0]:
            #print(f"-----------\nY:{pg.mouse.get_pos()[1]}\nX:{pg.mouse.get_pos()[0]}")
            min_ = (int(pg.mouse.get_pos()[1]/(H*esc_y/y)))*x
            xmin_ = (int(pg.mouse.get_pos()[0]/(W*esc_x/x)))
            if pg.mouse.get_pos()[0] <= W*esc_x and pg.mouse.get_pos()[1] <= H*esc_y and not DEL:
                if FOCUS != 'grid' and P.last_clicked:
                    P.last_clicked[1].click()
                    P.last_clicked = None
                    for i in MARK:
                        if G.grid[i].state:
                            G.grid[i].color = (0,0,0)
                        else:
                            G.grid[i].color = (255,255,255)
                        
                    for i in ADDED:
                        TO_DRAW.remove(i)
                FOCUS = 'grid'

                try:
                    if G.light and min_ + xmin_ not in G.grid:
                        G.add_pixel(xmin_,min_)
                            
                    i = G.grid[min_ + xmin_]
                    
                    if i.left <= pg.mouse.get_pos()[0] <= i.left+i.width and i.top <= pg.mouse.get_pos()[1] <= i.top+i.height:
                        i.click()
                        if (xmin_,y-(min_//x)) not in POINTS:
                            POINTS.append((xmin_,y-(min_//x)))
                        else:
                            POINTS.remove((xmin_,y-(min_//x)))
                        
                        if i.state:
                            TO_DRAW.append(min_ + xmin_)
                        else:
                            TO_DRAW.remove(min_ + xmin_)
                    
                        
                except Exception as e:
                    logger.exception(e)
                        

            elif P.left <= pg.mouse.get_pos()[0] <= P.left + P.width and P.top <= pg.mouse.get_pos()[1] <= P.top + P.height:
                for k,i in enumerate(P.list_buttons[P.min:P.max]):
                    if i.left <= pg.mouse.get_pos()[0] <= i.left + i.width and i.top <= pg.mouse.get_pos()[1] <= i.top + i.height:
                        FOCUS = 'panel'
                        
                        if P.last_clicked:
                            P.last_clicked[1].click()
                            for l in MARK:
                                G.grid[l].color = (0,0,0)
                            
                        for j in P.objects[P.min:P.max][k].points[1:]:
                            try:
                                if not DEL:
                                    if not i.state:
                                        MARK.append(abs(j[1]-y)*x+j[0])
                                        
                                        G.grid[abs(j[1]-y)*x+j[0]].color = (50,255,50)
                                        if not G.grid[abs(j[1]-y)*x+j[0]].state:
                                            TO_DRAW.append(abs(j[1]-y)*x+j[0])
                                            ADDED.append(abs(j[1]-y)*x+j[0])
                                            
                                    else:
                                        G.grid[abs(j[1]-y)*x+j[0]].color = (50,255,50)
                                        ADDED.append(abs(j[1]-y)*x+j[0])
                                        
                                else:
                                    TO_DRAW.remove(abs(j[1]-y)*x+j[0])

                            except Exception as e:
                                logger.exception(e)
                                #print(P.objects[k].p0,P.objects[k].p1)
                                #print(abs(j[1]-y)*x,j[0])
                        if DEL:
                            del P.objects[k]
                            del P.list_buttons[k]
                            P.last_clicked = None
                            
                        i.click()
                        P.last_clicked = (k,i)
                        
            
            else:
                if P.last_clicked:
                    P.last_clicked[1].click()
                    P.last_clicked = None
                    for i in MARK:
                        if G.grid[i].state:
                            G.grid[i].color = (0,0,0)
                        else:
                            G.grid[i].color = (255,255,255)
                    for i in ADDED:
                        TO_DRAW.remove(i)

    
    if len(TO_DRAW) > 0:
        for i in TO_DRAW:
            G.grid[i].draw(screen)
        
    pg.display.flip()
    
