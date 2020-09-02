import smtplib



def mailSender(dest, name):      
        sender = "regmimishan@gmail.com"
        to = dest
        subject = "Registration Successful"
        headers = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (sender, to, subject)  
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('regmimishan@gmail.com','gmailpassword1234')
        message = headers + "Hi " + name + ", thank you for registering with us!"
        s.sendmail('regmimishan@gmail.com', dest, message)
        s.quit()


mailSender("mishanregmi@gmail.com", "Mishan Regmi")