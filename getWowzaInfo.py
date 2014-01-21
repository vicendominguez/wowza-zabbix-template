#!/bin/env python
# Vicente Dominguez
# -a conn - Global connections
# -a strnum - Global application(streaming) num

import urllib2, base64, sys, getopt
import xml.etree.ElementTree as ET

# Default values
username = "admin"
password = "admin"
host = "localhost"
port = "8086"
getInfo = "None"

##

def Usage ():
        print "Usage: getWowzaInfo.py -u user -p password -h 127.0.0.1 -P 8086 -a [conn|strnum]"
        sys.exit(2)

def getCurrentConnections():
        print xmlroot[0].text

def getCurrentStreams():
        Application =  xmlroot.findall('VHost/Application')
        print len(Application)

def unknown():
        print "unknown"

##




argv = sys.argv[1:]

try :
        opts, args = getopt.getopt(argv, "u:p:h:P:a:")

        # Assign parameters as variables
        for opt, arg in opts :
                if opt == "-u" :
                        username = arg
                if opt == "-p" :
                        password = arg
                if opt == "-h" :
                        host = arg
                if opt == "-P" :
                        port = arg
                if opt == "-a" :
                        getInfo = arg
except :
                usage()

url="http://" + host + ":" + port + "/connectioncounts/"
request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request)
xmlroot = ET.fromstring(result.read())


if ( getInfo == "conn"):
        getCurrentConnections()
elif ( getInfo == "appnum"):
        getCurrentStreams()
else:
        unknown()
        sys.exit(1)


