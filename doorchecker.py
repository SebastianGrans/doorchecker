
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

	def get_status():
		# Establish a serial connection with the Arduino.  
		# Change '/dev/ttyACM0' to whatever is appropriate.
		ser = serial.Serial('/dev/ttyACM0',9600)

		# The arduino resets every time a serial connection is established and the
		# following is somewhat of a workaround. 
		# Reset can be disabled by placing a 120 ohm resistor between reset and gnd.
		#
		# The workaround is that we wait for the Arduino to reset, and to send a sign 
		# of life. Then we send it an arbitrary char to let it know that we are able
		# recieve. 
		 
		x = ser.readline()
		ser.write(b'A')

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
			write_to_file(newStatus)
			oldStatus = newStatus
		else:
			pass
		sleep(60)

if __name__ == '__main__':
	main()
