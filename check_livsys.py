import os
import platform
from datetime import datetime

net_addr=input('Input network address subnet need to test: ')
net_lst=net_addr.split('.')
net_addr_prexix=net_lst[0]+'.'+net_lst[1]+'.'+net_lst[2]+'.'
start_num=input('Input start number: ')
end_num=input('Input end number: ')
start_IP=net_addr_prexix+start_num
end_IP=net_addr_prexix+end_num
print("Process scanning from IP {} To IP {} starting:".format(start_IP,end_IP))
t1=datetime.now()

os_sys=platform.system()
if(os_sys=='Windows'):
	command='ping -n 1 '
	print('Current System is Window!!!')
else:	
	command='ping -c 1 '
	print('Current System is Linux/Unix!!!')
print("")
for ip_num_end in range(int(start_num),int(end_num)+1):
	ip_addr=net_addr_prexix+str(ip_num_end)
	ping_cmd=command+ip_addr
	response=os.popen(ping_cmd)
	for line in response.readlines():
		if ("TTL=" in line):
			print('IP Address {} is Live'.format(ip_addr))
			break

t2=datetime.now()
print("")
print('Finish scanning in total {}'.format(t2-t1))