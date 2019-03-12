List = [1, 2, 3, 4, 5]
List2 = [2, 3, 4, 5, 6]
#print("cmp(List, List2) is", cmp(List, List2)); #works in python2
print("List = [1, 2, 3, 4, 5]");
print("max(List) is", max(List));
print("min(List) is", min(List));
print("len(List) is", len(List));
List = (1, 2, 3, 4, 5)
print("List = (1, 2, 3, 4, 5)");
print("list(List) is", list(List));
List = [1, 2, 3, 4, 5];
print("List = [1, 2, 3, 4, 5]");
List.append(6)
print("List.append(6), Updated list:", List);
print("List.count(4) is", List.count(4));
List.extend(List2)
print("List.extend(List2), Updated list:", List);
print("List.index(4) is", List.index(4));
List.insert(2, 100);
print("List.insert(2, 100), Updated list:", List);
print("List.pop(2) is", List.pop(2));#index is 2
print("Updated List:", List);
List.remove(4)
print("List.remove(4), Updated List:", List); #element is 4
List.reverse();
print("List.reverse(), Updated List:", List);
List.sort();
print("List.sort(), Updated List:", List);
