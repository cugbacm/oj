#!/usr/bin/env python
# coding=utf-8
# Modified by qiang.he

import shlex, subprocess, os, config, logging, shutil, lorun,shutil, time

class UserSubmit(object):
    """docstring for UserSubmit"""
    solution_id = ""
    problem_id = ""
    language = ""
    user_id = ""
    program = ""
    mem_limit = 0
    time_limit = 0

    def __init__(self, solution_id, problem_id, language, user_id, program,mem_limit,time_limit):
        self.solution_id = solution_id
        self.problem_id = problem_id
        self.language = language
        self.user_id = user_id
        self.program = program
        self.mem_limit = mem_limit
        self.time_limit = time_limit

# 降低程序的执行权限,将程序以nobody用户的身份执行
def low_level():
    try:
        os.setuid(int(os.popen("id -u %s" % "nobody").read()))
    except:
        pass

# dangerous code
def check_dangerous_code(solution_id, language):

  if language in ['python2', 'python3']:
    code = file('/home/cugbacm/Documents/work_dir/%s/main.py' % solution_id).readlines()
    support_modules = [
        're',  # 正则表达式
        'sys',  # sys.stdin
        'string',  # 字符串处理
        'scanf',  # 格式化输入
        'math',  # 数学库
        'cmath',  # 复数数学库
        'decimal',  # 数学库，浮点数
        'numbers',  # 抽象基类
        'fractions',  # 有理数
        'random',  # 随机数
        'itertools',  # 迭代函数
        'functools',
        #Higher order functions and operations on callable objects
        'operator',  # 函数操作
        'readline',  # 读文件
        'json',  # 解析json
        'array',  # 数组
        'sets',  # 集合
        'queue',  # 队列
        'types',  # 判断类型
    ]
    for line in code:
      if line.find('import') >= 0:
        words = line.split() # 以空格隔开单词
        tag = 0
        for w in words:
          if w in support_modules:
            tag = 1
            break
          if tag == 0:
            return False
        return True

  if language in ['gcc', 'g++']:
    try:
      #code = file('hone/work/%s/main.c' % solution_id).read()
      code = file('/home/cugbacm/Documents/work_dir/%s/main.c' % solution_id).read()
    except:
      #code = file('/home/cugbacm/Documents/work_dir/%s/main.cpp' % solution_id).read()
      #code = file('./core/work_dir/%s/main.cpp' % solution_id).read()
      code=file('/home/cugbacm/Documents/work_dir/%s/main.cpp' % solution_id).read()

    if code.find('system') >= 0:
      return False
    return True

# 编译文件
def compile(solution_id, language):
    low_level()
    language = language.lower()   # 将语言变成小写字母
    dir_work = os.path.join(config.work_dir, str(solution_id))
    print "dir_work:",dir_work

    build_cmd = {
      "gcc":"gcc %s/main.c -o %s/main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE" % (dir_work, dir_work),
      "g++": "g++ %s/main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o %s/main" % (dir_work, dir_work),
      "java": "javac %s/Main.java" % dir_work,
      "python2": 'python2 -m py_compile %s/main.py' % dir_work,
      "python3": 'python3 -m py_compile %s/main.py' % dir_work
  }

    if language not in build_cmd.keys():
        print "language is not in build_cmd"
        return False

    p = subprocess.Popen(
        build_cmd[language],
        shell=True,
        cwd=dir_work,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out, err = p.communicate()# 编译错误信息
    err_txt_path = os.path.join(config.work_dir, str(solution_id),'err.txt')
    f = file (err_txt_path, 'w')
    f.write(err)
    f.write(out)
    f.close()

    if p.returncode == 0: # return 0, 编译成功
        return True
    return False

# 判题
def judge(solution_id, problem_id, data_count, time_limit,
        mem_limit, program_info, result_code, language):
    low_level()
    max_men = 0
    max_time = 0
    # 判断编译语言
    if language in ['java', 'python2', 'python3']:
        time_limit = time_limit * 2
        mem_limit = mem_limit * 2
    full_path = os.path.join(config.data_dir, str(problem_id))
    files = os.listdir(full_path)

    for item in files:
        if item.endswith('.in'):
            input_path = "/home/cugbacm/Documents/data_dir/%s/%s"%(str(problem_id),item)
            ret = judge_one_mem_time(solution_id,
          problem_id,
          item,
          time_limit + 10,
          mem_limit,
          language
            )
            if ret == False:
                continue

            if ret['result'] == 5:
                program_info['result'] = result_code['Runtime Error']
                return program_info

            elif ret['result'] == 2:
                program_info['result'] = result_code['Time Limit Exceeded']
                program_info['take_time'] = time_limit + 10
                return program_info

            elif ret['result'] == 3:
                program_info['result']  = result_code['Memory Limit Exceeded']
                program_info['take_memory'] = mem_limit
                return program_info

            if max_time < ret['timeused']:
                max_time = ret['timeused']

            if max_men < ret['memoryused']:
                max_men = ret['memoryused']

            result = judge_result(problem_id, solution_id, item)

            if result == False:
                continue

            if result == 'Wrong Answer' or result == 'Output Limit':
                program_info['result'] = result_code[result]
                break

            elif result == 'Presentation Error':
                program_info['result'] = result_code[result]

            elif result == 'Accepted':
                if program_info['result'] != 'Presentation Error':
                    program_info['result'] = result_code[result]

    program_info['take_time'] = max_time
    program_info['take_memory'] = max_men

    return program_info

def function():
    pass

# 每组数据进行测试
def judge_one_mem_time(solution_id, problem_id, item, time_limit, mem_limit, language):
    low_level()
    input_path = os.path.join(config.data_dir,str(problem_id),"%s" %item)
    try:
        input_data = file(input_path)
    except:
        return False

    out_path = os.path.join(config.work_dir,str(solution_id),'%s'%(item[:-2] + 'txt'))
    temp_out_data = open(out_path, 'w')

    if language == 'java':
        cmd = 'java -cp %s Main' % (os.path.join(config.work_dir, str(solution_id)))
        main_exe = shlex.split(cmd)

    elif language  == 'python2':
        cmd = 'python2 %s' % (os.path.join(config.work_dir, str(solution_id), 'main.pyc'))
        main_exe = shlex.split(cmd)

    elif language == 'python3':
        cmd = 'python3 %s' % (os.path.join(config.work_dir, str(solution_id), '__pycache__/main,cpython-33.pyc'))
        main_exe = shlex.split(cmd)

    else:
        main_exe = [os.path.join(config.work_dir,str(solution_id), 'main')]

    runcfg = {
      'args': main_exe,
      'fd_in': input_data.fileno(),
      'fd_out': temp_out_data.fileno(),
      'timelimit': time_limit,#in MS
      'memorylimit': mem_limit,# in KB
    }

    rst = lorun.run(runcfg)
    input_data.close()
    temp_out_data.close()
    return rst

# 判断结果
def judge_result(problem_id, solution_id, item):
    low_level()
    # logging.debug('Judging result')
    currect_result = os.path.join(config.data_dir, str(problem_id), '%s' % (item[:-2] + 'out'))
    user = os.path.join(config.work_dir, str(solution_id), '%s' % (item[:-2] + 'txt'))
    try:
        curr = file(currect_result).read().replace('\r','')
        curr = curr.strip('\n')
        user_result = file(user).read().replace('\r','')
        user_result = user_result.strip('\n')
        # currLen=len(curr)
        # if curr[currLen-1]=='\n':
        # open(current_result,'w').write(curr[:-1])
        # curr=file(current_result).read().replace('\r','')
        # userLen=len(user_result)
        # if user_result[userLen-1]=='\n':
        # open(user,'w').write(user_result[:-1])
        # user_result=file(user).read().replace('\r','')
    except:
        return False

    if curr == user_result:
        return "Accepted"

    if curr.split() == user_result.split():
        return "Presentation Error"

    if curr in user_result:
        return "Output Limit"

    return "Wrong Answer"

def run(problem_id, solution_id, language, data_count, user_id,time_limit,mem_limit):
    low_level()
    # 获取内存和时间
    # time_limit = 10000
    # mem_limit = 300000
    program_info = {
      'solution_id': solution_id,
      'problem_id': problem_id,
      'take_time': 0,
      'take_memory': 0,
      'user_id': user_id,
      'result': 0,
      'err_explain':0,
    }
    result_code = {
      'In Queuing': 0,
      'Accepted': 1,
      'Time Limit Exceeded': 2,
      'Memory Limit Exceeded': 3,
      'Wrong Answer': 4,
      'Runtime Error': 5,
      'Output Limit': 6,
      'Compile Error': 7,
      'Presentation Error': 8,
      'System Error': 9,
      'Judging': 10
    }
    print "run:check_dangerous_code%s" % check_dangerous_code(solution_id, language)

    if check_dangerous_code(solution_id, language) == False:
        program_info['result'] = result_code["Runtime Error"]
        return program_info
    compile_result = compile(solution_id, language)
    print "run:compile %s" % compile_result
    if compile_result is False:
        program_info['result'] = result_code['Compile Error']
        # clean_work_dir(solution_id)
        return program_info

    if data_count == 0:
        program_info['result'] = result_code['System Error']
        clean_work_dir(solution_id)
        return program_info

    result = judge(
      solution_id,
      problem_id,
      data_count,
      time_limit,
      mem_limit,
      program_info,
      result_code,
      language,
    )
    # clean_work_dir(solution_id)
    return result


# 清空工作目录
def clean_work_dir(solution_id):
    dir_name = os.path.join(config.work_dir, str(solution_id))
    shutil.rmtree(dir_name)

# 得到某道题目的数据总量
def get_data_count(problem_id):
    full_path = os.path.join(config.data_dir, str(problem_id))
    print "full_path:%s" % full_path
    try:
        # listdir获取当前目录中的内容
        files = os.listdir(full_path)
    except OSError as e:
        return 0
    print files
    count = 0
    for item in files:
        if item.endswith('.in'):
            count += 1

    print 'get_data_count excute\n'
    return count

def judge_submit(solution_id, problem_id, language, user_id, program, time_limit, mem_limit):
    re_code = {
        0:'In Queuing',
        1:'Accepted',
        2:'Time Limit Exceeded',
        3:'Memory Limit Exceeded',
        4:'Wrong Answer',
        5:'Runtime Error',
        6:'Output Limit',
        7:'Compile Error',
        8:'Presentation Error',
        9:'System Error',
        10:'Judging'
    }
    print 'main excute\n'
    data_count = get_data_count(problem_id)
    print "data_count:%s", data_count
    path = os.path.join(config.work_dir,'%s' % solution_id)
    print "solution_id path: %s" % path
    if os.path.exists(path):
        # shutil.rmtree删除一个目录
        shutil.rmtree(path)
        # os.makedirs  创建递归的目录树，可以是绝对路径也可以是相对路径
    os.makedirs(path)
    print "solution_id path: %s" % path
    main_path = {
        'gcc': path + '/main.c',
        'g++': path + '/main.cpp',
        'java': path + '/Main.java',
        'python2': path + '/main.py',
        'python3': path + '/main.py'
      }
    open(main_path[language], 'w').write(program)
    result = run(problem_id, solution_id, language, data_count, user_id, time_limit, mem_limit)
    result['result'] = re_code[result['result']]
    result['codeLength'] = os.path.getsize(main_path[language])
    err_path = path + '/err.txt'
    if os.path.exists(err_path):
        if(result['result']=='Compile Error'):
            result['err_explain'] = 'Compile Error:'+file(err_path).read()
        elif(result['result']=='System Error'):
            result['err_explain'] = 'System Error: There is no data for the '+result['problem_id']+' problem'
        elif(result['result']=='Runtime Error'):
            result['err_explain'] = 'Runtime Error: '
        # user_submit.status = re_code[result['result']]
        # user_submit.codeLength = os.path.getsize(main_path)
        # user_submit.runTime =  result['take_time']
        # user_submit.memory = result['take_memory']
        # user_submit.save()

    # lean_work_dir(solution_id)
    return result

    #return run(problem_id, solution_id, language, data_count, user_id)

if __name__ == '__main__':
    program = "#include<iostream> \n  using namespace std; int main(){int  a, b; cin>>a>>b;cout<<a+b<<endl; return 0;}"
    user_submit = UserSubmit(12, 1000, 'g++', '1004101117', program,1000,32562)
    print judge_submit(12, 1000, 'g++', '123', program, 1000, 65536)
