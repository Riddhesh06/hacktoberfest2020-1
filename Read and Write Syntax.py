a = open("gui.txt",'r')
b = a.read()
print(b)

w = "abc"
a = open("gui.txt",'w')
b = a.write(f"{w}")

a = open("gui.txt",'r')
b = a.read()
print(b)
