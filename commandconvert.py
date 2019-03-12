import sys
def convert(x):
	try:
		x = int(x);
	except:
		try:
			x =float(x);
		except:
			x = x;
	return x;

sys.argv= list(map(convert, sys.argv));
print(sys.argv);
