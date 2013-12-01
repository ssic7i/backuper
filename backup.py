import os
import subprocess
import sys

line_in = sys.argv

filelist = line_in[1] #file contain list of files
dest_folder = line_in[2]
f = open(filelist, 'r')
list_files = ''
for line in f:
 list_files = list_files + line[0:len(line)-1] + ' '

i = 0
newlist = ''
while i < len(list_files):
 if list_files[i] == '\\':
  newlist = newlist + '/'
 else:
  newlist = newlist + list_files[i]
 i = i+1
 
i = 0
newdest = ''
while i < len(dest_folder):
 if dest_folder[i] == '\\':
  newdest = newdest + '/'
 else:
  newdest = newdest + dest_folder[i]
 i = i+1

#print(newlist)
#print(dest_folder)
#print(newdest)

PIPE = subprocess.PIPE

k = subprocess.Popen('tar -c ' + newlist + '--file=archive.tar', shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
while True:
        s = k.stdout.readline()
        if not s: break
        print s

k = subprocess.Popen('gzip archive.tar', shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
while True:
        s = k.stdout.readline()
        if not s: break
        print s
		
k = subprocess.Popen('copy archive.tar.gz ' + newdest, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
while True:
        s = k.stdout.readline()
        if not s: break
        print s