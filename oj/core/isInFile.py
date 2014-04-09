import glob

def isInFile(filiName):
	l = len(filiName)
	if ((l <= 3) or (filiName[-3:] != '.py')):
		return 0
	else:
		return l - 3

a = glob.glob('/home/qianghe/Documents/test/*')
for i in range(len(a)):
	if isInFile(a[i]) != 0:
		print a[i][ 0 : -3]