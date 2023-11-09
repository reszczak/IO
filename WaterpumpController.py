import datetime
import time


class Controller:
    errorcode = 0
    alarm = False
    isErrorCode = False
    isOn = False
    alarmDate = datetime.datetime.now()

    def __init__(self, isOn):
        self.isOn = isOn
    def alarmCommited(self, isThereAlarm):
        self.alarm = isThereAlarm
        print("Alarm commited")

    def errorCodeCommit(self, code):
        self.isErrorCode = True
        self.errorcode = code
        print("Error commited")
    def returnControllerStatus(self):
        controllerList = (self.errorcode, self.alarm, self.isOn)
        return controllerList
    def switchOnThePump(self):
        self.isOn = True
        print("Pump is switched on")
    def switchOffThePump(self):
        self.isOn = False
        print("Pump switched off")
    def switchOnThePumpByDate(self, seconds):
        self.isOn = True
        print("Pump switched on")
        start_time = time.time()
        end_time = start_time + seconds

        while time.time() < end_time:
            if self.disconnectPowerSupply(self):
                self.isOn = False
                print("Pump switched off because of alarm")
                return False
        self.isOn = False
        print("Pump switched off")
    def disconnectPowerSupply(self):
        if self.alarm:
            self.isOn = False
            print("Pump switched off")
            return True
        else:
            return False
