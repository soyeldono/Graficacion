#ifndef WIDGETOPENGL_H
#define WIDGETOPENGL_H

#include <QOpenGLWidget>
#include <QOpenGLFunctions>
#include <QGLFramebufferObjectFormat>

class WidgetOpenGL : public QOpenGLWidget,protected QOpenGLFunctions
{
public:
    WidgetOpenGL();


explicit WidgetOpenGL(QWidget *parent = 0);
protected:
    void initializeGL() Q_DECL_OVERRIDE;
    void resizeGL(int w, int h)Q_DECL_OVERRIDE;
    void paintGL()Q_DECL_OVERRIDE;

public:
    double yr = 0;
    double xr = 0;
    double zr = 0;

    int barpos = 0;
    bool plus = true;


};

#endif // WIDGETOPENGL_H
