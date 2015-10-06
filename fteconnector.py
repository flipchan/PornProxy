import os
import sys, cmd, commands

print""
print"This scripts help u connect to an fte server "
print"fteproxy server connector "
print"let the proxy begin//flipchan"
print"for more info visit fteproxy.org"
print""
print"Let the connection configz run!"
print""

flipchanserver = {'entertheserverip'}

print"Ftebuilder"
getftebuilder =raw_input("Want to download the ftebuilder?Y/N: ")
print""
connecttoit =raw_input("Do you want to conn3ct to flipchan's fteproxy server or one running on localhost 1/2?: ")
print"if u selected 1 enter your public ip (ipchicken.com)"
print"if u selected 2 enter your local ip"
ipcoonf =raw_input("enter your ip: ")
print"Default client port is 8079"
clientport =raw_input("enter client port: ")
print"Default server port is 8080"
serverport =raw_input("Enter server's port: ")
print"default proxy port is 8081"
proxyport =raw_input("Enter the proxy port: ")
print""
startserver =raw_input("Do you want to start an fteproxy server on localhost Y/N: ")
print""

if startserver=="Y":
    startlocal()
    


if getftebuilder=="Y":
    os.system("git clone https://github.com/kpdyer/fteproxy-builder.git")
    print"Ftebuiler downloaded "
    print"installing ftebuilder"
    os.system("cd fteproxy-builder")
    os.system("make all")
    print"done!"
    os.system("cd ..")


if connecttoit=="1":
    print"u selected to connect to flipchans server "
    connecttoflipchan()
    
#connection syntax fteproxy --client_ip $CLIENT_IP --client_port $CLIENT_PORT --server_ip $SERVER_IP --server_port $SERVER_PORT

    
if connecttoflipchan=="2":
    print"u selected to connect to localhost "
    os.system(" " + "" + "")
    connecttolocalhost()
    

    

def connecttoflipchan():
    os.system("fteproxy --client_ip " + ipcoonf + " --client_port " + clientport + " --server_ip " + flipchanserver + " --server_port " + serverport + " ")
    connecttoflipchan()

def connecttolocalhost():
    os.system("fteproxy --cleint_ip " + ipcoonf + " --client_port " + clientport + " --server_ip " + localhost + " --server_port " +  serverport + " ")
    connecttolocalhost()
    
#fteproxy --server_ip $SERVER_IP --server_port $SERVER_PORT --proxy_ip $PROXY_IP --proxy_port $PROXY_PORT
def startlocal():
    os.system("fteproxy --server_ip " + localhost + " --server_port " + serverport + " --proxy_ip " + localhost + " --proxy_port" + proxyport + "")
    startlocal()
    
    
print""
print"Connection successfully configured"
print""