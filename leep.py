# check if the year is leep year or not
year=int(input("enter the year:"))
if((year%400==0)or(year%100!=0)and(year%4==0)):
    print ("Given year is a leep year")
else:
    print("Given year is not a leep year")