from email.mime.multipart import MIMEMultipart


from email.mime.text import MIMEText                # for text
import smtplib                                      # smtp server import kora holo
from email.mime.image import MIMEImage              # for sending image... ... ..
from pathlib import Path
from string import Template                 # we will use The "Template" class to change the name from html template.

template = Template(Path("template.html").read_text())   # html template file er ekta template obj toiri kore newa hoilo.

template.substitute()   # with this "substitute()" method, we can replace parameters dynamicly.






message = MIMEMultipart()
message["from"] = "Rafsan"
message["to"] = "rafsantest255@gmail.com"
message["subject"] = "This is a Test"


message.attach(MIMEText("Here is the message body"))
message.attach(MIMEImage(Path("rafsan.jpeg").read_bytes()))




with smtplib.SMTP(host="smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("here is the email", "here is the password")
    smtp.send_message(message)
    print("sent")

