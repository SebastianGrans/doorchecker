

// Change this to whatever pin you are using for the magnetic reed switch.
// Also note that it is perfectly suitable to use analog pins for digital data.
int door = A0; 

void setup() {
	Serial.begin(9600);
	pinMode(door, INPUT);
    digitalWrite(door, HIGH);
}

void loop() {

	/* When the python script has successfully sent something to the arduino,
		we enter this if-statement */
	if(Serial.available()) {
            char command = Serial.read();
            if(command == 'x') {
              Serial.println(!digitalRead(door));
    	      delay(10);
            }
	}
}
