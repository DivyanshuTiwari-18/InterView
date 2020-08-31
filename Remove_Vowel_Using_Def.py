p="aeiouAEOUI"
def remove(s):
	new=""
	for i in s:
		if i in "aeouiAEOUI":
			pass
		else:
			new+=i
	return new				
string=input("Enter String ")
re  = remove(string)
print(re)
