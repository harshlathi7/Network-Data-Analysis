def time_to_num(t):
	lnt = len(t) - 3
	n = 0
	e = 1
	while t[lnt]!='=':
		n = e*(ord(t[lnt])-ord('0')) + n
		lnt-=1
		e*=10
	return n

file_name = input()
f = open(file_name)
cnt = sm = 0
l = f.readlines()
ln = len(l)
t_prev = -1
i=2
while i < ln-6:
	if l[i]=="Request timed out.\n":
		t_prev = -1
	else:
		if t_prev==-1:
			j=l[i].split()
			t_prev = time_to_num(j[-2])
		else:
			j=l[i].split()
			t_curr = time_to_num(j[-2])
			cnt+=1
			sm = sm + abs(t_curr - t_prev)
			t_prev = t_curr
	i+=1

print("jitter =",sm/cnt)