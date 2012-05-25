#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *


class EIOWindow(QMainWindow):

    def __init__(self, parent=None):
        super(EIOWindow, self).__init__(parent)
        self.setWindowTitle("EtherIO")

        centre = EIOCentralWidget()

        self.setCentralWidget(centre)

class EIOCentralWidget(QWidget):

    def __init__(self, parent=None):
        super(EIOCentralWidget, self).__init__(parent)

        # widgets which will be contained in the central widget
        self.dac0 = DACGroupBox("DAC 0", 0.0)

        # layout of the widgets
        layout = QGridLayout()
        layout.addWidget(self.dac0)

        self.setLayout(layout)

        # signals

class DACGroupBox(QGroupBox):

    def __init__(self, parent=None, name="DAC #", value=0.0):
        super(DACGroupBox, self).__init__(parent)

        # DAC value
        self.value = value

        # widgets in the box
        self.DACSlider = QSlider(Qt.Vertical)
        self.DACText = QLineEdit("%7.4f V" % self.value)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.DACSlider, 0, Qt.AlignHCenter)
        layout.addWidget(self.DACText)

        self.setLayout(layout)

if __name__ == '__main__':
    # create the app
    app = QApplication(sys.argv)
    # show the form
    main = EIOWindow()
    main.show()
    main.raise_()
    # run the main loop
    sys.exit(app.exec_())

