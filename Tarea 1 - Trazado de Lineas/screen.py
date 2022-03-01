import pygame as pg
from pygame.locals import *
from typing import Tuple, Union, Sequence
from Objects.line import Line
from Objects.triangle import Triangle
import random as rd

class Button:
    def __init__(self,left: float,top: float,width: float,height: float,state: bool=False,color: Tuple[int, int, int]=(255,255,255),text: str="",font_size: int=10,
                text_color: Tuple[int,int,int]=(0,255,255)) -> None:
        self.state = state
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
    
    def click(self):
        self.state = not self.state
        #print(f"Button:{self} has been pressed, new state:{self.state}")
    
    
    def draw(self,screen):
        pg.draw.rect(screen,self.color,(self.left,self.top,self.width,self.height),0)
        
        #pg.draw.rect(screen,(0,0,0),(self.left,self.top,self.width,self.height),2 if not self.state else -1)
        if self.text != "":
            font = pg.font.SysFont('arial black',self.font_size)
            text = font.render(self.text,True,self.text_color)
            x = (self.left + self.left+self.width)//2
            y = (self.top + self.top+self.height)//2
            screen.blit(text,(x,y))
    

class Pixel(Button):
    def __init__(self,left: float,top: float,width: float,height: float,state: bool=False,color: Tuple[int, int, int]=(255,255,255),color_off=(0,0,0)) -> None:
        """
        Create a Button that simulate a pixel on the grid

        Parameters
        ----------
            left: float
                Coordinate X from upper left corner of Pixel
            top: float
                Coordinate Y from upper left corner of Pixel
            widht: float
                Width of Pixel
            height: float
                Height of Pixel
            state: bool, optinal
                Represent if the pixel is on or off, defautl False
            color: tuple[int, int, int]
                RGB color of Pixel
        """
        super().__init__(left,top,width,height,state,color)
        self.color_off = color_off
    
    def click(self):
        self.color = self.color_off if not self.state else self.color
        self.state = not self.state
    
    def draw(self, screen):
        pg.draw.rect(screen,self.color,(self.left,self.top,self.width,self.height),0)


class Grid:
    def __init__(self,size,grid_size,esc,light=False) -> None:
        """
        Create a grid with size (grid_size) that simulate pixels of screen. The grid
        could be drawed with Pygame.

        Parameters
        ----------
            size: tuple (int x, int y)
                Size of the screen that will be drawed
            grid_size: tuple (int x, int y)
                Size of grid
            esc: tuple (float x, float y), x,y (0,1]
                Escale the size of each pixel using size as base
            light: bool, optional default False
                Create the grid in light mode for hard processing
        
        See Also
        --------
            Class Pixel
        """
        self.w = size[0]
        self.h = size[1]
        self.size = size
        self.nx = grid_size[0]
        self.ny = grid_size[1]
        self.n = grid_size
        self.esc_x = esc[0]
        self.esc_y = esc[1]
        self.esc = esc
        self.light = light
        self.grid = self.__create_grid()

    def __create_grid(self):
        if not self.light:
            G = []
            for Y in range(self.ny):
                for X in range(self.nx):
                    G.append(Pixel((self.w*self.esc_x/self.nx)*X,(self.h*self.esc_y/self.ny)*Y,(self.w*self.esc_x/self.nx)+2,(self.h*self.esc_y/self.ny)+2))
        else:
            G = {}
        return G
    
    def add_pixel(self,X,Y):
        """
        Only for Grid with light in True
        """
        if self.light:
            self.grid[X+Y] = Pixel((self.w*self.esc_x/self.nx)*X,(self.h*self.esc_y/self.ny)*(Y/self.nx),(self.w*self.esc_x/self.nx)+2,(self.h*self.esc_y/self.ny)+2)
        else:
            raise TypeError("This method is exclusive for grid with self.light in True")
    
    def draw(self,screen):
        for i in self.grid:
            i.draw(screen)
    
    def clear(self):
        for i in self.grid:
            i.state = False
    

class SubPanel(Button):
    def __init__(self, left: float, top: float, width: float, height: float, state: bool = False, color: Tuple[int, int, int] = (255, 255, 255), text: str = "", 
                font_size: int = 10, text_color: Tuple[int, int, int] = (0, 255, 255),) -> None:
        super().__init__(left, top, width, height, state, color, text, font_size, text_color)
    
    def draw(self, screen):
        pg.draw.rect(screen,self.color,(self.left,self.top,self.width,self.height),0)

        if self.text != "":
            font = pg.font.SysFont('arial black',self.font_size)
            text = font.render(self.text,True,self.text_color)
            x = (self.left + self.left+self.width)//2
            y = (self.top + self.top+self.height)//2
            screen.blit(text,(x,y)) 

    def click(self):
        self.color = (150,150,150) if not self.state else (255,255,255)
        self.state = not self.state
    

class Panel:
    def __init__(self,objects: Sequence[Union[Line,Triangle]],left: float,top: float,width: float,height: float,focus: int=0,color: Tuple[int, int, int]=(255,255,255),
                text: str="",font_size: int=10,color_objects=(150,150,150),show: int=10) -> None:
        self.focus = focus
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font_size = font_size
        self.color_objects = color_objects
        self.show = show
        #self.panel = Button(left,top,width,height,state,color,text,font_size)
        self.objects = objects
        self.list_buttons = self.__create_list()
        self.min = 0
        self.max = 10
        self.last_clicked = None
    
    def __create_list(self,):
        L = []
        for k,i in enumerate(self.objects):
            L.append(SubPanel(self.left,self.top+(self.height/self.show*k),self.width,self.height/self.show,text_color=(0,0,0),text=str(i.name)))
        return L
    
    def add_object(self, ob):
        if len(self.list_buttons) > 0:
            self.list_buttons.append(SubPanel(self.left,self.top+(self.height/self.show)*len(self.list_buttons),self.width,self.height/self.show,text_color=(0,0,0),text=str(ob.name)))
            self.objects.append(ob)
        else:
            self.list_buttons.append(SubPanel(self.left,self.top,self.width,self.height/self.show,text_color=(0,0,0),text=str(ob.name)))
            self.objects.append(ob)
    
    def draw(self,screen):
        #pg.draw.rect(screen,self.color,(self.left,self.top,self.width,self.height),-1)
        pg.draw.line(screen, self.color, (self.left,self.top), (self.left+self.width,self.top))
        pg.draw.line(screen, self.color, (self.left,self.top), (self.left,self.top+self.height))
        pg.draw.line(screen, self.color, (self.left+self.width,self.top), (self.left+self.width,self.top+self.height))
        pg.draw.line(screen, self.color, (self.left,self.top+self.height), (self.left+self.width,self.top+self.height))

        for i in self.list_buttons[self.min:self.max]:
            i.draw(screen)
        
