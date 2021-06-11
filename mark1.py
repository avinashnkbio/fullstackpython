print("program to print the avearge marks and grade of a student")
sub1 = int(input("Enter marks obtained in subject 1: "))
sub2 = int(input("Enter marks obtained in subject 2: "))
sub3 = int(input("Enter marks obtained in subject 3: "))
sub4 = int(input("Enter marks obtained in subject 4: "))
sub5 = int(input("Enter marks obtained in subject 5: "))
sub6 = int(input("Enter marks obtained in subject 6: "))

avg_marks =(sub1+sub2+sub3+sub4+sub5+sub6)/6
print("Average mark:",avg_marks)

if avg_marks>=90:
    print("Grade is A,Excellent")
elif avg_marks>=80:
    print("Grade is B,Good")
elif avg_marks>=70:
    print("Grade is C,Fair")
elif avg_marks>=60:
    print("Grade is D,Satisfactory")
else:
    print("Grade is F,Fail")