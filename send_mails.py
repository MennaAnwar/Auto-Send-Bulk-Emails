import csv, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_address = "mennamohamed549@gmail.com"
password = "pdopueoqnoqtdtpl"

message = MIMEMultipart()
message["Subject"] = "Exam Grades"
message["From"] = from_address

# Create the plain-text and HTML version of your message
text = """\
Hi {name},
How are you?
 your grade is {grade}"""
html = """\
<html>
  <body>
    <p><h1>Hi {name},</h1><br>
       How are you?<br>
        your grade is {grade}""
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.as_string().format(name=name,grade=grade)
            )

