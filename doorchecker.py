#!/usr/bin/python3
import serial

% Establish a serial connection with the Arduino.  
% Change '/dev/ttyACM0' to whatever is appropriate.
ser = serial.Serial('/dev/ttyACM0',9600)

% The arduino resets every time a serial connection is established and the
% following is somewhat of a workaround. 
% Reset can be disabled by placing a 120 ohm resistor between reset and gnd.
%
% The workaround is that we wait for the Arduino to reset, and to send a sign 
% of life. Then we send it an arbitrary char to let it know that we are able
% recieve. 
 
x = ser.readline()
ser.write(b'A')

% The Arduino sends data in bytes, so we decode into utf-8
print(ser.readline().decode('utf-8'),end='')
ser.close();

