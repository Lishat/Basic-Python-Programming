dicti = {"Name": "Subhadeep", "Year" : 1, "Batch":"A", "Roll No.":201601021};
dicto = {"Name": "Rathan", "Year": 1, "Batch":"B", "Roll No.":201601104};
#print("cmp(dicti, dicto) is", cmp(dicti, dicto)); #works in python2
print("len(dicti) is", len(dicti));
print("str(dicti) is", str(dicti));
print("type(dicti) is", type(dicti));
dicto.clear();
print("dicto.clear(), Updated Dicto:", dicto);
dicto = dicti.copy();
print("dicto = dicti.copy(), Updated Dicto:", dicto);
seq = ('Name', 'Class');
dicto.clear();
dicto = dicto.fromkeys(seq,10)
print("dicto.clear(),dicto = dicto.fromkeys(seq,10), dicto is", dicto); 
print("dicti.get('How', 'Not available') is", dicti.get('How', 'Not available'));
#print("dicti.has_key('Name') is", dicti.has_key('Name')); #works in python2
print("dicti.items() is", dicti.items());#in python3 dicti_items is printed before the desired tuple
print("dicti.keys() is", dicti.keys())
print("dicti.setdefault('Name') is", dicti.setdefault('Name'));
dicto.clear();
dicto={"Place":"Hyderabad", "Native": "Odisha"}
dicti.update(dicto)
print("dicti.update(dicto), Updated dicti is", dicti);
print("dicti.values() is", dicti.values());#in python3 dicti_values is printed before the desired tuple
