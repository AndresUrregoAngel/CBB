#_*_coding:UTF-8 _*_
'''
##Exercice 1
flag = True
while flag:
    try:
        num= int(input('type a number'))
    except ValueError as v:
        print('Error wrong value' , v)
    else:
        print('votre valeu is:',num)
        flag = False
'''
'''
##Exercise 2
flag = True
while flag:
    try:
        num = int(input('type a number'))
        if not num in range (1,6):
            raise Exception ('wrong number , your option must be between 1 and 5')
    except Exception as v:
        print(v)

    else:
        print('Is good')
        flag=False

'''
flag=True
while flag:
    try:
        numa = int(input('type a number a'))
        numb = int(input('type a number b'))
        res = numa / numb
    except ValueError as values:
        print('You have to type numbers not letters',values)
    except ZeroDivisionError as zero:
        print('this division can not be executed because there a zero as value', zero)

    else:
        print('the result after a division  of a / b is:',res)
        flag=False

