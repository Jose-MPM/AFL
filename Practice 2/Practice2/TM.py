import json


class TM:

	

	def __init__(self, name):

		try:
			with open(name) as file:
				data = json.loads(open(name).read())
		except Exception as e:
			raise e


		self.states = data["Estados"]
		self.sigma = data["Entrada"]
		self.gamma = data["Cinta"]
		self.i_state = data["Inicial"]
		self.symbol = str(data["Blanco"])
		self.f_state = data["Finales"]
		self.tape = dict()
		self.delta = data["Transiciones"]
		self.valid = False



	def set_delta(self):

		trans = dict()

		for t in self.delta:
			trans.setdefault((t[0], t[1]), (t[2], t[3], t[4]))

		return trans



	def is_valid(self, string):
		for char in string:
			return char not in self.sigma
		
	def load(self, string):

		self.tape.setdefault(0, self.symbol)
		self.tape.setdefault(1, self.i_state)
		self.tape.update(enumerate(string, 2))
		self.tape.setdefault(len(string) + 2, self.symbol)

		return self.tape

	''' Given a state and a symbol, return a tuple with movements'''
	def find_state(self, state, symbol):

		trns = self.set_delta()

		if trns.has_key((state, symbol)):
			return trns.get((state, symbol))
		else:
			return

	def move(self):   #_|q0|010_ ---> _10_ ---> _x|qn|10_
		#valid = False
		reader_head = 1

		self.config(self.tape.values())

		curr_state = self.tape.pop(reader_head)
		sim =  self.tape.pop(reader_head + 1)

		tupl = self.find_state(curr_state, sim)

		while tupl is not None:

			curr_state = tupl[0]
			sim = tupl[1]

			if tupl[2] == 'R':
				self.tape.setdefault(reader_head, sim)
				self.tape.setdefault(reader_head + 1, curr_state)
				reader_head = reader_head + 1

			elif tupl[2] == 'L':	
				temp = self.tape.pop(reader_head - 1)
				self.tape.setdefault(reader_head - 1, curr_state)
				self.tape.setdefault(reader_head + 1, sim)
				self.tape.setdefault(reader_head, temp)
				reader_head = reader_head - 1	

			else:
				self.tape.setdefault(reader_head, curr_state)
				self.tape.setdefault(reader_head + 1, sim)

			#print("".join(self.tape.values()))
			self.config(self.tape.values())

			curr_state = self.tape.pop(reader_head)
			sim =  self.tape.pop(reader_head + 1)
			tupl = self.find_state(curr_state, sim)		
			if curr_state in self.f_state:
				#print("Cadena aceptada")
				self.valid = True
	


	def config(self, values):

		chain = "" 
		
		for i in range(0, len(values) - 1):

			if values[i] in self.states:
				elem = values.pop(i)
				chain += "|" + elem + "|"

			chain += values[i]

		print(chain)
		


name = raw_input("Ingrese el nombre del archivo: ")
m = TM(name)
inp = raw_input("Inserte la cadena de entrada")
#inp = "012"
print(inp ,m.is_valid(inp))
m.load(inp)
m.set_delta()
m.move()
if m.is_valid(inp):
	m.load(inp)
	m.set_delta()
	m.move()
	if m.valid:
		print("Cadena aceptada")
	else:
		print("Cadena rechazada")
else:
	print("Tu cadena ha sido rechazada.")

#print("".join(m.tape.values()))
#m.set_delta()
#m.move()