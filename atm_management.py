#ATM mechine
balance=5000
pin=6888
while True:
    print("********Welcome to ABHI ATM *******")
    print("Enter the PIN Number ::",end="")
    user_pin_input=int(input())
    if user_pin_input==pin:
        print(".:Please select the option Below{Note::Enter the number}:.")
        print("1.Balance Enquery:.")
        print("2.With Drawl:.")
        print("3.Deposite:.")
        print("4.Exite:.")
        user_choice_input=int(input())
        match user_choice_input:
            case 1:
                print(f"Acount Balance ::{balance}")
            case 2:
                print("Enter the Amount")
                user_withdraw_input=int(input())
                if user_withdraw_input>balance:
                    print("***Insufficent Balance ****")
                    print(f"Current Balance:{balance}")
                else:
                    balance=balance-user_withdraw_input
                    print("Take you Cash")
                    print(f"Current Balance::{balance}")
            case 3:
                print("Enter the cash to Deposite::")
                user_deposite_input=int(input())
                balance=balance+user_deposite_input
                print(f"After Deposite Balance:{balance}")
            case 4:
                print("Thanku ABHI ATM bye bye::❤️❤️")
                break
            case _:
                print("Invalid Choice :")
    else:
        print("Enter the valid PIN ::")
