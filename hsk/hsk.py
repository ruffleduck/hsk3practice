from json import load
from random import randint, choice
with open('hsk3.json', 'r') as f:
	hsk = load(f)

total = 0
missed = []
while True:
	if randint(0,1) == 0 and len(missed) > 0:
		r = choice(missed)
	else:
		r = randint(0,len(hsk['char'])-1)
	if total > 0:
		print(total - len(missed), '/', total,
			'= {}%'.format(round((total - len(missed)) / total * 100)))
	print(hsk['char'][r])
	input()
	print(hsk['char'][r], hsk['pinyin'][r], hsk['transl'][r])
	if input('correct? [Y/n] ') != '':
		missed.append(r)
	print()
	total += 1