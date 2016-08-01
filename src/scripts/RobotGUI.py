import sys
from PyQt4 import QtGui

class RobotGUI(QtGui.QWidget):
    def __init__(self):
        super(RobotGUI, self).__init__()

        self.initUI()

    def initUI(self):
        font = QtGui.QFont('SansSerif', 10)

        self.grid = grid = QtGui.QGridLayout()
        self.setLayout(grid)

        # Header
        xLabel = QtGui.QLabel('X', self)
        yLabel = QtGui.QLabel('Y', self)
        zLabel = QtGui.QLabel('Z', self)
        grid.addWidget(xLabel, 0, 1)
        grid.addWidget(yLabel, 0, 2)
        grid.addWidget(zLabel, 0, 3)

        # Acceleration
        self.acl = []
        aclLabel = QtGui.QLabel('Acceleration', self)
        grid.addWidget(aclLabel, 1, 0)
        self.acl.append(QtGui.QTextEdit())
        self.acl.append(QtGui.QTextEdit())
        self.acl.append(QtGui.QTextEdit())
        self.addRow(1, self.acl)

        # Speed
        self.speed = []
        speedLabel = QtGui.QLabel('Speed', self)
        grid.addWidget(speedLabel, 2, 0)
        self.speed.append(QtGui.QTextEdit())
        self.speed.append(QtGui.QTextEdit())
        self.speed.append(QtGui.QTextEdit())
        self.addRow(2, self.speed)

        # Position
        self.pos = []
        posLabel = QtGui.QLabel('Position', self)
        grid.addWidget(posLabel, 3, 0)
        self.pos.append(QtGui.QTextEdit())
        self.pos.append(QtGui.QTextEdit())
        self.pos.append(QtGui.QTextEdit())
        self.addRow(3, self.pos)

        labels = [xLabel, yLabel, zLabel, aclLabel, speedLabel, posLabel]
        for label in labels:
            label.setFont(font)

        self.setGeometry(300, 300, 150, 300)
        self.setWindowTitle('ATN ROV')
        self.show()

    def addRow(self, row, elements):
        for text in elements:
            text.setFixedHeight(30)
            text.setFixedWidth(100)
            text.setReadOnly(True)
        for y in range(len(elements)):
            self.grid.addWidget(elements[y], row, y + 1)

    def setSpeedX(self, speed):
        self.speed[0].setText(speed)

    def setSpeedY(self, speed):
        self.speed[1].setText(speed)

    def setSpeedZ(self, speed):
        self.speed[2].setText(speed)

    def setSpeed(self, speeds):
        for i in range(3):
            self.speed[i].setText(speeds[i])

    def setPosX(self, pos):
        self.pos[0].setText(pos)

    def setPosY(self, pos):
        self.pos[1].setText(pos)

    def setPosZ(self, pos):
        self.pos[2].setText(pos)

    def setPos(self, pos):
        for i in range(3):
            self.pos[i].setText(pos[i])

    def setAclX(self, acl):
        self.acl[0].setText(acl)

    def setAclY(self, acl):
        self.acl[1].setText(acl)

    def setAclZ(self, acl):
        self.acl[2].setText(acl)

    def setAcl(self, acl):
        for i in range(3):
            self.acl[i].setText(acl[i])

def main():
    app = QtGui.QApplication(sys.argv)
    ex = RobotGUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()