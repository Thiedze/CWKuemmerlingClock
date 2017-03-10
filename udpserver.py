import socket

class UdpServer():

	def __init__(self, clock):
		self.clock = clock
		
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.bind(("", 5050))

	def run(self):
		while True:
			data, addr = self.socket.recvfrom(1024)
			split = data.split(":")
			if len(split) == 2:
				if split[0] == "mode":
					clock.setMode(int(split[1]))
				else:
					rgbColor = split[1].split(",")
					rgbColor = map(int, rgbColor)
					if split[0] == "seconds":
						self.clock.setColorSeconds(rgbColor)
					elif split[0] == "minutes":
						self.clock.setColorMinutes(rgbColor)
					elif split[0] == "hours":
						self.clock.setColorHours(rgbColor)

