from ssdb import SSDB
import sys
import cugbacm.proto.rank_pb2

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
  status = ssdb.get(userID + "\t" + str(problemID))
  if not status:
    #if there has no data, Insert The result
    try:
      ssdb.set(userID + "\t" + str(problemID), status);
    except:
      pass
  else:
    if status == 1:
        pass#if the problem is AC,Do Nothing
    else:
      #if The problem has problem but the result is not AC
      try:
        ssdb.set(userID + "\t" + str(problemID), status);
      except:
        pass

def GetUserProblem(userID, problemID):
  global ssdb
  status = ssdb.get(userID + "\t" + str(problemID))
  return status

if __name__ == '__main__':
  ssdb = SSDB(host='127.0.0.1', port=6666)
  print ssdb.get("QQ	1000")


