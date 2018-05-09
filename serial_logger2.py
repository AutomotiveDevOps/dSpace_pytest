import serial

import datetime

try:
    datafile = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat().replace(":","_")+".dat2"
	while True:
		with serial.Serial(port="COM5", baudrate=115200) as ser:
			packet = ser.read_until(terminator=b'\x04')
			with open("data.dat", "wb") as fid:
                fid.write(datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat().encode("UTF-8"))
				fid.write(packet)
except KeyboardInterrupt:
	pass
except:
	raise
    
# git remote get-url origin | sed "s/https:\/\//git@/" | sed "s/\.com\//.com:/
# git remote set-url --push origin