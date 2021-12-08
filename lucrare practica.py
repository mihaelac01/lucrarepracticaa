f=open('lista clasei 11 D.txt','r')
linii=list(f)
f.close()
nr=0
med=0
print('Nume', 'Prenume', 'Nota', 'Grupele' ,sep='\t')
m=open('lista clasei 11 D engl1.txt','w')
p=open('lista clasei 11 D engl2.txt','w')
for linie in linii:
	 print(linie.rstrip())
campuri=linie.split()
nota=int(campuri[2])
nr+=1
med+=nota
if campuri[3]=='engl1':
	m.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
	m.write('\n')
if campuri[3]=='engl2':
    p.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
    p.write('\n')
print('Media elevilor este',med/float(nr))
m.close()
p.close()