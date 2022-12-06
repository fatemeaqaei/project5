def jadval_zarb(num1, num2):
    for i in range (num2 + 1):
        for j in range(num1 + 1):
            if i == 0 and j == 0 :
                print('⚠', end="\t")
            elif i == 0 or j == 0 :
                print(i+  j, end="\t")
            else:
                print(i * j, end="\t")
        print(' ')

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
jadval_zarb(num1, num2)