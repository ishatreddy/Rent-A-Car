import smtplib

print('Hello! Welcome to Isha Car Rental.')
print()
wheels = input('''Would you like to rent a 2 wheeler or a 4 wheeler vehicle?
For 2 wheelers please type A and for 4 wheelers please type B.\n''').upper().strip()
print()
if wheels == 'A':
    print('''Here are the options for 2 wheelers:
    ---------------------------------------------
    1.Harley Davidson Motorbike    AED 70/Day
    2.Yamaha Motorbike             AED 50/Day
    3.Honda Motorbike              AED 40/Day
    4.Vespa Motorcycle             AED 35/Day
    ---------------------------------------------''')
elif wheels == 'B':
    print('''Here are the options for 4 wheelers:
    ---------------------------------------------
    1.Porsche Convertible          AED 370/Day
    2.Range Rover SUV              AED 300/Day
    3.Infiniti Q50 Sedan           AED 220/Day
    4.Nissan Sunny Sedan           AED 150/Day
    ---------------------------------------------''')
else:
    print('Sorry that is an invalid selection. Please type A or B.')
print()
vehicle = int(input('Which one would you like to rent? Please type the number corresponding to the vehicle of your choice.\n'))
if wheels == 'A' and vehicle == 1:
    bill= 70
elif wheels == 'A' and vehicle == 2:
    bill= 50
elif wheels == 'A' and vehicle == 3:
    bill = 40
elif wheels == 'A' and vehicle == 4:
    bill= 35
elif wheels == 'B' and vehicle == 1:
    bill= 370
elif wheels == 'B' and vehicle == 2:
    bill= 300
elif wheels == 'B' and vehicle == 3:
    bill= 220
elif wheels == 'B' and vehicle == 4:
    bill= 150
else:
    print('Sorry that is an invalid selection. Please choose a vehicle from the given list above.')
print()
duration = int(input('''How many days would you like to rent the vehicle for? (Min. 1, Max. 30)

Offers:
-------
11-20 Days: 10% off total bill
21-30 Days: 20% off total bill\n'''))
total = bill*duration
if duration >= 11 and duration <=20:
    total = total*0.9
elif duration >= 21 and duration <=30:
    total = total*0.8
else:
    total = total
print()
insurance= input('Would you like to purchase car insurance for an additional AED 200? Please type Yes or No.\n').lower().strip()
if insurance == 'yes':
    total = total+200
elif insurance == 'no':
    total = total
else:
    print('Sorry that is an invalid response. Please type Yes or No.')
print()
print(f'Your total bill is AED {total}')
print()
method= input('Would you like to pay by cash, card or online bank transfer?\n').lower().strip()
print()
if method == 'card':
    number= input('Please enter your credit card number:\n')
    code = input('Please enter your security code:\n')
elif method == 'online bank transfer':
    print(f'''Please transfer {total} to Isha Car Rental. Our bank account details are: 
Bank Name: ADCB
Branch Name: Al Barsha
Account No: 365279048922
Account Currency: AED''')
elif method == 'cash':
    print('You can pay us when you come to pick up the car.')
print()
email= input('Please enter your email address:\n').lower().strip()
name= input('Please enter your full name:\n').title().strip()
company= 'Isha Car Rental'
gmail_user = 'input email'
gmail_password = 'input password'
sent_from = company
to = email
subject = 'Your Isha Car Rental Purchase'
body = f'''Dear {name}, 
Your car rental service order for {total} has been placed and confirmed. 
You can pick up your purchase at our Al Barsha rental center in 2 business days.'''
email_text = f"""From: {sent_from}  
To: {to}  
Subject: {subject}
{body}
"""
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    print('Email sent!')
except:
    print('Something went wrong...')
print()
print('''Thank you for doing business with Isha Car Rental!
You should receive a transaction confirmation by email shortly.
---------------------------------------------------------------
For any further issues please contact us at ishacarrental@gmail.com | 0506342208''')
