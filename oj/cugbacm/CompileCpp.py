#!/usr/bin/env python
import pika
import time
import subprocess
import os
import os.path
import defi
import filecmp
import sys
import glob
import time
import MySQLdb

def compileCppPath(id):#receive id
    pass
    path = '/home/cugbacm/Documents/' + id +'/'
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
    f_out = open('/home/cugbacm/Documents/test/ans.out','w')
    #f_err = open('/home/cugbacm/Documents/test/err.out','w')
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
        return '/home/cugbacm/Documents/test/dp.cpp','g++ /home/cugbacm/Documents/test/dp.cpp -o /home/cugbacm/Documents/test/dp'
    if (language == 'c') or (language == 'gcc'):
        return 'program.cc','g++ program.cpp -o program'
    if language == 'java':
        return 'program.java', 'g++ program.cpp -o program'

def main(id, language, program):
    fileProgram = open('/home/cugbacm/Documents/test/dp.cpp','w')
    fileProgram.write(program)
    fileProgram.close()
    filePath,compileFile = makeFilePath(language)
    dirName = compileCppPath(id)
    baseName = glob.glob(dirName + '*')
    for i in range(len(baseName)):
        if isInFile(baseName[i]) != 0:
            path1 = baseName[i]
            compileCpp(compileFile, filePath,path1)
            path2 = baseName[i][0:-3] + '.out'
            compare('/home/cugbacm/Documents/test/ans.out', path2)
            if defi.oj_WA == 1:
                return "oj_WA"
                defi.oj_AC = 0
                break
            if defi.oj_PE == 1:
                return "oj_PE"
                defi.oj_AC = 0
                break
    if defi.oj_AC == 1:
        return 'oj_AC'

'''if __name__ == '__main__':
    program = '#include <iostream>\n using namespace std; int main(){int a,b;cin >> a >> b;cout << a+b << endl;return 0;}'
    main('1000', 'c++', program)'''
'''def callback(ch, method, properties, body):
    print body
    db = MySQLdb.connect(host = "127.0.0.1", port=3306, user = "root", passwd = "cugbacm", db="oj")
    cursor = db.cursor()
    #print "select * from cugbacm_submit where runID = %s" % body
    cursor.execute("select * from cugbacm_submit where runID = '%s'" % body)
    for row in cursor.fetchall():
        print row
        program = '#include <iostream>\n using namespace std; int main(){int a,b;cin >> a >> b;cout << a+b << endl;return 0;}'
        sql = "UPDATE cugbacm_submit SET status='%s' where runID='%s'" % (main('1000', 'c++', row[10]), body)
        #print sql
        cursor.execute(sql)
    #print " [x] Received %r" % (body,)
    db.commit()
    cursor.close()
    db.close()
    ch.basic_ack(delivery_tag = method.delivery_tag)

def Judge():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue', durable=True)
    print ' [*] Waiting for messages. To exit press CTRL+C'
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback, queue='task_queue')
    channel.start_consuming()

Judge()'''

