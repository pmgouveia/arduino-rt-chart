import serial
import sys
import datetime
from datetime import datetime
## args... which serial? which sensor? 

if len(sys.argv) < 2:
    sys.stderr.write('Utilizacao: python2 serial2file.py /dev/ttyUSBX modulo\n')
    sys.exit(1)
    
arduino = serial.Serial(sys.argv[1], 9600) # abre a porta do arduino

while True:
	agora = datetime.now()
	
	hora = str(agora.hour) + "h" + str(agora.minute) + "m" + str(agora.second) + "s;"
	
	try:
		#ler linha do serial(arduino) e guardar na variavel linhaSerial
		linhaSerial = arduino.readline()
		
		linhaSerial = hora+linhaSerial
        		
		#imprime para o ecra o que recebeu
		sys.stdout.write(linhaSerial) 
		
		# abre o ficheiro para escrever... argv[2] segundo argumento
		ficheiroLog = open(sys.argv[2]+".dat", "a+")
		
		# escreve a linha no ficheiro
		ficheiroLog.write(linhaSerial)
		
		# fecha o ficheiro
		ficheiroLog.close()
		#print "adeus"
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
