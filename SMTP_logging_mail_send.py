
import logging.handlers
import getpass
 
MAILHOST = 'localhost'
FROM = 'you@yourdomain'
TO = ['%s@localhost' %getpass.getuser()] 
SUBJECT = 'Test Logging email from Python logging module (buffering)'
 
class BufferingSMTPHandler(logging.handlers.BufferingHandler):
    def __init__(self, mailhost, fromaddr, toaddrs, subject, capacity):
        logging.handlers.BufferingHandler.__init__(self, capacity)
        self.mailhost = mailhost
        self.mailport = None
        self.fromaddr = fromaddr
        self.toaddrs = toaddrs
        self.subject = subject
        self.setFormatter(logging.Formatter("%(asctime)s %(levelname)-5s %(message)s"))
 
    def flush(self):
        if len(self.buffer) > 0:
            try:
                import smtplib
                port = self.mailport
                if not port:
                    port = smtplib.SMTP_PORT
                    smtp = smtplib.SMTP(self.mailhost, port)
                    msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (self.fromaddr, ",".join(self.toaddrs), self.subject)
                for record in self.buffer:
                    s = self.format(record)
                    print(s)
                    msg = msg + s + "\r\n"
                smtp.sendmail(self.fromaddr, self.toaddrs, msg)
                smtp.quit()
            except:
                self.handleError(None) # no particular record
            self.buffer = []

def test():
    logger = logging.getLogger("")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(BufferingSMTPHandler(MAILHOST, FROM, TO, SUBJECT, 10))
    for data in ['First', 'Second', 'Third', 'Fourth']:
        logger.info("%s line of log", data)
    logging.shutdown()
 
if __name__ == "__main__":
    test()