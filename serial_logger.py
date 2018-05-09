import serial

try:
	while True:
		with serial.Serial(port="COM5", baudrate=115200) as ser:
			packet = ser.read_until(terminator=b'\x04')
			with open("data.dat", "wb") as fid:
				fid.write(packet)
except KeyboardInterrupt:
	pass
except:
	raise