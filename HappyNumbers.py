def check_happy_num(num):
    lst = []
    while True:
        summation = 0
        for i in num:
            summation += int(i)**2
            
        if summation == 1:
            return True
        elif summation in lst:
            return False
        else:
            lst.append(summation)
            num = str(summation)
            continue
            

def list_happy_num(num):
    count = 0
    start = 1
    happy_list = []
    while count < num:
        check = check_happy_num(str(start))
        if check == True:
            happy_list.append(start)
            start +=1
            count += 1
            continue
        else:
            start += 1
            continue
    return happy_list

                  
def play():
    choice = input('Do you want a list of Happy Numbers(press "1") or just want to check a number(press "2") ')
    if choice =='1':
        ask = input('How many numbers do you want? ')
        try:
            happy = list_happy_num(int(ask))
            print(happy)
        except:
            print('Sorry, wrong input')
            
    elif choice == '2':
        number = input('Please enter number: ')
        try:
            check = check_happy_num(number)
            if check == True:
                print('Happy Number')
            else:
                print('Not a Happy Number')
        except:
            print('Sorry, wrong input')
            
    else:
        print('Sorry, wrong input')
        

if __name__ == "__main__" :
    play()
