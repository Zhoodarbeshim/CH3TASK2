words = input("Enter words: ").split()
new_string = ""
words.sort(key = len)
for i in words:
	i = i + " "
	new_string += (str(i))

print()
print(new_string)
print()