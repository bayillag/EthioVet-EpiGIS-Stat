# -*- coding: utf-8 -*-

"""
/***************************************************************************
 EthioVet-EpiGIS-Stat
 Specialized for Jinka Regional Veterinary Laboratory
 
 Form implementation generated from reading ui file 'globalt_dialog_base.ui'
 Updated for PyQt6 / QGIS 4
 ***************************************************************************/
"""

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 471)
        
        # Main Layout
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        
        # Splitter for Data Field
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setMinimumSize(QtCore.QSize(251, 0))
        self.comboBox.setObjectName("comboBox")
        
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 7)
        
        # Neighboring Method Section
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_3.addWidget(self.comboBox_5, 1, 1, 1, 3)
        
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | 
                                   QtCore.Qt.AlignmentFlag.AlignTrailing | 
                                   QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 4, 1, 1)
        
        self.comboBox_6 = QtWidgets.QComboBox(Dialog)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_3.addWidget(self.comboBox_6, 1, 5, 1, 1)
        
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Policy.Expanding, 
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 6, 1, 1)
        
        # Weighting Scheme Section
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 2, 0, 1, 2)
        
        spacerItem1 = QtWidgets.QSpacerItem(64, 20, QtWidgets.QSizePolicy.Policy.Expanding, 
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 2, 1, 1)
        
        # Variance Assumption
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 3, 1, 2)
        
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_3.addWidget(self.comboBox_4, 2, 5, 1, 1)
        
        # Alternative Hypothesis
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 3, 0, 1, 3)
        
        spacerItem2 = QtWidgets.QSpacerItem(254, 20, QtWidgets.QSizePolicy.Policy.Expanding, 
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 4, 1, 2)
        
        # Execute Button
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_3.addWidget(self.toolButton, 3, 6, 1, 1)
        
        # Results Display
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 4, 0, 1, 7)
        
        # Dialog Buttons
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Close | 
                                          QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 5, 4, 1, 3)

        self.retranslateUi(Dialog)
        
        # Modern Signal/Slot connections
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EthioVet: Global Spatial Statistics"))
        self.label.setText(_translate("Dialog", "Livestock Data Field:"))
        self.label_5.setText(_translate("Dialog", "Neighbouring Method:"))
        self.label_2.setText(_translate("Dialog", "Weighting Scheme:"))
        self.label_4.setText(_translate("Dialog", "Variance Assumption:"))
        self.label_3.setText(_translate("Dialog", "Hypothesis (Greater/Less):"))
        self.toolButton.setText(_translate("Dialog", "Run Analysis"))
