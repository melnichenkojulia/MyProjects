# Write a script that summarizes and processes sales data into different categories
# Generate a PDF using Python
# Automatically send a PDF by email
# Write a script to check the health status of the system

# descriptions(.txt->.html) vs images(.tiff->jpeg)
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import os
import psutil
import socket
from PIL import Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
file_path = "../final_google/suppliers/"


def convert_im(filename):
    filename = os.path.join(filename[:-3] + "tiff")
    # print(filename)
    if filename.endswith('.tiff'):
        im = Image.open(str(os.path.join(file_path + filename)))


        new_file = os.path.join(file_path + filename[:-4] + "jpeg")
        im.thumbnail(im.size)
        im.save(new_file, "JPEG", quality=100)
        # print(new_file)
        return new_file
def convert_txt():
    l_dict=[]
    for filename in os.listdir(file_path):
        if filename.endswith('.txt'):
            with open(os.path.join(file_path + filename), "r") as txt:
                body = txt.read()
                name, body = body.split("\n", 1)
                weight, description = body.split("\n", 1)
                weight = int(weight.strip(" lbs"))
                dict = {"name": name, "weight": weight, "description": description, "image_name": convert_im(filename)}
                l_dict.append(dict)
              # print(dict)

                #sending dict on site
    # site = "http://34.122.209.128/feedback/"
    for i in l_dict:
        pass
        #print('post', requests.post(site, data=i))
        # print(i)
    return l_dict


#generate pdf
# reports.generate_report(attachment, title, paragraph)
# name, weight
def generate_pdf():
    data_name=[]
    data_weight=[]
    report = SimpleDocTemplate(os.path.join(file_path,"Processed.pdf"))
    styles = getSampleStyleSheet()
    report_title = Paragraph("Processed update on "+datetime.datetime.now().strftime("%B %d, %Y"), styles["h1"])
    report.build([report_title])
    dict=convert_txt()
    # print("dict=",dict)
    j=0
    # reports=[]
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    story = []
    story.append(report_title)
    for i in dict:
        reports=Paragraph
        print(i)
        data_name.append(i["name"])
        data_weight.append(i["weight"])
        t1 = "name: "+str(data_name[j])
        t2="weight: "+str(data_weight[j])+" lbs"
        t4=" "


        # add some flowables
        story.append(Paragraph(t1, styleN))
        story.append(Paragraph(t2, styleN))
        story.append(Paragraph(t4, styles["h4"]))

        j = j + 1

    report.build(story)


#send it by email
#emails.generate_email() and emails.send_email()


def email_sending(subject,body,pdf_need):
    # Create a multipart message and set headers

    sender_email = "vlastelin3212@gmail.com"
    receiver_email = ['supermeatvlad@gmail.com', 'julia1melnichenko@gmail.com']
    password = 'vbhf2212'  # input("Type your password and press enter:")
    for i in receiver_email:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = i
        message["Subject"] = subject
        # message["Bcc"] = receiver_email  # Recommended for mass emails
        print(message)
        # Add body to email
        message.attach(MIMEText(body, "plain"))
        part = MIMEBase("application", "octet-stream")
        if pdf_need=="yes":

            filename = os.path.join(file_path,"Processed.pdf")  # file path

        # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment

                part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

        # Add attachment to message and convert message to string
            message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.set_debuglevel(1)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."





#health_check
def health_check():
#cpu usage %, avaliable disc space is lower than %, avaliable memory is less than MB,
    cpu_percent=psutil.cpu_percent()
    print("cpu_percent=",psutil.virtual_memory().percent) # gives an object with many fields
    if cpu_percent>80:
        subject_health ='Error - CPU usage is over 80%'
    #Available disk space is lower than 20%
    disk_space=psutil.disk_usage("C:/").percent
    print("disk_space=",disk_space)
    if disk_space<20:
        subject_health ='Error - Available disk space is less than 20%'
    # you can convert that object to a dictionary
    # print(dict(psutil.virtual_memory()._asdict()))

    # hostname "localhost" cannot be resolved   to "127.0.0.1"
    hostname=socket.gethostbyname(socket.gethostname()) # print(socket.getfqdn()) #Moon-PC
    print("hostname=",hostname)
    if hostname!="127.0.0.1":
        subject_health='Error - hostname "localhost" cannot be resolved to "127.0.0.1"'
    print("sub=",subject_health)
    if subject_health!="":
        body_health = "Please check your system and resolve the issue as soon as possible "
        email_sending(subject_health,body_health,"no")

generate_pdf()
email_sending(subject,body,"yes")
health_check()








