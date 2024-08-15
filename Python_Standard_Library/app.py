# from pathlib import Path
# pathlib - python docs
# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path.with_name("file.txt")
# print(path.absolute())
# path.with_suffix(".txt")
# print(path)

# path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
# print(path.iterdir())
# for p in path.iterdir():
#     print(p)

# path = Path("ecommerce/__init__.py")
# print(path.stat())


# WEB BROWSER
# import webbrowser

# print("Deployment completed")
# webbrowser.open("http://google.com")

# SENDING EMAILS
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# import smtplib

# message = MIMEMultipart()
# message["from"] = "Tom Fyfe"
# message["to"] = "tomfyfe85@gmail.com"
# message["subject"] = "TEST"
# message.attach(MIMEText("Body"))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("tomfyfe85@gmail.com", "Batdad696")
#     print("sent..")

#     smtp.send_message(message)


#  COMMAND LINE ARGUMENTS
# import sys
# print(sys.argv)

# RUNNING EXTERNAL PROGRAMS
# import subprocess

# # completed = subprocess.run(["python3", "other.py"], capture_output=True, text=True)
# # print(completed.stdout)
# try:
#     completed = subprocess.run(["false"], capture_output=True, text=True, check=True)
# # print(completed.stdout)
# except subprocess.CalledProcessError as ex:
#     print(ex)