sub1 = int(input("Enter number 1 : "))
sub2 = int(input("Enter number 2 : "))
sub3 = int(input("Enter number 3 : "))

percen = (sub1 + sub2+ sub3)/3
print(percen,"%")

if(percen >= 40 and sub1 >= 33 and sub2 >=33 and sub3 >=33):
    print("PASS")
else:
    print("FAIL")    