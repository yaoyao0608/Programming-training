# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))
#方案1
# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print ("The input file is %d bytes long" % len(indata))
print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print ("Alright, all done.")

out_file.close()
in_file.close()


#方案2

#indata = open(from_file).read()
#open(to_file,'w').write(indata)

#方案3
#open(to_file,'w').write(open(from_file).read())