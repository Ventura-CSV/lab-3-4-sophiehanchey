def main():
    x = int(input('Enter your input: '))
    y = int(input('Enter your input: '))
    
    #determining what quadrant the point is
    if(x>0):
        if(y>0):
            quadrant = 1
        else:
            quadrant = 4
    else:
        if(y>0):
            quadrant = 2
        else:
            quadrant = 3

    print(f'Quadrant: {quadrant}')
    ########################################
    # Do not delete the return statement
    ########################################
    return quadrant


if __name__ == '__main__':
    main()
