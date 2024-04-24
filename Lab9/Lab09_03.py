A = (80,"A")
B  = (70,"B")
C = (60,"C")
D = (50,"D")
F = (40,"F")
while True :
    number = input("Enter score : ")
    if number == 'y' :
        break 
    elif float(number) >= A[0] :
        print(A[1])
    elif B[0] <= float(number) < B[0] + 10 :
        print(B[1])
    elif C[0] <= float(number) < C[0] + 10 :
        print(C[1])
    elif D[0] <= float(number) < D[0] + 10 :
        print(D[1])
    elif F[0] <= float(number) < F[0] + 10 :
        print(F[1])
    
