import smtplib
import json
config = {}
with open('config.json', "r") as configFile:
    config = json.load(configFile)

userName = '{0}@gmail.com'.format(config['userName'])

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.ehlo()
smtp_server.starttls()

smtp_server.login(userName, config['password'])
smtp_server.sendmail(userName, userName, 'Subject: Test\nTest! TEST')
smtp_server.quit()
print('Email sent successfully')
