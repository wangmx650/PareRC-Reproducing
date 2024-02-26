import os

filepath=os.path.realpath(__file__)
script_dir = os.path.dirname(os.path.normpath(filepath))
home_dir = os.path.dirname(os.path.normpath(script_dir))
conf_dir = home_dir+"/conf"
CONF = conf_dir+"/sysSetting.xml"

f = open(CONF)
start = False
concactstr = ""
for line in f:
    if line.find("setting") == -1:
        line = line[:-1]
	concactstr += line
res=concactstr.split("<attribute>")

slavelist=[]
fstype=""
for attr in res:
    if attr.find("agents.addr") != -1:
	valuestart=attr.find("<value>")
	valueend=attr.find("</attribute>")
	attrtmp=attr[valuestart:valueend]
	slavestmp=attrtmp.split("<value>")
	for slaveentry in slavestmp:
	    if slaveentry.find("</value>") != -1:
		entrysplit=slaveentry.split("<")
		slave=entrysplit[0]
		slavelist.append(slave)
    if attr.find("fullnode.addr") != -1:
        valuestart=attr.find("<value>")
        valueend=attr.find("</attribute>")
	attrtmp=attr[valuestart:valueend]
	slavestmp=attrtmp.split("<value>")
        for slaveentry in slavestmp:
            if slaveentry.find("</value>") != -1:
	        entrysplit=slaveentry.split("<")
 		slave=entrysplit[0]
		slavelist.append(slave)

# stop

print "stop coordinator"
os.system("redis-cli flushall")
os.system("killall DistCoordinator")

for slave in slavelist:
    print "stop slave on " + slave
    os.system("ssh " + slave + " \"killall DistAgent \"")
    os.system("ssh " + slave + " \"redis-cli flushall \"")
