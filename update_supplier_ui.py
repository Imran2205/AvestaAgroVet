# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_supplier_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.save_n_new_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_new_btn.setObjectName("save_n_new_btn")
        self.gridLayout.addWidget(self.save_n_new_btn, 9, 2, 1, 1)
        self.email_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.email_line_edit.setObjectName("email_line_edit")
        self.gridLayout.addWidget(self.email_line_edit, 7, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.contact_person_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.contact_person_line_edit.setObjectName("contact_person_line_edit")
        self.gridLayout.addWidget(self.contact_person_line_edit, 4, 1, 1, 3)
        self.supplier_name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.supplier_name_line_edit.setObjectName("supplier_name_line_edit")
        self.gridLayout.addWidget(self.supplier_name_line_edit, 3, 1, 1, 3)
        self.address_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.address_text_edit.setObjectName("address_text_edit")
        self.gridLayout.addWidget(self.address_text_edit, 5, 1, 1, 3)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 9, 3, 1, 1)
        self.save_n_exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_n_exit_btn.setObjectName("save_n_exit_btn")
        self.gridLayout.addWidget(self.save_n_exit_btn, 9, 1, 1, 1)
        self.number_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.number_line_edit.setObjectName("number_line_edit")
        self.gridLayout.addWidget(self.number_line_edit, 8, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.search = QtWidgets.QLineEdit(self.centralwidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 1, 1, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout.addWidget(self.search_btn, 1, 2, 1, 1)
        self.id = QtWidgets.QComboBox(self.centralwidget)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 2, 1, 1, 1)
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setObjectName("edit_btn")
        self.gridLayout.addWidget(self.edit_btn, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Customer"))
        self.save_n_new_btn.setText(_translate("MainWindow", "Save and New"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label.setText(_translate("MainWindow", "Sipplier ID"))
        self.label_8.setText(_translate("MainWindow", "Add Supplier"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.save_n_exit_btn.setText(_translate("MainWindow", "Save and Exit"))
        self.label_2.setText(_translate("MainWindow", "Supplier Name"))
        self.label_4.setText(_translate("MainWindow", "Contact Person"))
        self.label_6.setText(_translate("MainWindow", "Email"))
        self.label_9.setText(_translate("MainWindow", "Number"))
        self.label_5.setText(_translate("MainWindow", "Search"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.edit_btn.setText(_translate("MainWindow", "Edit"))
