#grading system

score = int(input("Enter your score: "))

if 70 <= score <= 100:
    print("Grade: A")
  
elif 60 <= score < 70:
    print("Grade: B")
  
elif 50 <= score < 60:
    print("Grade: C")
  
elif 45 <= score < 50:
    print("Grade: D")
  
elif 40 <= score < 45:
    print("Grade: E")
  
else:
    print("Grade: F")
