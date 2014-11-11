from ssdb import SSDB
import sys
#import cugbacm.proto.rank_pb2

ssdb_ip = "127.0.0.1"
ssdb_port = 6666
ssdb = SSDB(host=ssdb_ip, port=ssdb_port)

def GetContestRankListProto(contestID):
  global ssdb
  proto_str = ssdb.get(contestID)
  return proto_str

def SetContestRankListProto(contestID, rank_list_proto_str):
  global ssdb
  try:
    ssdb.set(contestID, rank_list_proto_str)
  except:
    pass
def InsertUserProblemStatus(userID, problemID, status):
  #AC == 1  No_pass = 2 other = 0
  global ssdb
  value = "2"
  if status == "Accepted":
    value = "1"
  st = str(ssdb.get(userID + '\t' + str(problemID)))
  if st == "1":
    return;
  else:
    ssdb.set(userID + '\t' + str(problemID), value)

def GetUserProblem(userID, problemID):
  global ssdb
  st = ssdb.get(userID + '\t' + str(problemID))
  if str(st) != "1" and str(st) != "2":
    return "0"
  else:
    return str(st)

if __name__ == '__main__':
  ssdb = SSDB(host='127.0.0.1', port=6666)
  print GetUserProblem("QQ", 1000)
  ssdb.delete("QQ	1000")

