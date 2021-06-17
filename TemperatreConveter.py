#Temperrature convetor and heart beat conventor....
import time
import json
def Choose_one_of_them(X):
    switch={
        "Enter one number":"Covert Fahrenheit to celsius","Enter two number":"Covert Fahrenheit to celsius","Enter three number":"To check the time-rate of heart beat"
        }
    return switch.get(X,"Please enter proper option")

All_option_in_one={
    1:"Covert Fahrenheit to celsius",
    2:"Covert Fahrenheit to celsius",
    3:"To check the time-rate of heart beat"
}
Y=json.loads(All_option_in_one)



Enter=int(input("Please enter your option to see to check the tempearture:"))
Choose = Choose_one_of_them(Enter)
print(Choose)
if Enter is 1:
    F=int(input("Enter Fahrenheit temperature:"))
    C=(F-32)*5/9
    print(f"\n\n{C} is your Celcius temperature.")
if Enter is 2:
    C=int(input("Enter Celsius temperature:"))
    F=(C*9/5)+32
    print(f"\n\n{F} is your Fahrenheit temperature")
if Enter is 3:
    print("The timer will go on till 15 seconds count the beat")
    ready_button=int(input("\n\nPrees 1 when you are ready:"))
    if ready_button is 1:
        second=15
        for i in range(second):
            print(str(second-i) + "sec")
            time.sleep(1)




