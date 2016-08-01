#!/usr/bin/env python

import rospy
import json
from robot_interface.msg import *
from RobotGUI import RobotGUI
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
gui = RobotGUI()

def callback(data):
    # print("test OK")
    # rospy.loginfo(rospy.get_caller_id() + 'Received: %s', data.status)
    status = json.loads(data.status)
    time = status['time']
    aclx = status['aclx']
    acly = status['acly']
    aclz = status['aclz']
    # gui.setAclX(aclx)
    # gui.setAclY(acly)
    # gui.setAclZ(aclz)
    print(time, ", ", aclx, ", ", acly, ", ", aclz)
    # print(data.status)



def listener():
    rospy.init_node('navdataListener', anonymous=True)

    rospy.Subscriber('/openrov/status', rovstatus, callback)

    print(rospy.get_caller_id())

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()


if __name__ == '__main__':
    listener()
    sys.exit(app.exec_())
