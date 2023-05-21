import recommendation as re
from PySide6.QtWidgets import QApplication,QMainWindow,QTableWidgetItem
from PySide6.QtCore import  Qt,Signal,QObject
from Window_ui import Ui_MainWindow
from threading import Thread

class Customsignals(QObject):
    recommend_end=Signal()


reco=re.recommendation()
Mysignals=Customsignals()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.re=re.recommendation()
        self.band()

    def band(self):
        self.ui.query_button.clicked.connect(self.query)
        Mysignals.recommend_end.connect(self.print_recommend)
        self.ui.chart_button.clicked.connect(self.get_chart)
        self.ui.records_button.clicked.connect(self.get_records)

    def query(self):
        self.ui.query_button.setEnabled(False)
        self.ui.query_button.setText('计算中')
        userId=self.ui.re_userId.text()
        task=Thread(target=self.get_recommend,args=(userId))
        task.start()

    def get_recommend(self,userId):
        self.recommend=reco.get_recommend(userId)
        Mysignals.recommend_end.emit()

    def print_recommend(self):
        self.ui.reco.setRowCount(0)
        num=int(self.ui.movie_num.text())
        recommend=self.recommend
        # print(recommend)
        row=0
        for i,_i in recommend.iterrows():
            if i=='movieId':
                continue
            if row>=num:
                break
            self.ui.reco.insertRow(row)
            cell1=QTableWidgetItem(str(i))
            cell2=QTableWidgetItem(str(reco.movieId_name(i)))
            self.ui.reco.setItem(row,0,cell1)
            self.ui.reco.setItem(row,1,cell2)
            row+=1
        self.ui.query_button.setEnabled(True)
        self.ui.query_button.setText('开始计算')

    def get_records(self):
        userId=int(self.ui.records_userId.text())
        records=reco.get_user_item(userId)
        self.ui.records.setRowCount(0)
        row=0
        for i in records.itertuples():
            print(i.movieId)
            self.ui.records.insertRow(row)
            cell1=QTableWidgetItem(str(i.movieId))
            cell2=QTableWidgetItem(str(reco.movieId_name(i.movieId)))
            cell3=QTableWidgetItem(str(i.rating))
            self.ui.records.setItem(row,0,cell1)
            self.ui.records.setItem(row,1,cell2)
            self.ui.records.setItem(row,2,cell3)
            row+=1

    def get_chart(self):
        self.ui.chart_button.setEnabled(False)
        self.ui.chart_button.setText('查询中')
        maxmean=float(self.ui.maxmean.text())
        minmean=float(self.ui.minmean.text())
        maxpeo=float(self.ui.maxpeo.text())
        minpeo=float(self.ui.minpeo.text())
        chart=reco.get_charts()
        chart=chart[(chart.num<=maxpeo)&(chart.num>=minpeo)&(chart.score>=minmean)&(chart.score<=maxmean)]
        self.ui.charts.setRowCount(0)
        row=0
        for i in chart.itertuples():
            print(i.title)
            self.ui.charts.insertRow(row)
            cell1=QTableWidgetItem(str(i.Index))
            cell2=QTableWidgetItem(str(i.title))
            cell3=QTableWidgetItem(str(i.num))
            cell4=QTableWidgetItem(str(i.score))
            self.ui.charts.setItem(row,0,cell1)
            self.ui.charts.setItem(row,1,cell2)
            self.ui.charts.setItem(row,2,cell3)
            self.ui.charts.setItem(row,3,cell4)
            row+=1
        self.ui.chart_button.setEnabled(True)
        self.ui.chart_button.setText('开始查询')

if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出