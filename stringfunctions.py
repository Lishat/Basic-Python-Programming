string = 'hello world'
print("string = 'hello world'")
print('string.capitalize() is', string.capitalize())
print('string.center(40, ) is', string.center(40, ))
print("string.count('l', 0, len(string) ) is", string.count('l', 0, len(string)))
#str = "this is string example....wow!!!";
#str = str.encode('base64','strict');
#print "Encoded String: " + str;
#print "Decoded String: " + str.decode('base64','strict') 			works in python2
print("string.endswith('lo', 1, 5) is", string.endswith('lo', 1, 5))
st = "hello \t world"
print("st = 'hello \t world' st.expandtabs(8):",st.expandtabs(8), "st.expandtabs(16):", st.expandtabs(16))
print("string.find('lo', 1, 5) is", string.find('lo', 1, 5))
print("string.index('lo', 1, 5) is", string.index('lo', 1, 5))
print("string.isalnum() is", string.isalnum()) #space exists
print("string.isalpha() is", string.isalpha()) #space exists
print("string.isdigit() is", string.isdigit())
print("string.islower() is", string.islower())
print("string.isnumeric() is", string.isnumeric())
print("string.isspace() is", string.isspace())
print("string.istitle() is", string.istitle()) #all first letters capital
print("string.isupper() is", string.isupper())
string1 = "-"
seq = ("Hello", "world", "How", "are", "you?")
print("string1 = '-'; seq = ('Hello', 'world', 'How', 'are', 'you?'), string1.join(seq) is", string1.join(seq) )
print("len(string) is", len(string))
print("string.ljust(40, 'a') is", string.ljust(40, 'a'))
print("string.lower() is", string.lower())
print("string.lstrip('h') is", string.lstrip('h'))
intab='l';
outtab='8';
print("intab='l',outtab='8', string.translate(string.maketrans(intab, outtab)) is", string.translate(string.maketrans(intab, outtab)))
print("max(string) is", max(string));
print("min(string) is", min(string));
print("string.replace('hello', 'Get Lost', 3) is", string.replace('hello', 'Get Lost', 3));
print("string.rfind('lo', 0, len(string)) is", string.rfind('lo', 0, len(string)));
print("string.rindex('l', 0, len(string)) is", string.rindex('l', 0, len(string)));
print("string.rjust(40, 'a') is", string.rjust(40, 'a'));
print("string.rstrip('d') is", string.rstrip('d'));
stri = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print ("stri.split( ) is", stri.split( ));
print ("stri.split(' ', 1 ) is", stri.split(' ', 1));
print("string.split() is", string.split() );
print("'All is well\nHello World'.splitlines() is", "All is well\nHello World".splitlines());
print("string.startswith('hel') is", string.startswith("hel"))
print("string.strip() is", string.strip())
print("string.swapcase() is", string.swapcase())
print("string.title() is", string.title())
print("string.upper() is", string.upper())
print("string.zfill(22) is", string.zfill(22))
print("string.isdecimal() is", string.isdecimal())
