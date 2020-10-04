firstNumber = float(input())
secondNumber=float(input())

if firstNumber>secondNumber:
    print('%d > %d'%(firstNumber,secondNumber))
elif secondNumber>firstNumber:
    print('%d < %d'%(firstNumber,secondNumber))
else:
    print('%d = %d'%(firstNumber,secondNumber))