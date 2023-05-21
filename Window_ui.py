# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QSplitter, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1084, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(17)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.re_userId = QSpinBox(self.groupBox)
        self.re_userId.setObjectName(u"re_userId")
        font1 = QFont()
        font1.setPointSize(18)
        self.re_userId.setFont(font1)
        self.re_userId.setMinimum(1)
        self.re_userId.setMaximum(610)

        self.verticalLayout_2.addWidget(self.re_userId)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.movie_num = QSpinBox(self.groupBox)
        self.movie_num.setObjectName(u"movie_num")
        self.movie_num.setFont(font1)
        self.movie_num.setMaximum(9743)

        self.verticalLayout_2.addWidget(self.movie_num)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.query_button = QPushButton(self.groupBox)
        self.query_button.setObjectName(u"query_button")
        self.query_button.setFont(font1)

        self.verticalLayout_3.addWidget(self.query_button)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(15)
        self.label_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_2)

        self.reco = QTableWidget(self.groupBox)
        if (self.reco.columnCount() < 2):
            self.reco.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.reco.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.reco.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.reco.setObjectName(u"reco")
        font3 = QFont()
        font3.setPointSize(14)
        self.reco.setFont(font3)
        self.reco.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.reco)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addWidget(self.groupBox)

        self.quick_query = QTabWidget(self.centralwidget)
        self.quick_query.setObjectName(u"quick_query")
        self.quick_charts = QWidget()
        self.quick_charts.setObjectName(u"quick_charts")
        self.verticalLayout = QVBoxLayout(self.quick_charts)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.quick_charts)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font2)
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        font4 = QFont()
        font4.setPointSize(10)
        self.groupBox_4.setFont(font4)
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minmean = QDoubleSpinBox(self.groupBox_4)
        self.minmean.setObjectName(u"minmean")
        self.minmean.setFont(font3)
        self.minmean.setMaximum(5.000000000000000)

        self.horizontalLayout.addWidget(self.minmean)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(36)
        self.label_4.setFont(font5)

        self.horizontalLayout.addWidget(self.label_4)

        self.maxmean = QDoubleSpinBox(self.groupBox_4)
        self.maxmean.setObjectName(u"maxmean")
        self.maxmean.setFont(font3)
        self.maxmean.setMaximum(5.000000000000000)

        self.horizontalLayout.addWidget(self.maxmean)


        self.horizontalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font4)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minpeo = QSpinBox(self.groupBox_5)
        self.minpeo.setObjectName(u"minpeo")
        self.minpeo.setFont(font3)

        self.horizontalLayout_2.addWidget(self.minpeo)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.maxpeo = QSpinBox(self.groupBox_5)
        self.maxpeo.setObjectName(u"maxpeo")
        self.maxpeo.setFont(font3)
        self.maxpeo.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.maxpeo)


        self.horizontalLayout_7.addWidget(self.groupBox_5)

        self.chart_button = QPushButton(self.groupBox_3)
        self.chart_button.setObjectName(u"chart_button")

        self.horizontalLayout_7.addWidget(self.chart_button)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.charts = QTableWidget(self.quick_charts)
        if (self.charts.columnCount() < 4):
            self.charts.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.charts.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.charts.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.charts.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.charts.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.charts.setObjectName(u"charts")
        self.charts.setFont(font3)
        self.charts.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.charts)

        self.quick_query.addTab(self.quick_charts, "")
        self.quick_user = QWidget()
        self.quick_user.setObjectName(u"quick_user")
        self.verticalLayout_7 = QVBoxLayout(self.quick_user)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.splitter = QSplitter(self.quick_user)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.records_userId = QSpinBox(self.layoutWidget)
        self.records_userId.setObjectName(u"records_userId")
        self.records_userId.setFont(font1)
        self.records_userId.setMinimum(1)
        self.records_userId.setMaximum(610)

        self.verticalLayout_5.addWidget(self.records_userId)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.records_button = QPushButton(self.layoutWidget)
        self.records_button.setObjectName(u"records_button")
        self.records_button.setFont(font1)

        self.verticalLayout_5.addWidget(self.records_button)

        self.splitter.addWidget(self.layoutWidget)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.records = QTableWidget(self.groupBox_2)
        if (self.records.columnCount() < 3):
            self.records.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.records.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.records.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.records.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.records.setObjectName(u"records")
        self.records.setFont(font3)
        self.records.horizontalHeader().setDefaultSectionSize(138)
        self.records.horizontalHeader().setProperty("showSortIndicator", False)
        self.records.horizontalHeader().setStretchLastSection(True)
        self.records.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_6.addWidget(self.records)

        self.splitter.addWidget(self.groupBox_2)

        self.verticalLayout_7.addWidget(self.splitter)

        self.quick_query.addTab(self.quick_user, "")

        self.horizontalLayout_6.addWidget(self.quick_query)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1084, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.quick_query.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u67d0\u4e2a\u7528\u6237\u7684\u63a8\u8350\u5217\u8868", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237Id:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf:", None))
        self.query_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u63a8\u8350\u7535\u5f71\u5217\u8868:", None))
        ___qtablewidgetitem = self.reco.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5f71Id", None));
        ___qtablewidgetitem1 = self.reco.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5f71", None));
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7b5b\u9009", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u5206\u8303\u56f4", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u89c2\u770b\u4eba\u6570\u8303\u56f4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.chart_button.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        ___qtablewidgetitem2 = self.charts.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5f71Id", None));
        ___qtablewidgetitem3 = self.charts.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5f71", None));
        ___qtablewidgetitem4 = self.charts.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u770b\u4eba\u6570", None));
        ___qtablewidgetitem5 = self.charts.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u5747\u5206", None));
        self.quick_query.setTabText(self.quick_query.indexOf(self.quick_charts), QCoreApplication.translate("MainWindow", u"\u7535\u5f71\u603b\u5206\u6392\u884c\u699c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237Id:", None))
        self.records_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u67e5\u8be2", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u89c2\u5f71\u5386\u53f2", None))
        ___qtablewidgetitem6 = self.records.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5f71Id", None));
        ___qtablewidgetitem7 = self.records.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u7535\u5f71", None));
        ___qtablewidgetitem8 = self.records.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5206", None));
        self.quick_query.setTabText(self.quick_query.indexOf(self.quick_user), QCoreApplication.translate("MainWindow", u"\u7528\u6237\u89c2\u5f71\u8bb0\u5f55", None))
    # retranslateUi

