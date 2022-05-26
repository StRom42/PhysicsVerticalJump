# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'params.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_ParamsUi(object):
    def setupUi(self, ParamsUi):
        if not ParamsUi.objectName():
            ParamsUi.setObjectName(u"ParamsUi")
        ParamsUi.resize(405, 543)
        self.gridLayout = QGridLayout(ParamsUi)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spinBox_5 = QSpinBox(ParamsUi)
        self.spinBox_5.setMaximum(300)
        self.spinBox_5.setObjectName(u"spinBox_5")


        self.gridLayout.addWidget(self.spinBox_5, 4, 1, 1, 1)

        self.spinBox_3 = QSpinBox(ParamsUi)
        self.spinBox_3.setMaximum(300)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.label_4 = QLabel(ParamsUi)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_6 = QLabel(ParamsUi)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label = QLabel(ParamsUi)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(ParamsUi)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.height_input = QSpinBox(ParamsUi)
        self.height_input.setMaximum(300)
        self.height_input.setValue(183)
        self.height_input.setObjectName(u"height_input")

        self.gridLayout.addWidget(self.height_input, 0, 1, 1, 1)

        self.spinBox_6 = QSpinBox(ParamsUi)
        self.spinBox_6.setMaximum(300)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout.addWidget(self.spinBox_6, 5, 1, 1, 1)

        self.mass_input = QSpinBox(ParamsUi)
        self.mass_input.setMaximum(300)
        self.mass_input.setValue(80)
        self.mass_input.setObjectName(u"mass_input")

        self.gridLayout.addWidget(self.mass_input, 1, 1, 1, 1)

        self.label_5 = QLabel(ParamsUi)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(ParamsUi)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.spinBox_4 = QSpinBox(ParamsUi)
        self.spinBox_4.setMaximum(300)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout.addWidget(self.spinBox_4, 3, 1, 1, 1)

        self.calc_button = QPushButton(ParamsUi)
        self.calc_button.setObjectName(u"calc_button")

        self.gridLayout.addWidget(self.calc_button, 6, 0, 1, 2)


        self.retranslateUi(ParamsUi)

        QMetaObject.connectSlotsByName(ParamsUi)
    # setupUi

    def retranslateUi(self, ParamsUi):
        ParamsUi.setWindowTitle(QCoreApplication.translate("ParamsUi", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("ParamsUi", u"\u0414\u043b\u0438\u043d\u0430 \u0433\u043e\u043b\u0435\u043d\u0438:", None))
        self.label_6.setText(QCoreApplication.translate("ParamsUi", u"\u041e\u0431\u0445\u0432\u0430\u0442 \u0438\u043a\u0440\u044b: ", None))
        self.label.setText(QCoreApplication.translate("ParamsUi", u"\u0420\u043e\u0441\u0442:", None))
        self.label_3.setText(QCoreApplication.translate("ParamsUi", u"\u0414\u043b\u0438\u043d\u0430 \u0431\u0435\u0434\u0440\u0430:", None))
        self.label_5.setText(QCoreApplication.translate("ParamsUi", u"\u041e\u0431\u0445\u0432\u0430\u0442 \u0431\u0435\u0434\u0440\u0430: ", None))
        self.label_2.setText(QCoreApplication.translate("ParamsUi", u"\u041c\u0430\u0441\u0441\u0430 \u0442\u0435\u043b\u0430:", None))
        self.calc_button.setText(QCoreApplication.translate("ParamsUi", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi

