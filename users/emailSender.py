import smtplib
import introvertChallenges
import random
import pickle



def email_sender(emailAddress):
    challengeChoice = random.randint(1, introvertChallenges.numberOfChallenges())
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("donle22599@gmail.com", "mfaijkr7")

    msg = introvertChallenges.switch_demo(challengeChoice);
    server.sendmail("donle22599@gmail.com", emailAddress, msg)
    server.quit()


def sendAllUsers():
    with open('/home/don/backup1/users/emailAddresses', 'rb') as f:
        while True:
            try:
                a = pickle.load(f)
            except EOFError:
                f.close()
                break
            else:
                email_sender(a)



sendAllUsers()
