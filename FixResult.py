import os
path=input("please enter the path of your result.csv:")
f=open(path)
warp=f.readlines()
f.close()
t=0
tk=0
with open("/storage/emulated/0/re.txt" , "w") as f2:
				    f2.close()
just=input("""
1-just ip(enter 1)
2-hiddify warp(enter2)

>:""")
while just != "1" and just  !="2":
	print("bad code")
	just=input("""
1-just ip(enter 1)
2-hiddify warp(enter2)""")
if just == "2":
	for i in range(1, len(warp)-1):
		if t ==1:
			with open("/storage/emulated/0/re.txt" , "a") as f2:
				    f2.write("warp://")
			for k in warp[i]:
				if k ==",":
				
					print(tk, "ip found")
					with open("/storage/emulated/0/re.txt" , 	"a") as f2:
					    f2.write("/?ifp=10-20")
					    f2.write("\n")
				    
					tk=tk +1
					break
			
				with open("/storage/emulated/0/re.txt" , "a") as f2:
			    
				    f2.write(k)
		    

		t=1

if just == "1":
		for i in range(1, len(warp)-1):
			
			if t ==1:
			
				for k in warp[i]:
					
					if k ==",":
					 	 	with open("/storage/emulated/0/re.txt" , "a") as f2:
					 	 		f2.write("\n")
					 	 	tk=tk +1
					 	 	print(tk, "ip found")
					 	 	break
					with open("/storage/emulated/0/re.txt" , "a") as f2:
					 	f2.write(k)
			t=1
print("finished")
