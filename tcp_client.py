#!/usr/bin/python
import socket
import time
target_host = "127.0.0.1"
target_port = 911
count=0
proceed=0
while proceed == 0:
	# create a socket object
	# AF_INET means we will be using Ip4 address
	# SOCK_STREAM indicates that this will be a TCP client
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# connect the client
	client.connect((target_host,target_port))   
	# send some data
	x=client.send("GET / HTTP/1.1\r\nHost: /computing\r\n\r\n")
	# receive some data
	response = client.recv(4096)
	print response
	count=count+1
    	responseLength=len(response)
	print "Launching Attack for Attempt "+str(count)
	print "Response length = "+str(responseLength)
	time.sleep(0)
        if count == 200 or responseLength > 17:
		proceed=1
		print "found a posible target"
	print "Testing Site "+str(x)
 
    
    
