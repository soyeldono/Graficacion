#include "widgetopengl.h"
#include <iostream>


WidgetOpenGL::WidgetOpenGL(QWidget *parent):QOpenGLWidget(parent)
{

}

void WidgetOpenGL::initializeGL()
{
   initializeOpenGLFunctions();
   glEnable(GL_DEPTH_TEST);

}


void WidgetOpenGL::resizeGL(int w, int h)
{


}


void WidgetOpenGL::paintGL()
{
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
    glDepthFunc(GL_LESS);
    glEnable(GL_DEPTH_TEST);
    glShadeModel(GL_SMOOTH);
    // Resetear transformaciones
    glLoadIdentity();

    glRotatef(xr, 1.0, 0.0, 0.0);
    glRotatef(yr, 0.0, 1.0, 0.0);
    glRotatef(zr, 0.0, 0.0, 1.0);

    // LADO FRONTAL
    glBegin(GL_POLYGON);


    glColor3f( 1.0, 0.0, 0.0 );
    glVertex3f(  0.5, -0.5, -0.5 );
    glColor3f( 0.0, 1.0, 0.0 );
    glVertex3f(  0.5,  0.5, -0.5 );
    glColor3f( 0.0, 0.0, 1.0 );
    glVertex3f( -0.5,  0.5, -0.5 );
    glColor3f( 1.0, 0.0, 1.0 );
    glVertex3f( -0.5, -0.5, -0.5 );

    glEnd();

    glBegin(GL_POLYGON); //blanco
    glColor3f( 1.0, 1.0,1.0);
    glVertex3f(0.5,-0.5,0.5);
    glVertex3f(0.5, 0.5,0.5);
    glVertex3f(-0.5,0.5,0.5);
    glVertex3f(-0.5,-0.5,0.5);
    glEnd();

    glBegin(GL_POLYGON); // morado
    glColor3f( 1.0, 0.0,1.0);
    glVertex3f(0.5,-0.5,-0.5);
    glVertex3f(0.5, 0.5,-0.5);
    glVertex3f(0.5, 0.5, 0.5);
    glVertex3f(0.5,-0.5, 0.5);
    glEnd();

    glBegin(GL_POLYGON); // verde
    glColor3f( 0.0, 1.0,0.0);
    glVertex3f(-0.5,-0.5, 0.5);
    glVertex3f(-0.5, 0.5, 0.5);
    glVertex3f(-0.5, 0.5,-0.5);
    glVertex3f(-0.5,-0.5,-0.5);
    glEnd();

    glBegin(GL_POLYGON); // azul
    glColor3f( 0.0, 0.0, 1.0);
    glVertex3f( 0.5, 0.5, 0.5);
    glVertex3f( 0.5, 0.5,-0.5);
    glVertex3f(-0.5, 0.5,-0.5);
    glVertex3f(-0.5, 0.5, 0.5);
    glEnd();

    glBegin(GL_POLYGON); // rojo
    glColor3f( 1.0, 0.0,0.0);
    glVertex3f( 0.5,-0.5,-0.5);
    glVertex3f( 0.5,-0.5, 0.5);
    glVertex3f(-0.5,-0.5, 0.5);
    glVertex3f(-0.5,-0.5,-0.5);
    glEnd();

    glFlush();
      this->makeCurrent();

    update();


}
