import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "maggiedatlon@gmail.com"  # Enter your address
receiver_email = "mayceenelson@yahoo.com"  # Enter receiver address
receiver_txt_sms ="7193717373@mms.att.net"
password = "asvj kofy ulct qodi"
message = "This is Canon Professional Wellness Clinic reminding you of your blood work that needs completed tomorrow as discussed at your last visit with your primary care provider. "

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_txt_sms, message)