#!/usr/bin/python
import socket
import threading

bind_ip= "127.0.0.1"
bind_port = 910

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)
# this is our client-handling thread
def handle_client(client_socket):
	# print out what the client sends
    	request= client_socket.recv(1024)
    	print "[*] Received: %s" % request
	msgString="INTERCEPTED DATA ON FLY\n\n"
    	# send back a packets
	msgAddr=raw_input("DESTINATION  ADDRESS :")
	msgBody=raw_input("MESSAGE SUBJECT:")
	msgLoc=raw_input("MESSAGE BODY :")
	msgString=msgString+"MESSAGE ADDRESS : "+msgAddr+"\nMESSAGE BODY : "+msgBody+"\nDESTINATION : "+msgLoc+"\n"
	client_socket.send(msgString)
	client_socket.close() 
   
while True:
	client,addr = server.accept()
    	print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    	# spin up our client thread to handle incoming data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()
