List = [1, 2, 3, 4, 5]; 
List1 = []; 
sum1=0;
sum1 = sum(List[::2]);
List = List[::2];
List1 = List1 + List;
print (sum1);
print (List1);
