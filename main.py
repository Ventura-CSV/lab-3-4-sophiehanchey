def main():
    ##################################################
    # Comlete your code here
    ##################################################
    num1 = int(input('Enter the number 1'))
    num2 = int(input('Enter the number 2'))
    num3 = int(input('Enter the number 3'))

    if (num1 > num2):
        if (num1 > num3):
            print("The greatest number is", num1)
        else:
            print("The greatest number is", num3)
    else:
        if (num2 > num3):
            print("The greatest number is", num2)
        else:
            print("The greatest number is", num3)

    pass


if __name__ == '__main__':
    main()
