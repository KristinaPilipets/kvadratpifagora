from modul import*
a=input("Siseta sinu sünnidaatum (pp.kk.aaaa) >>> ")
if len(a)==10:
	ans=kontrool(a)
	if ans==True:
		pifagor(a)
	else:
		print("Vale sünnidaatum proovi uuesti")
else:
	print("Vale sünnidaatum")
