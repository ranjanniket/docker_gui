import os



while True:
	print("Chat with me tell me your requirement: " , end='')
	p = input()

	if (("open" in p) or ("run" in p)) and (("web browser" in p) or ("firefox" in p)):
	  os.system("firefox")
	elif (("open" in p) or ("run" in p)) and (("text editor" in p) or ("gedit" in p)):
	  os.system("gedit")
	elif (("run" in p) or ("open" in p)) and (("jupyter notebook" in p) or ("notebook" in p)):
	  os.system("jupyter notebook --allow-root")
	elif (("open" in p) or ("run" in p)) and (("python3" in p) or ("python" in p)):
	  os.system("python3")
	elif ("exit" in p) or ("quit" in p):
	  break
	else:
 	 print("app not found")


