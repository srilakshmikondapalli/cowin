import smtplib


class mail():
    def integrate(self):
        sender_email = "srilaxmi.kondapalli9.8@gmail.com"
        password = "9948586854"
        receiver_email = input("enter your email:")
        message ="hello!!"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        print("login success")
        server.sendmail(sender_email, receiver_email, message)
        print("email sent")
        server.quit()
obj=mail()
obj.integrate()