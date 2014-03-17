import subprocess
import os
#os.system('g++ /home/qianghe/Documents/test/dp.cpp -o /home/qianghe/Documents/test/dp')
os.system('g++ -c /home/qianghe/Documents/test/dp.cpp')
os.system('g++ -o /home/qianghe/Documents/test/dp /home/qianghe/Documents/test/dp.o')
fin = open('/home/qianghe/Documents/test/data.in', 'r')
fout = open('/home/qianghe/Documents/test/data.out', 'w')
p = subprocess.Popen('/home/qianghe/Documents/test/dp', stdin = fin, stdout = fout, stderr = subprocess.PIPE)
fout.close()
f = open('/home/qianghe/Documents/test/data.out','r')
print f.read()

f.close()
