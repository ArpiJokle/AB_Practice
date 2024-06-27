#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QString File = QFileDialog::getOpenFileName(0, "Open dialog", "", "*.txt");
    std::ifstream fin(File.toStdString());
    int Number;
    MaxElement = INT_MIN;
    while (fin >> Number) {
        Data.push_back(Number);
        if (Number > MaxElement)
            MaxElement = Number;
    }

    Pen = new QPen();
    PenPos = new QPoint(0, 0);
    Pen->setColor(Qt::blue);

    this->update();
}

MainWindow::~MainWindow()
{
    delete ui;
    delete Pen;
    delete PenPos;
}

void MainWindow::paintEvent(QPaintEvent *)
{
    double Step = double(this->width() / MaxElement);
    int Ofset = (this->height()) / (this->Data.size());
    double Y = Ofset / 2;
    Pen->setWidth((this->height() / Data.size()) * 0.5);
    QPainter Painter(this);
    Painter.begin(this);
    Painter.setPen(*Pen);
    for(int i = 0; i < this->Data.size(); i++){
        Painter.drawLine(0, Y, this->Data[i] * Step, Y);
        Y += Ofset;
    }
    Painter.end();

}
