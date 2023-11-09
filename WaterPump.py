from WaterpumpController import Controller as WaterController
import datetime

c1 = WaterController
c1.__init__(c1, False)
c1.alarm = True
c1.errorcode = 123
c1.isErrorCode = True

while True:
    if c1.alarm:
        print("Alarm commited")
        c1.alarmDate = datetime.datetime.now()
        f = open("WaterpumpAlarms.txt", "w")
        f.write("Date of alarm commited " + str(c1.alarmDate))
        f.close()
        print("Alarm date saved to file")


    if c1.isErrorCode:
        print("Code: ", c1.errorcode, " Error code commited")
        f = open("WaterpumpErrorCodes.txt", "w")
        f.write("Error code: " + str(c1.errorcode))
        f.close()
        print("Error code saved to file")

    # c1.switchOnThePump(c1)
    # if c1.disconnectPowerSupply(c1):
    #     break                                 mozna tak
    # c1.switchOffThePump(c1)
    #                                           lub tak:

    c1.switchOnThePumpByDate(c1, 10)