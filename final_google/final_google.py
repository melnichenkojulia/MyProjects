# Write a script that summarizes and processes sales data into different categories
# Generate a PDF using Python
# Automatically send a PDF by email
# Write a script to check the health status of the system

# descriptions(.txt->.html) vs images(.tiff->jpeg)
import datetime
import requests
import os
import sys

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
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




generate_pdf()



#send it by email








# reports.generate_report(attachment, title, paragraph)
# name, weight







#emails.generate_email() and emails.send_email()


#health_check
#cpu usage %, avaliable disc space is lower than %, avaliable memory is less than MB,
# hostname "localhost" cannot be resolved   to "127.0.0.1"







