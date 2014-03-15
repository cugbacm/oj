import subprocess
import os
os.system('g++ -c /home/hq/Documents/test/add.cpp')
os.system('g++ -o /home/hq/Documents/test/add /home/hq/Documents/test/add.o')
p = subprocess.Popen('/home/hq/Documents/test/add',stdin = subprocess.PIPE , stdout = subprocess.PIPE, stderr = subprocess.PIPE)
f = open('/home/hq/Documents/test/add.in')
for strr in f:
	print strr
	p.stdin.write(strr)
	ans = p.stdout.read()
	fout = open('/home/hq/Documents/test/add.out', 'a+')
	fout.write(ans)
	fout.close
	print open('/home/hq/Documents/test/add.out').read()