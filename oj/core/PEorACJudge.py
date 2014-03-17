import filecmp
import defi
def  delnextline(f1):
	f = open(f1,'r')
	strr = f.read()
	return strr.split()
	
def compare(f_one, f_two):
	if filecmp.cmp(f_one,f_two):
		defi.oj_AC = 1
		print "oj_AC"
		return
	elif delnextline(f_one) == delnextline(f_two):
		defi.oj_PE = 1
		print "oj_PE"
		return
	else:
		defi.oj_WA = 1
		print "oj_WA"
		#return oj_WA

path1 = "/home/qianghe/Documents/test/data.out"
path2 = "/home/qianghe/Documents/test/out.txt"

compare(path1, path2)
if defi.oj_WA == 1:
	print "oj_WA"
if defi.oj_PE == 1:
	print "oj_PE"
if defi.oj_AC == 1:
	print "oj_AC"
