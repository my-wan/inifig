class cfg:
	def keyexist(s,k=''): # If section only ret 2, if [sec]+key found ret 3, else ret 0.
		b=0
		with open(ini,'r')as f:
			for line in f:
				if'['+s+']'in line[:len(s)+2]:b=1
				if b and(k+'=')in line[:len(k)+1]:return 3
				if b>1 and'['in line[:1]:return 2
				if b:b+=1
	def getkeyval(s,k):
		b=0
		with open(ini,'r')as f:
			for line in f:
				if'['+s+']'in line:b=1
				if b and(k+'=')in line[:len(k)+1]:return line[len(k)-len(line)+1:].strip()
				if b>1 and'['in line[:1]:return
				if b:b+=1
	def getsections(f):
		n=0
		list=[]
		with open(f,'r')as f:
			for line in f:
				if'['in line[:1]:n=line.find(']')
				if n:list.append(line[1:n])
				n=0
			return list
	def getkeys(s):
		b=0
		d=[]
		with open(ini,'r')as f:
			for line in f:
				if'['+s+']'in line[:len(s)+2]:b=1
				if b>1 and'['in line[:1]:b=0
				if b>1 and'='in line:
					n=line.find('=')
					if n > -1:d.append({line[:n]})
				if b:b+=1
			return d