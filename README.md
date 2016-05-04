# arduino-rt-chart
arduino-rt-chart realtime charts with arduino, on webapp.

Using (chart.js)[https://github.com/chartjs/Chart.js] and (jquery)[https://github.com/jquery/jquery]

start the webserver with:

`$ ./startWebServer [port]`
 
to record from the serial port

`$ python2 serial2file.py [serialport] [module]`
 
the serial port probably for arduino /dev/ttyUSB0.... you can also check on the arduino, when you choose the port 

the module defines the name of the file to record ... it will have the name: module.dat

to open the webserver open in your browser the page: [http://localhost:8000/](http://localhost:8000/) 
you will see 4 charts, built from the data of example.dat .

[FAQ](#FAQ)

### FAQ

* I cant find the serial port of my arduino?

after plugging the USB to your arduino, check with dmesg, which port it connect
`$ dmesg`
 
You should get something like this:

`[ XXXX.XXXX] usb 2-1.3: FTDI USB Serial Device converter now attached to ttyUSB0`

that means your serial port is /dev/ttyUSB0

or else you can also check with

`$ ls /dev`

* What is the module? 




