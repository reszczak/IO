import datetime

from CameraRecord import downloadDataFromCameras
from CameraController import Controller


c1 = Controller
c1.__init__(c1, '111', True)
# c1.alarm = True
# c1.errorcode = 123
# c1.isErrorCode = True

i = 0
while True:

    if c1.alarm:
        print("On position: ", c1.position, " Alarm commited")
        c1.alarmDate = datetime.datetime.now()
        f = open("CameraAlarms.txt", "w")
        f.write("Date of alarm commited" + str(c1.alarmDate))
        f.close()
        print("Alarm date saved to file")
    if c1.isErrorCode:
        print("Code: ", c1.errorcode, " Error code commited")
        f = open("CameraErrorCodes.txt", "w")
        f.write("Error code: " + str(c1.errorcode))
        f.close()
        print("Error code saved to file")
    if c1.disconnectPowerSupply(c1):
        break

    downloadDataFromCameras(duration_seconds=4, output_folder='./VideosFromCameras', i = i)
    i += 1



