void TestVector(int fartOverX, int listeMedSetebelte[], int listeMedTrykkSensor[], int antallSetePlassarIBilen) {
    //Adding all pins to a singular list
    int listeMedAllePins[];

    for (int i = 0; i < antallSetePlassarIBilen; i++) {
        //For listeMedSetebelte
        listeMedAllePins[i] = listeMedSetebelte[i];
    }

    for (int i = 0; i < antallSetePlassarIBilen; i++) {
        //For listeMedTrykkSensor
        listeMedAllePins[i + antallSetePlassarIBilen] = listeMedTrykkSensor[i];
    }

    listeMedAllePins[antallSetePlassarIBilen * 2 + 1] = fartOverX;
    int numberOfCombinations = pow(2, antallSetePlassarIBilen * 2 + 1);

    byte fart;
    byte trykkSensor;
    byte seteBelte;
    for (int i = 0; i < antallSetePlassarIBilen * 2 + 1; /* Er antall element i listeMedAllePins.(FINST IKKJE size() i arduino?) */ i++) {
        int maske = 1 << i;
        for (int y = 0; y < numberOfCombinations; y++) {
            int mask = maske & y;
            if (mask) {
                digitalWrite(listeMedAllePins[i], HIGH);
                Serial.println("Setting pin: " + listeMedAllePins[i] + " to HIGH");
            }
        }
        if (fart && trykkSensor && !seteBelte) {
            Serial.println("Alarm is on with pins: ");
        }
    }
}

void boardReset(int listeMedAllePins[], int antallSetePlassarIBilen) {
    for (int i = 0; i < antallSetePlassarIBilen * 2 + 1; i++) {
        digitalWrite(i, LOW);
    }
}