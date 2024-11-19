def calculatePay():
    # This first line is provided for you
    hours = input("Enter Hours: ")
    pay_rate = input("Enter Rate: ")
    try:
        total_hours = float(hours)
        total_rate = float(pay_rate)
    except:
        print("Error, please enter numeric input")
        quit()

    if total_hours > 40:
        reg_pay = total_hours * total_rate
        otp = (total_hours - 40.0) * (total_rate * 0.5)
        total_pay = reg_pay + otp
    else:
        total_pay = total_hours * total_rate
    print("Pay:",total_pay)
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
