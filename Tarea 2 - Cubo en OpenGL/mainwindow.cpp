#include "mainwindow.h"
#include "ui_mainwindow.h"


#include <iostream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_verticalSliderX_actionTriggered(int action)
{

    if (ui->widget->plus)
        ui->widget->xr += action;
    else
        ui->widget->xr -= action;
}


void MainWindow::on_verticalSliderY_actionTriggered(int action)
{
    if (ui->widget->plus)
        ui->widget->yr += action;
    else
        ui->widget->yr -= action;
}


void MainWindow::on_verticalSliderZ_actionTriggered(int action)
{

    if (ui->widget->plus)
        ui->widget->zr += action;
    else
        ui->widget->zr -= action;
}


void MainWindow::on_verticalSliderX_sliderMoved(int position)
{
    if (ui->widget->barpos < position) {
        ui->widget->plus = false;
    }else{
        ui->widget->plus = true;
    }
    ui->widget->barpos = position;

}


void MainWindow::on_verticalSliderY_sliderMoved(int position)
{
    if (ui->widget->barpos < position) {
        ui->widget->plus = false;
    }else{
        ui->widget->plus = true;
    }
    ui->widget->barpos = position;
}


void MainWindow::on_verticalSliderZ_sliderMoved(int position)
{
    if (ui->widget->barpos < position) {
        ui->widget->plus = false;
    }else{
        ui->widget->plus = true;
    }
    ui->widget->barpos = position;
}

