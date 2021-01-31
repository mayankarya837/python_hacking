#! /usr/bin/python

# coding a advance port scanner

from socket import *
import optparse #lib prompted for help options
from threading import *

def connscan(tgthost,tgtport) :
	try :
		sock=socket(AF_INET,SOCK_STREAM)
		sock.connect((tgthost,tgtport))
		print '[+] %d /tcp open' %(tgtport)
	except : 
		print '[-] %d /tcp close' %(tgtport)
def hostscan(tgthost,tgtport) :
	try :
		tgtip = gethostbyname(tgthost) #resolve ip addr by name
	except : 
		print "Unknown host %d" % (tgthost)
	try :
		tgtname = gethostbyaddr(tgtip)
		print " [+]scan result for : " +tgtname[0]
	except :
		print " [+] scan res for : " +tgtip
		
	setdefaulttimeout(1)
	
	#for multiple ports
	for port in tgtport :
		t = Thread (target=connscan, args = (tgthost, int(port)))
		t.start()
def main() :
	
	#show commands to user when there is any wrong entry.	
	parser = optparse.OptionParser('use the following pattern : ' + '( -H <target host> -P <target port> )')
	
	#Adding options to our parser
	parser.add_option('-H', dest='tgthost', type='string', help='specify target host')
	parser.add_option('-P', dest='tgtport', type='string', help='specify target port seperaterd by comma')
	
	(options,args) = parser.parse_args() # helps for the exection with args

	#specify our variables
	tgthost = options.tgthost
	tgtport = str(options.tgtport).split(',')
	
	#checking for the valid user input(argument)
	if (tgthost == None) | (tgthost == None) :
		print parser.usage
		exit(0)
	
	hostscan(tgthost,tgtport)
		
if __name__ == '__main__' :
	main()
	 
# syntax ./advportscan.py -H 192.168.1.5 -P 8080

	
 
