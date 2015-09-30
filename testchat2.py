import socket, select, string
import sys
import fte
import fteproxy
from recorded_data import *

'''

PornProxy is a free software you could redistribute it and/or modify it under the terms of the 

GNU General Public License as published by the Free Software Foundation either version 3.0 of the License or any later version.

PornProxy is free of charge but we accept donations(it would help if you donated both 

to flipchan and the Free Software Foundation).

PornProxy is distributed  in the hope that it will be useful, but WITHOUT ANY WARRANTY : 

without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 

PARTICULAR PURPOSE see the GNU General Public License along with PornProxy. if not see <http://www.gnu.org/licenses>.

__author__ = "Filip kalebo"

__copyright__ = "Free Software Foundation"

__license__ = "GPL"

__version__ = "3.0"

__maintainer__ = "Filip kalebo"

__email__ = "flipchan@riseup.net"

__status__ = "Project is in beta not done"

'''

#fte configs
client_server_regex = '^(0|1)+$'
server_client_regex = '^(A|B)+$'

#User-agent for porn data
#Mozilla running on kali
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"


def prompt() :
	sys.stdout.write('' + nickname)
	sys.stdout.flush()

if __name__ == "__main__":
	
	if(len(sys.argv) < 4) :
		print'Fte chatclient for PornProxy'
		print 'Usage : python telnet.py hostname port nickname'
		sys.exit()
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	nickname = int(sys.argv[3])
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s = fteproxy.wrap_socket(s,
		                 outgoing_regex=client_server_regex,
		                 outgoing_fixed_slice=256,
		                 incoming_regex=server_client_regex,
		                 incoming_fixed_slice=256)	
	s.settimeout(3)
	
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print 'Unable to connect'
		sys.exit()
	
	print 'Connected to remote host. Start sending messages'
	prompt()
	
	while 1:
		socket_list = [sys.stdin, s]
		
		# Get the list sockets which are readable
		read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
		
		for sock in read_sockets:
			#incoming message from remote server
			if sock == s:
				data = sock.recv(4096)
				if not data :
					print '\nDisconnected from chat server'
					sys.exit()
				else :
					#print data
					sys.stdout.write(data)
					prompt()
			
			#user entered a message
			else :
				msg = sys.stdin.readline()
				#send some randome selected p data
				s.send(data0())
				s.send(msg)
				prompt()
