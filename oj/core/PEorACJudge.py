import filecmp

oj_WA = 0
oj_PE = 0
oj_AC = 0

def  delnextline(f1):
	f = open('/home/qianghe/Documents/test/isInFile.py','r')
	strr = f.read()
	f.close()
	return strr.split()
def compare(f_one, f_two):
	if filecmp.cmp(f_one,f_two):
		print ""
		return
	elif delnextline(f_one) == delnextline(f_two):
		oj_PE = 1
		print "oj_PE"
		return
	else:
		oj_WA = 1
		#return oj_WA

path1 = "/home/qianghe/Documents/test/isInFile.py"
path2 = "/home/qianghe/Documents/test/isinfile.py"

compare(path1, path2)
if oj_WA == 1:
	print "oj_WA"
if oj_PE == 1:
	print "oj_PE"
if oj_AC == 1:
	print "oj_WA"
