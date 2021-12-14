def kontrool(a)->str:
	if a[0:2].isdigit()==True and a[3:5].isdigit()==True and a[6:13].isdigit()==True:
		if int(a[0:2]) <=31 and int(a[3:5])<=12 and int(a[6:13]):
			if int(a[3:5])==2:
				if int(a[6:13])<=29:
					ans="õige"
				else:
					ans="vale"
			else:
				ans="õige"
		else:
			ans="vale"
	else:
		ans="vale"
	return ans

def pifagor(a):
	
