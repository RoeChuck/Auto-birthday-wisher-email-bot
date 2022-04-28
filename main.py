import datetime
import random
import smtplib
import pandas

YOUR_EMAIL = input('Email address: ')
PASSWORD = input('Password: ')

birthdays_list = pandas.read_csv('birthday.csv')
now = datetime.datetime.now()
different_letters = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

for (index, row) in birthdays_list.iterrows():
    if now.month == row.month and now.day == row.day:
        with open(file=random.choice(different_letters)) as file:
            a = file.read()
        email_body = a.replace("[NAME]", row["name"])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=YOUR_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=YOUR_EMAIL,
                to_addrs=row.email,
                msg=f"Subject: Happy Birthday!\n\n{email_body}"
            )