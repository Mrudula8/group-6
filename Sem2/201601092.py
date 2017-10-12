#----------------------CO Assignment--------------------------
#-->Roll number:201601092
def Results(p,l):
	flag=0
	if(p==l):
		flag=1
	return flag
def Input(fin):
	s=""
	l=0
	fp=open(fin)
	p=fp.read()
	p=p.strip()	
	p=p+'^'
	b="^^"
	f="#"
	h=":"
	instructions=[]	
	while(p[l]!='^'):
		if((p[l]!="\n")):
			if(p[l+1]=="^"):
				s=s+p[l]
				instructions.append(s)
				l=l+1
				s=""
			else:
				s=s+p[l]
				l=l+1
		else:
			instructions.append(s)
			l=l+1
			s=""
	instructions.append(b)
	length=len(instructions)
	for j in range(length):
		if(instructions[j]==".text"):
			index=j
			break
	instructions=instructions[index: ]
	o=0
	while(instructions[o]!=b):
		p=len(instructions[o])
		if((instructions[o]=="") or instructions[o][p-1]==h):
			stock=instructions[o]
			instructions.remove(stock)
		elif(instructions[o][0]==f):
			stock=instructions[o]
			instructions.remove(stock)
			if f in instructions[o]:
				for k in range(p):
					if(instructions[o][k]==f):
						instructions[o]=instructions[:k]
						break
		o=o+1		
	instructions.pop()
	for m in range(len(instructions)):
		instructions[m]=instructions[m].strip()
	return instructions
def arrayands(li):
	for j in li:
		if " " in j[0]:
			spl=j[0]
			l=spl.split(" ")
			j[0]=l[0]
			j.insert(1,l[1])
	return li
def Flag(p,li):
	flag=0
	for k in li:
		if p in k:
			flag=1
	return flag
def function(intli):
	s=","
	for i in range(len(intli)):
		if s in intli[i]:
			intli[i]=intli[i].split(',')
		else:
			intli[i]=intli[i].split(' ')
	return intli		
def in_out(li):
	instructions=["sw","lw","lb","sb","bgt","blt","beqz","bne","beq","bge","mfhi","mflo"]
	result=[]
	array=[]
	new=[]
	sets=["bgt","blt","bne","beq","bge"]
	for k in li:
		y=len(k)
		if((y>=2) and (k[0][0]!="j")):
			if((k[0]!="li") and (k[1]!="$v0")):
				if k[0] not in instructions:
					if((k[0]=="sll")):
						array.append('mul')
					elif((k[0]=="srl")):
						array.append('div')
					else:
						array.append(k[0])
					x=k[0]
					k.remove(x)
					result.append(k[0])
					x=k[0]
					k.remove(x)
					order=k
					k=[]
					k.append(array)
					k.append(result)
					k.append(order)
					new.append(k)
					array=[]
					result=[]
				elif k[0] in sets:
					array.append(k[0])
					x=k[0]
					k.remove(x)
					order=[]
					order.append(k[0])
					x=k[0]
					k.remove(x)
					order.append(k[0])
					x=k[0]
					k.remove(x)
					result=k
					k=[]
					k.append(array)
					k.append(result)
					k.append(order)
					new.append(k)
					array=[]
					result=[]	
				elif(k[0]=='mfhi'):
					array.append('move')
					x=k[0]
					k.remove(x)
					result.append(k[0])
					x=k[0]
					k.remove(x)
					order=["hi"]
					k=[]
					k.append(array)
					k.append(result)
					k.append(order)
					new.append(k)
					array=[]
					result=[]
				elif((k[0]=="lw") or (k[0]=="lb")):
					array.append(k[0])
					x=k[0]
					k.remove(x)
					result.append(k[0])
					x=k[0]
					k.remove(x)
					order=k[0].split('(')
					order.remove(order[0])
					order[0]=order[0][ :3]
					k=[]
					k.append(array)
					k.append(result)
					k.append(order)
					new.append(k)
					array=[]
					result=[]
				elif(k[0]=='mflo'):
					array.append('move')
					x=k[0]
					k.remove(x)
					result.append(k[0])
					x=k[0]
					k.remove(x)
					order=["lo"]
					k=[]
					k.append(array)
					k.append(result)
					k.append(order)
					new.append(k)
					array=[]
					result=[]
				elif((k[0]=="beqz")):
					array.append(k[0])
					x=k[0]
					k.remove(x)
					order=[]
					order.append(k[0])
					order.append('0')
					x=k[0]
					k.remove(x)
					result=k
					k=[]
					k.append(array)
					k.append(result)
					k.append(order)
					new.append(k)
					array=[]
					result=[]
				else:
					array.append(k[0])
					x=k[0]
					k.remove(x)
					result.append(k[0])
					x=k[0]
					k.remove(x)
					order=k
					k=[]
					k.append(array)
					k.append(order)
					k.append(result)
					new.append(k)
					array=[]
					result=[]
			elif(k[0]=="slt"):
				order=[]
				array.append('slt')
				x=k[0]
				k.remove(x)
				result.append(k[0])
				x=k[0]
				k.remove(x)
				order=k
				k.append(array)
				k.append(result)
				k.append(order)
				new.append(k)
				array=[]
				result=[]
			elif((k[0]=="li") and (k[1]=="$v0")):
				order=[]
				array.append('addi')
				x=k[0]
				k.remove(x)
				result.append(k[0])
				x=k[0]
				k.remove(x)
				order.append(k[0])
				order.append('$zero')
				k=[]
				k.append(array)
				k.append(result)
				k.append(order)
				new.append(k)
				array=[]
				result=[]
			else:
				pass
		else:
			pass
	return new
def Strings(li):
	s="("
	if s in li[1][0]:
		l=li[1][0].split(s)
		l.remove(l[0])
		length=len(l[0])
		l[0]=l[0][ :length-1]
		li[1][0]=l[0]
	for j in range(len(li[2])):
		if s in li[2][j]:
			l=li[2][j].split(s)
			l.remove(l[0])
			length=len(l[0])
			l[0]=l[0][ :length-1]
			li[2][j]=l[0]
	return li
def ensure(p):
	array={'add':3 , 'sub' :3 ,'bge':1,'move':5 , 'mul':3 ,'lb':4, 'div':3 , 'sw':5 ,'bgt':1,'slt':1, 'beq':1,'lw':4 , 'beqz':1, 'blt':1,'li':1 ,'sb':5,'bne':1,'la':1 ,'mfhi':5,'addi':3,'slti':3,'mult':2}
	return array[p]
def wobpdep_R_after_W(li):
	length=len(li)
	print("RAW dependency without bypassing:")
	for k in range(length-4):
		for l in range(k+1,k+4):
			if ((li[k][1][0] in li[l][2]) or (Flag(li[k][1][0],li[l][2])==1)):
				print("{",li[k][1][0],",",li[l][2],"}","   ","(",k+1,",",l+1,")","->dependent(R_after_W)")
	for i in range(length-4,length-3):
		for j in range(length-3,length):
			if ((li[i][1][0] in li[j][2]) or (Flag(li[i][1][0],li[j][2])==1)):
				print("{",li[i][1][0],",",li[j][2],"}","   ","(",i+1,",",j+1,")","->dependent(R_after_W)")
	for k in range(length-3,length-2):
		for l in range(length-2,length):
			if ((li[k][1][0] in li[l][2]) or (Flag(li[k][1][0],li[l][2])==1)):
				print("{",li[k][1][0],",",li[l][2],"}","   ","(",k+1,",",l+1,")","->dependent(R_after_W)")
	for i in range(length-2,length-1):
		for j in range(length-1,length):
			if ((li[i][1][0] in li[j][2]) or (Flag(li[i][1][0],li[j][2])==1)):
				print("{",li[i][1][0],",",li[j][2],"}","   ","(",i+1,",",j+1,")","->dependent(R_after_W)")
def wobpdep_W_after_W_after_read(li):
	length=len(li)
	for k in range(length-4):
		if((ensure(li[k][0][0])==3) or (ensure(li[k][0][0])==4) or (ensure(li[k][0][0])==5)):
			for l in range(k+1,k+2):
				if ((li[k][1][0]==li[l][1][0]) or (Results(li[k][1][0],li[l][2])==1)):
					print("{",li[k][1][0],",",li[l][1][0],"}","   ","(",k+1,",",l+1,")","->dependent(W_after_W)")
	for i in range(length-4,length-3):
		if((ensure(li[i][0][0])==3) or (ensure(li[i][0][0])==4) or (ensure(li[i][0][0])==5)):
			for j in range(length-3,length-2):
				if ((li[i][1][0]==li[j][1][0]) or (Results(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][1][0],"}","   ","(",i+1,",",j+1,")","->dependent(W_after_W)")
	for k in range(length-3,length-2):
		if((ensure(li[k][0][0])==3) or (ensure(li[k][0][0])==4) or (ensure(li[k][0][0])==5)):
			for l in range(length-2,length-1):
				if ((li[k][1][0]==li[l][1][0]) or (Results(li[k][1][0],li[l][2])==1)):
					print("{",li[k][1][0],",",li[l][1][0],"}","   ","(",k+1,",",l+1,")","->dependent(W_after_W)")	
	for i in range(length-2,length-1):
		if((ensure(li[i][0][0])==3) or (ensure(li[i][0][0])==4) or (ensure(li[i][0][0])==5)):
			for j in range(length-1,length):
				if ((li[i][1][0]==li[j][1][0]) or (Results(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][1][0],"}","   ","(",i+1,",",j+1,")","->dependent(W_after_W)")
def wobpdep_W_after_R(li):
	length=len(li)
	for k in range(length-4):
		for l in range(k+1,k+4):
			if ((li[l][1][0] in li[k][2]) or (Flag(li[l][1][0],li[k][2])==1)):
				print("{",li[l][1][0],",",li[k][2],"}","   ","(",l+1,",",k+1,")","->dependent(W_after_R)")
	for i in range(length-4,length-3):
		for j in range(length-3,length):
			if ((li[j][1][0] in li[i][2]) or (Flag(li[j][1][0],li[i][2])==1)):
				print("{",li[j][1][0],",",li[i][2],"}","   ","(",j+1,",",i+1,")","->dependent(W_after_R)")
	for k in range(length-3,length-2):
		for l in range(length-2,length):
			if ((li[l][1][0] in li[k][2]) or (Flag(li[l][1][0],li[k][2])==1)):
				print("{",li[l][1][0],",",li[k][2],"}","   ","(",l+1,",",k+1,")","->dependent(W_after_R)")
	for i in range(length-2,length-1):
		for j in range(length-1,length):
			if ((li[j][1][0] in li[i][2]) or (Flag(li[j][1][0],li[i][2])==1)):
				print("{",li[j][1][0],",",li[i][2],"}","   ","(",j+1,",",i+1,")","->dependent(W_after_R)")
def wbpdep_R_after_W(li):
	length=len(li)
	print("RAW dependency with bypassing:")
	for k in range(length-4):
		if((li[k][0][0]=="lw") or (li[k][0][0]=="la")):
			for l in range(k+1,k+2):
				if ((li[k][1][0] in li[l][2]) or (Flag(li[k][1][0],li[l][2])==1)):
					print("{",li[k][1][0],",",li[l][2],"}","   ","(",k+1,",",l+1,")","->dependent(R_after_W)")	
		elif((li[k][0][0]=="sw") or (li[k][0][0]=="sb") or (li[k][0][0]=="move")):
			for j in range(k+1,k+3):
				if ((li[k][1][0] in li[j][2]) or (Flag(li[k][1][0],li[j][2])==1)):
					print("{",li[k][1][0],",",li[j][2],"}","   ","(",k+1,",",j+1,")","->dependent(R_after_W)")
	for i in range(length-4,length-3):
		if((li[i][0][0]=="lw") or (li[i][0][0]=="la")):
			for j in range(length-3,length-2):
				if ((li[i][1][0] in li[j][2]) or (Flag(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][2],"}","   ","(",i+1,",",j+1,")","->dependent(R_after_W)")	
		elif((li[i][0][0]=="sw") or (li[i][0][0]=="sb") or (li[i][0][0]=="move")):
			for j in range(length-3,length-1):
				if ((li[i][1][0] in li[j][2]) or (Flag(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][2],"}","   ","(",i+1,",",j+1,")","->dependent(R_after_W)")
	for k in range(length-3,length-2):
		if((li[k][0][0]=="lw") or (li[k][0][0]=="la")):
			for l in range(length-2,length-1):
				if ((li[k][1][0] in li[l][2]) or (Flag(li[k][1][0],li[l][2])==1)):
					print("{",li[k][1][0],",",li[k][2],"}","   ","(",k+1,",",l+1,")","->dependent(R_after_W)")	
		elif((li[k][0][0]=="sw") or (li[k][0][0]=="sb") or (li[k][0][0]=="move")):
			for j in range(length-2,length):
				if ((li[k][1][0] in li[j][2]) or (Flag(li[k][1][0],li[j][2])==1)):
					print("{",li[k][1][0],",",li[j][2],"}","   ","(",k+1,",",j+1,")","->dependent(R_after_W)")	
	for i in range(length-2,length-1):
		if((li[i][0][0]=="lw") or (li[i][0][0]=="la")):
			for j in range(length-1,length):
				if ((li[i][1][0] in li[j][2]) or (Flag(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][2],"}","   ","(",i+1,",",j+1,")","->dependent(R_after_W)")	
		elif((li[i][0][0]=="sw") or (li[i][0][0]=="sb") or (li[i][0][0]=="move")):
			for j in range(length-1,length):
				if ((li[i][1][0] in li[j][2]) or (Flag(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][2],"}","   ","(",i+1,",",j+1,")","->dependent(R_after_W)")	
def wobpdep_W_after_W_before_read(li):
	length=len(li)
	for i in range(length-4):
		if((ensure(li[i][0][0])==3) or (ensure(li[i][0][0])==4) or (ensure(li[i][0][0])==5)):
			for j in range(i+1,i+4):
				if ((li[i][1][0]==li[j][1][0]) or (Results(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][1][0],"}","   ","(",i+1,",",j+1,")","->dependent(W_after_W)")
	for k in range(length-4,length-3):
		if((ensure(li[k][0][0])==3) or (ensure(li[k][0][0])==4) or (ensure(li[k][0][0])==5)):
			for l in range(length-3,length):
				if ((li[k][1][0]==li[l][1][0]) or (Results(li[k][1][0],li[l][2])==1)):
					print("{",li[k][1][0],",",li[l][1][0],"}","   ","(",k+1,",",l+1,")","->dependent(W_after_W)")
	for i in range(length-3,length-2):
		if((ensure(li[i][0][0])==3) or (ensure(li[i][0][0])==4) or (ensure(li[i][0][0])==5)):
			for j in range(length-2,length):
				if ((li[i][1][0]==li[j][1][0]) or (Results(li[i][1][0],li[j][2])==1)):
					print("{",li[i][1][0],",",li[j][1][0],"}","   ","(",i+1,",",j+1,")","->dependent(W_after_W)")
	for k in range(length-2,length-1):
		if((ensure(li[k][0][0])==3) or (ensure(li[k][0][0])==4) or (ensure(li[k][0][0])==5)):
			for l in range(length-1,length):
				if ((li[k][1][0]==li[l][1][0]) or (Results(li[k][1][0],li[l][2])==1)):
					print("{",li[k][1][0],",",li[l][1][0],"}","   ","(",k+1,",",l+1,")","->dependent(W_after_W)")				
def main():
	inputlist=Input("w.asm")
	s="#"
	for j in range(len(inputlist)):
		if s in inputlist[j]:
			inputlist[j]=""
	put=function(inputlist)
	put.remove(['.text'])
	for k in put:
		if(k==[]):
			put.remove([])
	for y in put:
		if(y==['syscall']):
			put.remove(y)
	get=arrayands(put)
	array=in_out(get)
	print("The instructions are:")
	for p in range(len(array)):
		array[p]=Strings(array[p])
	for i in range(len(array)):
		print(array[i]," ->> ",i+1)
	print("\n")
	wobpdep_R_after_W(array)
	print("\n")
	wbpdep_R_after_W(array)
	print("\n")
	print("WAW dependency without bypassing:")
	wobpdep_W_after_W_before_read(array)
main()
