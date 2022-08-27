import nmap
nm = nmap.PortScanner()
en0 = '192.168.0.110'
lo = '127.0.0.1'
print(nm.scan(lo,'22-443'))
print(nm.scaninfo())
print("all hosts: ",nm.all_hosts())
print("hostname: ",nm[lo].hostname())
print("state: ",nm[lo].state())
print("all protocols: ",nm[lo].all_protocols())
print(nm[lo].keys())
print("hostanem,addr,vendor,status")
print(nm[lo].keys(['hostnames']))
print(nm[lo].keys(['addresses']))
print(nm[lo].keys(['vendor']))
print(nm[lo].keys(['status']))


# print(nm[lo]['tcp'].keys())
# print(nm[lo].has_tcp(22))
# print(nm[lo].has_tcp(23))
# print(nm[lo].all_tcp())
# print(nm[lo]['tcp'][80])
# print(nm[lo].tcp(22))