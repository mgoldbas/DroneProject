from dronekit import connect, VehicleMode


def connectMyCopter():
	connection_string = '127.0.0.1:14550'
	vehicle = connect(connection_string, wait_ready=True)
	print(vehicle)


if __name__ == "__main__":
	connectMyCopter()

