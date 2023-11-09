import datetime
class Controller:
    position = '0'
    errorcode = 0
    alarm = False
    isErrorCode = False
    isOn = True
    alarmDate = datetime.datetime.now()

    def __init__(self, position, isOn):
        self.position = position
        self.isOn = isOn
    def allarmCommited(self, isThereAlarm):
        self.alarm = isThereAlarm
        print("Alarm commited")

    def errorCodeCommit(self, code):
        self.isErrorCode = True
        self.errorcode = code
        print("Error commited")
    def returnControllerStatus(self):
        controllerList = (self.position, self.errorcode, self.alarm, self.isOn)
        return controllerList
    def disconnectPowerSupply(self):
        if self.alarm:
            self.isOn = False
            return True
        else:
            return False
