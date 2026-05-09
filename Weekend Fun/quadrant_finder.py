#Pseudocode:
    #Step1. Collect x and y coordinates.
    #Step2. Use if-elif  statement to check where the point lies on the graph (Quadrants, Origin, or Axes).


x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif x == 0 and y == 0:
    print("Origin")
elif y == 0 and x != 0:
    print("X-axis")
elif x == 0 and y != 0:
    print("Y-axis")
    
    
    
    
    
    
    
    
    
