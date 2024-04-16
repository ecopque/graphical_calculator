# main.py (A)
import sys
from PySide6.QtWidgets import (QApplication, QLabel)
from main_window import cls_mainwindow

from PySide6.QtGui import QIcon

from variables import PATH_WINDOW_ICON_PATH
from display import cls_display

if __name__ == '__main__':
    # Create the application:
    var_app = QApplication(sys.argv)
    var_window = cls_mainwindow()
    
    #
    var_label = QLabel('Enter your operation')
    var_label.setStyleSheet('font-size: 10px;')

    var_window.mtd_addwidgettoverticallayout(var_label)
    # var_window.mtd_adjustfixedsize() #A1:

    # Defining icon
    var_icon = QIcon(str(PATH_WINDOW_ICON_PATH))
    var_window.setWindowIcon(var_icon)
    var_app.setWindowIcon(var_icon)

    # Display
    var_display = cls_display()
    # var_display = cls_display('aaa')
    var_display.setPlaceholderText('Enter your operation')
    var_window.mtd_addwidgettoverticallayout(var_display)
    

    var_window.mtd_addwidgettoverticallayout(cls_display('bbb'))

    var_window.mtd_adjustfixedsize() #A1:
    # Runs everything
    var_window.show()
    var_app.exec()

#A1: We could put it inside #B1 / def my_addWidgetToVerticalLayout.
