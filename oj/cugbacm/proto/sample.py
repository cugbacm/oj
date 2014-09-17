#导入生成的py包
import  contest_submit_pb2

#声明一个变量是ContestSubmit
contest_submit = contest_submit_pb2.ContestSubmit()

#赋值
contest_submit.id = 1111111
contest_submit.timestamp = 111100

#将proto buffer转换成一个字符串
proto_str = contest_submit.SerializeToString()
print proto_str

#声明一个测试的ContestSubmit验证是否能从字符串中解析出来proto
test = contest_submit_pb2.ContestSubmit()

#解析的api
test.ParseFromString(proto_str)

#验证一下是否输出了1111111 111100
print test.id
print test.timestamp
