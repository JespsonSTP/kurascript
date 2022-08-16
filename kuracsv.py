import smtplib
import csv
import getpass
from email.message import EmailMessage


#this section here is to initialize the smptp server and the gmail 2 factor authentication 
smtp_obj = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.ehlo()
email=getpass.getpass(prompt="Enter email: ")
password=getpass.getpass(prompt="Enter password: ")
diagnostic_num=getpass.getpass(prompt="Enter diagnostic num: ")
smtp_obj.login(email, password)

#admin email for cc 
"""
admin1 = getpass.getpass(prompt="Enter email: ") 
admin2 = getpass.getpass(prompt="Enter email: ") 
admin3 = getpass.getpass(prompt="Enter email: ") 
admin4 = getpass.getpass(prompt="Enter email: ") 

def passing_send_email(email, stu_email, diagnostic_num, stu_name, stu_grade, stu_out_of_five, admin1, admin2, admin3, admin4):

"""

#function to send email
def passing_send_email(email, stu_email, diagnostic_num, stu_name, stu_grade, stu_out_of_five):
    #This function contains all the information needed to send an email using smtp
    msg = EmailMessage()
    msg.set_content(f"""
Hello {stu_name}, 

Below you will find your total score as well as the score for each question for diagnostic {diagnostic_num}.

Congratulations on earning a score of {stu_grade}, which meets the passing benchmark of 85%. 

We encourage you to continue to study, practice and, as always, seek out opportunities to help your classmates who may have questions about these and other topics. Remember, the more you teach, the more you learn and improve your understanding. 

Total Score: {stu_grade}
{stu_out_of_five}""")

    msg['Subject'] = f"score for diagnotic {diagnostic_num}"
    msg['From'] = email
    msg['To'] = stu_email
    #msg['cc'] = [admin1, admin2, admin3, admin4]
    smtp_obj.send_message(msg)

def failling_send_email(email, stu_email, diagnostic_num, stu_name, stu_grade, stu_out_of_five):
    #This function contains all the information needed to send an email using smtp
    msg = EmailMessage()
    msg.set_content(f"""
Hello {stu_name}, 

Below you will find your total score as well as the score for each question for diagnostic {diagnostic_num}.
     
You earned a score of {stu_grade}, which does not meet the passing benchmark of 85%. 

Do not be discouraged as you are certainly capable of learning this material but, as you can see, you will really need to dedicate more time to learning and practicing. We would highly recommend that you seek to retake this assignment by first reviewing the class notes, videos, online resources, and setting up/joining study groups with your classmates. If, after doing all of this, the answers are still not clear, then you should send out a request for an office hour with an instructor or learning coach. 
If after your first retake you do not pass again, we will want to set up a dedicated review session with you to understand where you may be encountering challenges so that we can help address them. 
    
Do not get discouraged! It’s time to rise to meet the challenge!

Total Score: {stu_grade}
{stu_out_of_five}""")

    msg['Subject'] = f"score for diagnotic {diagnostic_num}"
    msg['From'] = email
    msg['To'] = stu_email
    #msg['cc'] = [admin1, admin2, admin3, admin4]
    smtp_obj.send_message(msg)


def between_50_and_84_send_email(email, stu_email, diagnostic_num, stu_name, stu_grade, stu_out_of_five):
    #This function contains all the information needed to send an email using smtp
    msg = EmailMessage()
    msg.set_content(f"""
Hello {stu_name}, 

Below you will find your total score as well as the score for each question for diagnostic {diagnostic_num}.
     
You earned a score of {stu_grade}, which does not meet the passing benchmark of 85%. 

Do not be discouraged as you are certainly within range of passing. We would highly recommend that you seek to retake this assignment by first reviewing the class notes, videos, online resources, and setting up/joining study groups with your classmates. If, after doing all of this, the answers are still not clear, then you should send out your question(s) to an instructor or learning coach and they can decide whether it warrants an office hour. 

Don’t give up, you're almost there!
    
Total Score: {stu_grade}
{stu_out_of_five}""")

    msg['Subject'] = f"score for diagnotic {diagnostic_num}"
    msg['From'] = email
    msg['To'] = stu_email
    #msg['cc'] = [admin1, admin2, admin3, admin4]
    smtp_obj.send_message(msg)

csvfile = open('testing1.csv', 'r')

# Loop over a csv reader on the file object
for row in csv.DictReader(csvfile):
    # Add the rank and name to the dictionary
    #print(row)
    # Print the dictionary keys
    #print(row.keys())
    if int(row['perc_grade']) < 50:
        failling_send_email(email, row['email'], diagnostic_num, row['first name'], row['grade'], row['Score out of 5'])
    elif int(row['perc_grade']) > 50 and int(row['perc_grade']) < 84:
        between_50_and_84_send_email(email, row['email'], diagnostic_num, row['first name'], row['grade'], row['Score out of 5'])
    else:
        passing_send_email(email, row['email'], diagnostic_num, row['first name'], row['grade'], row['Score out of 5'])
    
    


smtp_obj.quit()

