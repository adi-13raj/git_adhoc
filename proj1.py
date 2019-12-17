print ("press 1:to create a directory")
print ("press 2:to create a file")
print ("press 3:to check and install any software")
print ("press 4:to make a new user")
print ("press 5:to check current date and time")
print ("press 6:reboot your system")
print ("press 7:to search a keyword on google")
print ("press 8:to play a song in vlc")
print ("press 9:to query for link regarding any keyword")
print ("press 10:update your status on facebook")
print ("press 11:to send a whatsapp message\n")
user=input("please enter your current username[prefer login with root]")
a=int(input("please enter your response : "))

import os
#press 1:
if a==1:
	x=input("please input the directory path[/path/name] to be created : ")
	os.system("mkdir "+x)
	print("your directory has been created in the desired location")
elif a==2:
	x=input("please enter the file name : ")
	os.system("touch "+x)
	print("your file has been created in the present working directory")
elif a==3:
	os.system("touch ftp://192.168.10.254 >> /etc/yum/repos.d/testrepo1")
	x=input("please enter the name of the software you want to install ")
	os.system("sudo yum install "+x)
elif a==4:
	x=input("please enter the username")
	os.system("useradd "+x)
	os.system("passwd "+x)
elif a==5:
	os.system("date")
elif a==6:
	os.system("reboot")
elif a==7:
	x=input("please enter the keyword :")
	import webbrowser
	webbrowser.open("http://www.google.com/search?q="+y)
elif a==8:
	x=input("enter the path of the song to be played")
	os.system("vlc "+x)
	
elif a>=9 and a<=11:
	print("WORK IN PROGRESS")
else:
	print("nothing to do.CAUTION: WRONG INPUT")
