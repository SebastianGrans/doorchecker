#!/usr/bin/env python3
def main():
	from time import sleep
	import serial

	oldStatus = False
	newStatus = False

	def write_to_file(var):
		try:
			f = open("index.html", "w")
			f.write("<html>\
					 <head>\
					 <meta charset=\"utf-8\">\
					 <title></title>\
					 <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\
					 </head>\
					 <body>\
					 <p>" + var + "</p>\
					 </body>\
					 </html>")
		except Exception as e:
			raise e
		finally:
			f.close()
			print("We succeeded in writing a new file.")

	def get_status():
		print("I'm gonna try talk to the arduino now...")
		# Establish a serial connection with the Arduino.  
		# Change '/dev/ttyACM0' to whatever is appropriate.
		ser = serial.Serial('/dev/ttyUSB0',9600)

		'''
		Depending on your setup, the arduino will reset on a new serial connection
		and it will take some time before the Arduino is ready to recieve messages.
		Therefore we must wait some time (0.2 seconds worked good for me. 0.1 caused 
		weird behavior.) and then send the data.

		Sending a character 'x' will cause the arduino to return the sensor value.
		1 if the reed switch is open, 0 closed. 

		'''

		sleep(0.2)
		ser.write(b'x')

		# The Arduino sends data in bytes, so we decode into utf-8
		status = ser.readline().decode('utf-8')
		ser.close();
		return status

	while True:
		try:
			newStatus = str(get_status())
		except Exception as e:
			raise e
		if oldStatus != newStatus:
			if newStatus.rstrip() == "1":
				status = 1
			else:
				status = 0				
			write_to_file(status)
			oldStatus = newStatus
		else:
			pass
		sleep(60)

if __name__ == '__main__':
	main()
