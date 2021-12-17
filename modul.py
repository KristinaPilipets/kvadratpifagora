from datetime import*

k=""
v=""
resultat={}
with open("result.txt","r",encoding='utf8') as f: # encoding - найденно в интернете так как была проблема из-за текста на русском
	for i in f:
		k,v=i.strip().split("-")
		resultat[k.strip()]=v.strip()

def kontrool(a)->bool:
	if a[0:2].isdigit()==True and a[3:5].isdigit()==True and a[6:10].isdigit()==True:
		d=int(a[0:2])
		m=int(a[3:5])
		y=int(a[6:10])
		print(d,m,y)
		if date(y,m,d) is not None:
			data=True
		else:
			data=False
	else:
		data=False
	return data

def pifagor(a):
	d=a[0:2]
	m=a[3:5]
	y=a[6:10]
	dy=int(a[0])+int(a[1])+int(a[3])+int(a[4])
	year=int(a[7])+int(a[8])+int(a[9])+int(a[-1])
	first=dy+year
	first=str(first)
	second=int(first[0])+int(first[1])
	third=int(first)-2*int(a[0:2])
	third=str(abs(third))
	fourth=int(third[0])+int(third[-1])
	firstrow=(d+m+y)
	secondrow=(str(first)+str(second)+str(third)+str(fourth))
	listid=list(firstrow+secondrow)
	listid=[int(x) for x in listid]
	print(listid)
	count={}
	for i in range(1,10):
		a=listid.count(i)
		if a==0:
			a="нет "+str(i)
		count.update({i:a})
	print(count.items())
	for keys,values in count.items():
		if type(values)==int:
			a=str(keys)*int(values)
		else:
			a=values
		b=resultat.get(a)
		print(a+" - "+b)