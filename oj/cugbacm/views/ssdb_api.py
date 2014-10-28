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

if __name__ == '__main__':
  ssdb = SSDB(host='127.0.0.1', port=6666)
  print ssdb.get("1")


