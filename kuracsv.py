import smtplib
import csv
import getpass
from email.message import EmailMessage



#jpjalscbzswchjwx
#jespson.saintpierre@lastmiletalent.com

#this section here is to initialize the smptp server and the gmail 2 factor authentication 
smtp_obj = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.ehlo()
email="yourownemail"
password="your own password"
diagnostic_num=getpass.getpass("Enter diagnostic num: ")
smtp_obj.login(email, password)
msg = EmailMessage()

#function to send email
def send_email(email, stu_email, diagnostic_num, stu_name, stu_grade):
    #This function contains all the information needed to send an email using smtp
    msg.set_content(f"Hi {stu_name}, Congratulations for completing diagnotic {diagnostic_num}. Here is your score {stu_grade}")

    msg['Subject'] = f"score for diagnotic {diagnostic_num}"
    msg['From'] = email
    msg['To'] = stu_email
    #msg['cc'] = []
    smtp_obj.send_message(msg)

csvfile = open('testing1.csv', 'r')

# Loop over a csv reader on the file object
for row in csv.DictReader(csvfile):
    # Add the rank and name to the dictionary
    #print(row)
    # Print the dictionary keys
    #print(row.keys())
    print(row['first name '], row['grade '], row['email'])
    send_email(email, row['email'], diagnostic_num, row['first name '], row['grade '])


smtp_obj.quit()