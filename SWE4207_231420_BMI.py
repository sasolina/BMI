
def greeting():
    """this function will provide the objective of the program and ask the user if they would like to continue"""
    choice = str(input('do you want to go futher (Y) or (n): ')) # this
    while choice not in ['y','n']:
        choice =  str(input('do you want to go futher (Y) or (n): '))
    if choice == 'n':
        print("Goodbye")
        quit()
    else:
        gather_data()
    return


def gather_data():
    """This function will gather data from a number of users using a list """
    list_bmi = []
    while True:
        height = float(input("Please enter height in m: "))
        weight = float(input("Please enter weight in kg: "))
        bmi = calculate_bmi(weight,height)
        print(f'The BMI for height of {height} and weight of {weight} is {round(bmi,2)} ')
        list_bmi.append(round(bmi,2))
        
        print(list_bmi)
        for each in list_bmi:
            print(each)

        stop_choice = input("To end this process Y: ")
        if stop_choice == 'Y':
            print(list_bmi)
            break

    find_highest(list_bmi)
    find_lowest(list_bmi)
    find_average(list_bmi)
    return 

def calculate_bmi (weight: float, height: float):
    """This function will calculate the BMI using arguements for weight and height"""
    # BMI = weight (kg) / height (m) ^ 2
    return ((weight)/(height*height ))

def find_highest(list_users):
    print(list_users)
    print(f'the highest bmi is {max(list_users)}.')

def find_lowest(list_users):
    print(list_users)
    print(f'the lowest bmi is {min(list_users)}.')

def find_average(list_users):
    print(list_users)
    print(f'the average bmi is {sum(list_users)/len(list_users)}.')


greeting()
