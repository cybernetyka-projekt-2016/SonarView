from socketIO_client import SocketIO, LoggingNamespace
import time
import random
import json

# def generate_measurements(quarter):
# 	result = []
# 	for i in range(90*quarter,90*(quarter+1),4):
# 		result.append({i:random.randrange(90, 120, 1)})
# 	result = json.dumps(result)
# 	return result

def print_time():
	millis = int(round(time.time() * 1000))
	print (millis)


with SocketIO('192.168.0.14', 5000, LoggingNamespace) as socketIO:
	print_time()
	for j in range(1,20):
		for i in range(0,359,4):
			val = 0
			if i > 270 or i < 90:
				val = random.randrange(50, 200, 1)
			else:
				val = 0
			socketIO.emit('measurement', {i:val})
			time.sleep(0.1)
	print_time()



	# for i in range(0,4):
	# 	data = generate_measurements(i)
	# 	socketIO.emit('measurement', data)
	# 	print(data)
		# time.sleep(0.05)
#    socketIO.wait()
