import string
import sys
p=raw_input();
for i in p:
	if i == ',':
		c = p.index(',')
	elif i == ')':
		d = p.index(')')

a = int(p[1:c])
b = int(p[c+1:d])
q=raw_input();
for j in q:
	if j == ',':
		g = q.index(',')
	elif i == ')':
		h = q.index(')')

e = int(q[1:g])
f = int(q[g+1:h])
	
if (f-b) > 0 and (e-a) < 0:
	print "%d/%d" %(b-f, a-e);
else:
	print "%d/%d" %(f-b, e-a);


