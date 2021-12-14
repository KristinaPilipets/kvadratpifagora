from modul import*
a=input("Siseta sinu sünnidaatum (pp.kk.aaaa) >>> ")
if len(a)==12:
	ans=kntrool(a)
	if ans=="õige":
		pifagor()
	else:
		print("Vale sünnidaatum proovi uuesti")
else:
	print("Vale sünnidaatum")
