from SendEmailTwo import sendMail

import getpass



if __name__ == "__main__":

    while True:

        choice = input("Do you want to send the data to RabbitMQ Queue(y/n) : ")

        if choice == 'y':

            sender = input("Enter Sender Gmail : ")

            password = getpass.getpass("Enter Sender Gmail Password : ")

            receiver = input("Enter Receiver Gmail : ")

            message = "Gmail Send Successfully. All the test cases passed"

            num1 = int(input("Enter first number : "))

            num2 = int(input("Enter Second number : "))

            sendMail.delay(sender , receiver , password , message , num1 , num2)

        elif choice == 'n':

            break

        else:

            print("Enter y(Yes) or n(No)")