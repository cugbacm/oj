import subprocess
import os
import os.path
import defi
import filecmp
import sys
import glob
import time

def compileCppPath(id):#receive id
    pass
    path = '/home/hq/Documents/' + id +'/'
    return path

def isInFile(filePath):#search '.in' file
    pass
    l = len(filePath)
    if (l <= 3) or (filePath[-3:] != '.in'):
        return 0
    else:
        return l - 3

def compileCpp(compileFile, filePath, path1):#compile .cpp
    os.system(compileFile)
    o_file = filePath[0:-4]
    f_in = open(path1,'r');
    f_out = open('/home/hq/Documents/test/ans.out','w')
    startTime = time.clock()
    p = subprocess.Popen(o_file, stdin = f_in, stdout = f_out)
    p.communicate(input=None)
    endTime = time.clock()
    print endTime - startTime


def delnextline(f1): #delete spaces
    f = open(f1,'r')
    strr = f.read()
    return strr.split()

def compare(f_one, f_two):#
    contentOne = file(f_one).read().replace('\r','').rstrip()
    contentTwo = file(f_two).read().replace('\r','').rstrip()
    if contentOne == contentTwo:
        defi.oj_AC = 1
    elif contentOne.split() == contentTwo.split():
        defi.oj_PE = 1
    elif contentTwo in contentOne:
        defi.oj_OL = 1
    else:
        defi.oj_WA = 1

def makeFilePath(language):#make os.system('compileFile') 
    pass
    if (language == 'c++') or (language == 'g++'):
        return '/home/hq/Documents/test/dp.cpp','g++ dp.cpp -o dp'
    if (language == 'c') or (language == 'gcc'):
        return 'program.cc','g++ program.cpp -o program'
    if language == 'java':
        return 'program.java', 'g++ program.cpp -o program'

def main(id, language):
    filePath,compileFile = makeFilePath(language)
    dirName = compileCppPath(id)
    baseName = glob.glob(dirName + '*')
    for i in range(len(baseName)):
        if isInFile(baseName[i]) != 0:
            path1 = baseName[i]
            compileCpp(compileFile, filePath,path1)
            path2 = baseName[i][0:-3] + '.out'
            compare('/home/hq/Documents/test/ans.out', path2)
            if defi.oj_WA == 1:
                print "oj_WA"
                defi.oj_AC = 0
                break
            if defi.oj_PE == 1:
                print "oj_PE"
                defi.oj_AC = 0
                break
    if defi.oj_AC == 1:
        print 'oj_AC'

if __name__ == '__main__':
    main('test', 'c++')
