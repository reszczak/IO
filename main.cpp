#include <iostream>
#include <thread>
#include <chrono>

using namespace std;

bool disconnectPowerSupply();
bool alarmsOrErrorCodes();
void locateAlarm();
void returnErrorCode();
void saveDataAboutErrorsAndAlarms();
void downloadDataFromCameras();

int main() {
    while (true) {
        if (disconnectPowerSupply()) {
            return 0;
        }

        downloadDataFromCameras();

        if (alarmsOrErrorCodes()) {
            locateAlarm();
            returnErrorCode();
        }

        saveDataAboutErrorsAndAlarms();
        std::this_thread::sleep_for(std::chrono::hours(24));
    }

    return 0;
}

bool disconnectPowerSupply() {

    return false;
}

void downloadDataFromCameras() {
    cout << "Pobrano dane z kamer." << endl;
}

bool alarmsOrErrorCodes() {

    return true;
}

void locateAlarm() {

    cout << "Zlokalizowano miejsce wystąpienia alertu." << endl;
}

void returnErrorCode() {
    cout << "Zwrócono kod błędu." << endl;
}

void saveDataAboutErrorsAndAlarms() {
    cout << "Zapisano dane o błędach i alertach." << endl;
}