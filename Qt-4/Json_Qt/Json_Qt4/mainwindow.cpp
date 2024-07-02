#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
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
    if (Data.size() == 0)
        return;
    double Step = double(this->width() / MaxElement);
    int Ofset = (this->height()) / (Data.size());
    double Y = Ofset / 2;
    Pen->setWidth((this->height() / Data.size()) * 0.5);
    QPainter Painter(this);
    Painter.begin(this);
    Painter.setPen(*Pen);
    for (int i = 0; i < Data.size(); i++) {
        Painter.drawLine(0, Y, Data[i] * Step, Y);
        Y += Ofset;
    }
    Painter.end();
}

void MainWindow::on_importButton_clicked()
{
    QString File = QFileDialog::getOpenFileName(0, "Open dialog", "", "*.json");
    std::fstream fin(File.toStdString());
    if (!fin.is_open())
        return;
    Json = nlohmann::json::parse(fin);
    fin.close();
    UpDate();
    this->update();
}

void MainWindow::on_addButton_clicked()
{
    Json[(ui->fieldName->text()).toStdString()] = ui->fieldValue->value();
    UpDate();
    this->update();
}

void MainWindow::UpDate()
{
    Data.clear();
    for (auto i : Json)
        Data.push_back(i);
    MaxElement = *(std::max_element(Data.begin(), Data.end()));
}

void MainWindow::on_saaveButton_clicked()
{
    QString file = QFileDialog::getOpenFileName(0, "Open dialog", "", "*.json");
    if (file.toStdString() == "")
        return;
    std::ofstream fout(file.toStdString());
    fout << Json.dump(4);
}

