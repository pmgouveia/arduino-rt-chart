import serial
import sys

## args... which serial? which sensor? 

if len(sys.argv) < 2:
    sys.stderr.write('Utilizacao: python2 serial2file.py /dev/ttyUSBX modulo\n')
    sys.exit(1)
    
ser = serial.Serial(sys.argv[1], 9600)
#try to open all the ports...
while True:
	
	try:
		x = ser.readline()
		# x = x.rstrip()
		sys.stdout.write(x)
		fo = open(sys.argv[2]+".dat", "a+")
		fo.write(x)
		fo.close()
	except Exception:
		print "Excepcao.... "
		pass
	

"""

import serial

fo = open("foo.txt", "wb")
fo.close()
ser = serial.Serial('/dev/ttyUSB0', 9600)
while True:
	print ser.readline()
	
	"""