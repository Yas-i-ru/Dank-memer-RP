import os , sys , configparser , time
from pypresence import Presence
from PySide2 import QtWidgets, QtGui

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'Dank memer : Running')
        menu = QtWidgets.QMenu(parent)

        connect_RPC = menu.addAction("Connect")
        connect_RPC.triggered.connect(self.RP_connect)
        connect_RPC.setIcon(QtGui.QIcon("./resources/connect.svg"))

        disconnect_RPC = menu.addAction("Disconnect")
        disconnect_RPC.triggered.connect(self.RP_disconnect)
        disconnect_RPC.setIcon(QtGui.QIcon("./resources/disconnect.svg"))

        refresh_RPC = menu.addAction("Refresh")
        refresh_RPC.triggered.connect(self.RP_refresh)
        refresh_RPC.setIcon(QtGui.QIcon("./resources/refresh.svg"))
        
        menu.addSeparator()

        configure = menu.addAction("Configure")
        configure.triggered.connect(lambda: os.system('notepad "./data.ini"'))
        configure.setIcon(QtGui.QIcon("./resources/configure.svg"))

        menu.addSeparator()

        info = menu.addAction("Info")
        info.triggered.connect(self.info)
        info.setIcon(QtGui.QIcon("./resources/info.svg"))

        menu.addSeparator()

        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: sys.exit())
        exit_.setIcon(QtGui.QIcon("./resources/exit.svg"))

        self.setContextMenu(menu)
        
    def RP_connect(self):
        self.get_data()
        self.RPC = Presence(728873948934176831)
        self.RPC.connect()

        self.RPC.update(
        start       = time.time(),
        state       = "Grinding",
        details     = self.status,
        large_image = f"prestige_{self.prestige}",
        large_text  = f"Prestige {self.prestige} Level {self.level}",
        small_image = self.image,
        small_text  = self.tooltip,
        )
        self.setToolTip(f'Dank memer : Connected')

    def RP_disconnect(self):
        self.setToolTip(f'Dank memer : Disconnected')
        self.RPC.clear()

    def RP_refresh(self):
        self.setToolTip(f'Dank memer : Refreshing')
        time.sleep(5)
        self.RP_disconnect()
        time.sleep(5)
        self.RP_connect()
        time.sleep(5)

    def get_data(self):
        config = configparser.ConfigParser()
        config.read(r'data.ini')

        self.status   = config['data']['status']
        self.prestige = config['data']['prestige']
        self.level    = config['data']['level']
        self.image    = config['data']['image']
        self.tooltip  = config['data']['tooltip']

    def info(self):
        with open ("./info.txt" , "w") as info:
            info.write(
            """
Dank memer RP

If you have just installed the application configure the data.ini first. After you configure the data.ini save it and
and connect. Disconnecting/Connecting is rate limited so it may take few seconds for the application to properly update
the rich presence.

Connect    : The application will start the rich presence with the discord client.
Disconnect : The application will stop the rich presence with the discord client.
Refresh    : The application will refresh the current state of the activity.
Configure  : Opens data.ini on notepad.
Info       : Creates the info.txt and opens it.
Exit       : Exits the application and ends the client session.

Version    : v.2.0.0
Build      : Public

More help : https://discord.gg/invite/zNJv2Uv
Releases  : https://github.com/yasirukavishka/Dank-memer-RP/releases/
            """
            )
        info.close()
        os.system('notepad "./info.txt"')

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("./resources/icon.ico"), w)
    tray_icon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()