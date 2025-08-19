# 骚扰邮件，启动！
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

import smtplib
# 省略使用模版（Template）部分

message = MIMEMultipart()
message["from"] = "StLloyd"
message["to"] = "german-quora-digest@quora.com"
message["subject"] = "This is a test"

message.attach(MIMEText("Body"))
message.attach(
    MIMEImage(Path("Python\Learning\PythonStandardLibrary\test1.jpg")))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("testuser@gmail.com", "Password")
    smtp.send_message(message)
    print("Sent")

    # 设置不对，这是跑不起来的，具体需要进一步研究
