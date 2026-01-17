# student marksheet maker
name=input("Enter Student Name")
roll=int(input("Enter Roll Number"))
 
 # subject name
sub1=input("Enter Subject 1 Name")
sub2=input("Enter Subject 2 Name")
sub3=input("Enter Subject 3 Name")
sub4=input("Enter Subject 4 Name")
sub5=input("Enter Subject 5 Name")

# Marks
m1=int(input("Enter marks for {sub1} :"))
m2=int(input("Enter marks for {sub2} :"))
m3=int(input("Enter marks for {sub3} :"))
m4=int(input("Enter marks for {sub4} :"))
m5=int(input("Enter marks for {sub5} :"))

# Total and Percentage
total=m1+m2+m3+m4+m5
percentage=total/5

# Result checking
if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
 result="FAIL"
 grade= "NO GRADE"
else:
 result="PASS"
 if percentage>=90:
  grade="O"
 elif percentage>=80:
  grade="A"
 elif percentage>=60:
  grade="B"
 elif percentage>=50:
  grade="C"
 elif percentage>=35:
  grade="D"

 # output
print("\n====STUDENT RESULT====")
print("NAME :",name)
print("ROLL NUMBER :",roll)
print("\nSUBECT-WISE MARKS :")
print(sub1,":",m1)
print(sub2,":",m2)
print(sub3,":",m3)
print(sub4,":",m4)
print(sub5,":",m5)

print("\nTOTAL MARKS:",total)
print("PERCENTAGE:",percentage,"%")
print("GRADE:", grade)
print("RESULT:",result)
