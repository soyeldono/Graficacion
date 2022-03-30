#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;


public slots:

private slots:
    void on_verticalSliderX_actionTriggered(int action);
    void on_verticalSliderY_actionTriggered(int action);
    void on_verticalSliderZ_actionTriggered(int action);
    void on_verticalSliderX_sliderMoved(int position);
    void on_verticalSliderY_sliderMoved(int position);
    void on_verticalSliderZ_sliderMoved(int position);
};
#endif // MAINWINDOW_H
