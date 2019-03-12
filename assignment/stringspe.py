str = "abc%s"
print(str%str%str%str);
str = "abc=%s def%%def";
print(str%str);
str = "abc=%s def%%%%def";
print(str%str);
