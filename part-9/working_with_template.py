from email.mime.multipart import MIMEMultipart


from email.mime.text import MIMEText                # for text
import smtplib                                      # smtp server import kora holo
from email.mime.image import MIMEImage              # for sending image... ... ..
from pathlib import Path
from string import Template                 # we will use The "Template" class to change the name from html template.

template = Template(Path("template.html").read_text())   # html template file er ekta template obj toiri kore newa hoilo.

# template.substitute()                     # with this "substitute()" method, we can replace parameters dynamicly.






message = MIMEMultipart()
message["from"] = "Rafsan"
message["to"] = "rafsantest255@gmail.com"
message["subject"] = "This is a Test"
body = template.substitute({"name": "Rafsan"})         # ei "substitute()" method er moddho diyea amra ekta dictionary pass
                                                # korte pari.  we can also pass keyword argument here instead of dictionary
                                                # like below ===>>
# body = template.substitute(name = "Rafsan")

message.attach(MIMEText(body, "html"))
# message.attach(MIMEImage(Path("rafsan.jpeg").read_bytes()))




with smtplib.SMTP(host="smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("here is email", "here is password")
    smtp.send_message(message)
    print("sent")

