from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot, pyqtSignal, QObject
import sys

# Additional libraries
import system

# Fixed
UI_PATH = system.resource_path('main.ui')
ICON_PATH = system.resource_path('icon.ico')


class Signal(QObject):
    signal = pyqtSignal(bool)  # Signal data type


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signalProxy = Signal()
        self.signal = self.signalProxy.signal

    @pyqtSlot()
    def run(self):
        """Do something"""
        self.signal.emit(True)  # Emit based on signal data type
        pass


class MainWindow(QMainWindow):
    def __init__(self, parent):  # Include parent for child window
        super(MainWindow, self).__init__()  # For parent window
        super(MainWindow, self).__init__(parent)  # For child window
        loadUi(UI_PATH, self)
        self.setWindowIcon(QIcon(ICON_PATH))

        # Threading
        self.threadpool = QThreadPool(self)

    def closeEvent(self, event):
        try:
            """Do somthing"""
            pass
        except:
            return

    def showEvent(self, event):
        try:
            """Do somthing"""
            pass
        except:
            return

    def Thread_Handler(self):
        self.worker = Worker()
        self.worker.signal.connect(self.Signal_Handler)
        self.threadpool.start(self.worker)

    def Signal_Handler(self, value):
        """Do something"""
        print(value)
        pass


if __name__ == "__main__":
    system.suppress_qt_warnings()
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
