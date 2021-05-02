from email.mime.multipart import MIMEMultipart   # here we have a email package named email in python and under this
                                                 # package there is a sub package "mime(Multipurpose Internet Mail Extensions)"
                                                 # this is a standers that defines that the format for email messages.
                                                 # this mime is not really a part of python this has another sub package
                                                 # called multipart, that exposes a class called MIMEMultipart.
                                                 # with this we can send email as plain text or html format

from email.mime.text import MIMEText                # for text
import smtplib                                      # smtp server import kora holo
from email.mime.image import MIMEImage              # for sending image... ... ..
from pathlib import Path





message = MIMEMultipart()                # here we have created a MIMEMultipart object
message["from"] = "Rafsan"
message["to"] = "rafsantest255@gmail.com"
message["subject"] = "This is a Test"       # these 3 headers are supported by MIMEMultipart() object.
                                            # but we don't have a header called body. so we need to attach this.

message.attach(MIMEText("Here is the message body"))
message.attach(MIMEImage(Path("rafsan.jpeg").read_bytes()))                 # here we nned to pass our image data in binary ba byte code akare




with smtplib.SMTP(host="smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()         # with this we are telling the smtp server that, I ama client, iwant to send an email.
    smtp.starttls()     # this will put smtp connection in tls mode. with this all the command we will send to the smtp server, will be encrypted.
    smtp.login("here is the email", "here is the password")        # This is for login the gmail, from which we want to send email.
    smtp.send_message(message)    # pass our email message object
    print("sent")

