import time , configparser , os , sys , subprocess
from pypresence import Presence
from PySide2 import QtWidgets , QtGui

start_time = time.time()
RPC = Presence(728873948934176831)
RPC.connect()
print("Discord RPC connected")

def main():
    config = configparser.ConfigParser()
    config.read(r'data.ini')

    status   = config['Status']['status']
    prestige = config['Levels']['prestige']
    level    = config['Levels']['level']
    image    = config['Small image']['image']
    tooltip  = config['Tooltip']['tooltip']

    RPC.update(
        start       = start_time,
        state       = "Grinding",
        details     = status,
        large_image = f"prestige_{prestige}",
        large_text  = f"Prestige {prestige} Level {level}",
        small_image = image,
        small_text  = tooltip,
    )
    print("Discord RPC updated!")
    time.sleep(15)

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self , icon , parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self , icon , parent)
        self.setToolTip(f'Dank memer')
        menu = QtWidgets.QMenu(parent)

        pause_ = menu.addAction("Pause")
        pause_.triggered.connect(
            RPC.clear()
            )

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(
            lambda: sys.exit()
            )

        self.setContextMenu(menu)

def tray():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.ico"), w)
    tray_icon.show()
    sys.exit(app.exec_())
    print("System tray loaded successfully!")

while True:
    main() 
    tray()