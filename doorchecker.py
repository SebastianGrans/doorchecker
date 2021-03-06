#!/usr/bin/env python3
def main():
	from time import sleep
	from datetime import datetime
	import os
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
					 <p>" + str(var) + "</p>\
					 </body>\
					 </html>")
		except Exception as e:
			raise e
		finally:
			f.close()
			print("Successfully updated the file.")

	def get_status():
		print("Opening connection... ", end="")
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

		# Sends an 'x' to the arduino which will reset, and respond with "I'm alive"
		# If serial-reset is not an issue, the next three rows can be commented.
		# On the other hand, leaving it as is should not affect the behaviour.
		ser.write(b'x') 
		status = ser.readline().decode('utf-8') # The Arduino sends data in bytes,
												# so we decode into utf-8
		print("Arduino respons: ", status)


		print("Sending data request... ", end="")
		# Send an 'x', and the arduino respons with switch status.
		ser.write(b'x')
		status = ser.readline().decode('utf-8')
		print("Data rasponse: ", status.rstrip())


		ser.close()
		return status

	def write_raw_data(status):
		"""Skriver ner timestamps i filer som är döpta efter dagen
		   som timestampen togs, dessa filer kan sedan återfinnas
		   i en mappstruktur som ser ut så här: 
		   		ÅR -> MÅNAD -> DAG.txt
		"""
		date = datetime.now().date().__str__().split("-")
		directory = os.path.join(date[0] + "/" + date[1])
		filePath = date[0] + "/" + date[1] + "/" + date[2] + ".txt"
		
		if not os.path.exists(directory):
			os.makedirs(directory)
		try:
			f = open(filePath, "a")
		except:
			print("New month")
		finally:
			f = open(filePath, "a")
			f.write(str(status) + ", " + datetime.now().time().__str__().split(".")[0] + "\n")
			f.close()

	while True:
		try:
			newStatus = str(get_status())
		except Exception as e:
			print("Problem with getting the status from the arduino")
			raise e
		if oldStatus != newStatus:
			print("Status has changed, trying to update the file", end="... ")
			if newStatus.rstrip() == "1":
				status = 1
			else:
				status = 0				
			write_to_file(status)
			write_raw_data(status)
			oldStatus = newStatus
		else:
			pass
		sleep(10) # Update frequency. Change this to whatever suits your needs.

if __name__ == '__main__':
	main()