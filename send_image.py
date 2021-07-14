from picamera import PiCamera
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

camera = PiCamera()
#The mail addresses and password
sender_address = # ENTER RASPBERRYPI EMAIL ADDRESS
sender_pass = # ENTER THE PASSWORD
receiver_address = # ENTER YOUR EMAIL ADDRESS

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A picture taken by Pi camera module. It has an attachment.'   #The subject line

while True:
    # Take image
    pic = '/home/pi/Desktop/img.jpg'
    camera.start_preview()
    sleep(5)
    camera.capture(pic)
    camera.stop_preview()
    print('Image Captured')

    # Attach the file
    File = open(pic, 'rb')
    img = MIMEImage(File.read())
    File.close()
    message.attach(img)

    # Send Mail
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')




