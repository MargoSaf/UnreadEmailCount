import imaplib,re
import email
def unread_email_count(username,password):
        try:
                mail = imaplib.IMAP4_SSL('imap.gmail.com')
                mail.login(username,password)
                x,y = mail.status('INBOX','(MESSAGES UNSEEN)')
                messages=int(re.search(b'MESSAGES\s+(\d+)',y[0]).group(1))
                unseen=int(re.search(b'UNSEEN\s+(\d+)',y[0]).group(1))
                return messages,unseen
        except imaplib.IMAP4.error:
                return 'NULL'
