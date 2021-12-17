from modul import*
while True:
	ext=input("Välja - 1, jätkama- 2 >>> ")
	if ext=="1":
		break
	elif ext=="2":
		a=input("Siseta sinu sünnidaatum (pp.kk.aaaa) >>> ")
		if len(a)==10:
			ans=kontrool(a)
			if ans==True:
				pifagor(a)
			else:
				print("Vale sünnidaatum proovi uuesti")
		else:
			print("Vale sünnidaatum")
	else:
		print("See funktsioon ei ole")
