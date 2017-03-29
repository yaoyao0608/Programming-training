from sys import argv

script, filename = argv

target = open(filename, 'w')

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

target.close()
