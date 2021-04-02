# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_money_received_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 2, 1, 1)
        self.received_date = QtWidgets.QDateEdit(self.centralwidget)
        self.received_date.setObjectName("received_date")
        self.gridLayout.addWidget(self.received_date, 10, 2, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 21, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 19, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 7, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 14, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 15, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 18, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 10, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 12, 1, 1, 1)
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setObjectName("type")
        self.gridLayout.addWidget(self.type, 12, 2, 1, 3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 15, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 4, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 16, 1, 1, 1)
        self.save_n_exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_exit_btn.setObjectName("save_n_exit_btn")
        self.gridLayout.addWidget(self.save_n_exit_btn, 20, 4, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 13, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 13, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 14, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 17, 4, 1, 1)
        self.amount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.amount.setMaximum(1e+28)
        self.amount.setObjectName("amount")
        self.gridLayout.addWidget(self.amount, 14, 2, 1, 2)
        self.remarks = QtWidgets.QTextEdit(self.centralwidget)
        self.remarks.setObjectName("remarks")
        self.gridLayout.addWidget(self.remarks, 18, 2, 1, 3)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 20, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem15, 17, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 11, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem17, 7, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 9, 2, 1, 1)
        self.save_n_new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_new_btn.setObjectName("save_n_new_btn")
        self.gridLayout.addWidget(self.save_n_new_btn, 20, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem19, 21, 4, 1, 1)
        self.customer = QtWidgets.QComboBox(self.centralwidget)
        self.customer.setObjectName("customer")
        self.gridLayout.addWidget(self.customer, 6, 2, 1, 3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 1, 1, 1)
        self.discount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.discount.setMaximum(1e+23)
        self.discount.setObjectName("discount")
        self.gridLayout.addWidget(self.discount, 16, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 18, 1, 1, 1)
        self.order_number = QtWidgets.QLineEdit(self.centralwidget)
        self.order_number.setObjectName("order_number")
        self.gridLayout.addWidget(self.order_number, 8, 2, 1, 3)
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 3, 2, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout.addWidget(self.search_btn, 3, 3, 1, 1)
        self.id = QtWidgets.QComboBox(self.centralwidget)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 4, 2, 1, 1)
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setObjectName("edit_btn")
        self.gridLayout.addWidget(self.edit_btn, 4, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Search"))
        self.label_6.setText(_translate("MainWindow", "Amount"))
        self.label_3.setText(_translate("MainWindow", "Order Number"))
        self.label_4.setText(_translate("MainWindow", "Received Date"))
        self.label_5.setText(_translate("MainWindow", "Type"))
        self.label_9.setText(_translate("MainWindow", "Money Received"))
        self.label_7.setText(_translate("MainWindow", "Discount"))
        self.save_n_exit_btn.setText(_translate("MainWindow", "Save and Exit"))
        self.label_2.setText(_translate("MainWindow", "Customer"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.save_n_new_btn.setText(_translate("MainWindow", "Save and New"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow", "Remarks"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))
