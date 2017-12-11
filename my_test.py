import re

com = re.compile("jie")

fa = re.findall(com, "My name is chenchuejie,and chenchujie is my name.")

print(fa)

