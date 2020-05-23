'''NEO cipher'''
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 '
def cipher(word, key):
	newword = ''
	for x in word:
		newword += alpha[(alpha.find(x) + key) % len(alpha)]
	return newword
def decipher(word, key):
	newword = ''
	for x in word:
		newword += alpha[(alpha.find(x) - key) % len(alpha)]
	return newword