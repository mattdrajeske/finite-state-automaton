def machine(string):
	fp = open("machine.fsa")

	alphabet = ""
	startstate = ""
	delta = []

	for line in fp:
		#file's content up until this point
		filecontents = ""
		filecontents += line

		if(line[0] == 'A'):
			alphabet = line[2:]
			print(alphabet)
		if(line[0] == 'B'):
			start_state = line[2:]
			print(start_state)
		if(line[0] == 'T'):

		if(line[0] == 'D'):
			delta.append([line])
			print(delta)


	fp.close()

machine('aaab')