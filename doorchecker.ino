
// Change this to whatever pin you are using for the magnetic reed switch.
int door = 8;

void setup() {
	Serial.begin(9600);
	pinMode(door, INPUT);

	/* As I mention in the python script, the Arduino resets on new serial
		connections so the following tells the Python script that the Arduino 
		has fully returned from reset. */ 
	Serial.println("I'm alive!");
}

// the loop function runs over and over again forever
void loop() {

	/* When the python script has successfully sent something to the arduino,
		we enter this if-statement */
	if(Serial.available() > 0) {
    	Serial.println(digitalRead(door));
    	Serial.end();
    	delay(100);
	}
}
