def getWordDict(strLine):

	words = strLine.split()
	d = {}
	for w in words:
		if w in d.keys():
			d[w] += 1
		else:
			d[w] = 1
	return d


def bow(lines):

	bag = {}

	for line in lines:
		d = getWordDict(line)
		for k in d.keys:
			if k in bag.keys():
				

with open('../stof') as stoffile:
	lines = stoffile.readlines()

	for line in 