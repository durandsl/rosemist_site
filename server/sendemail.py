import smtplib
import json
import cherrypy

@cherrypy.expose
class EmailHandler(object):

    def __init__(self):
        config = {}
        with open('config.json', "r") as configFile:
            config = json.load(configFile)

        self.userName = '{0}@gmail.com'.format(config['userName'])
        self.password = config['password']

    def GET(self):
        return "GET REQUEST SUCCESS"

    @cherrypy.tools.json_out()
    def POST(self, contactName, email, phoneNumber, emailBody):
        subject = "Subject: Web Contact Form - {0}".format(contactName);
        body = "{0}\n\nContact Name: {1}\nEmail: {2}\nPhone Number: {3}\nMessage:\n\n{4}" \
            .format(subject, contactName, email, phoneNumber, emailBody)
        try:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(self.userName, self.password)
            smtp_server.sendmail(self.userName, self.userName, body)
            smtp_server.quit()
            return {
                "type": "success",
                "message": "Contact form successfully submitted. Thank you, we will get back to you soon!"
            }
        except:
            return {
                "type": "danger",
                "message": "There was an error while submitting the form. Please try again later"
            }




