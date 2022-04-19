import os
import imaplib
import email
import sys
import shutil

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "progjar2022" + ORG_EMAIL
FROM_PWD = "pakbagus123"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

try:
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL,FROM_PWD)
    mail.select('inbox')
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()

    directory_name = "downloads"
    command = sys.stdin.readline()

    if(command.__contains__("downmail")):
        number = command[9:].rstrip("\n")
        number = int(number)
        for i in range(-1, -number-1, -1):
            typ, data = mail.fetch(id_list[i], '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(data[0][1])
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            
            email_from = msg['from']
            email_subject = msg['subject']
            
            #Get Body of the mail
            name_file = str(int(id_list[i]))+ " " + str(email_subject) + ".txt"
            name_save = directory_name + '/' + name_file
            with open(name_save, 'a') as f:
                f.write("From : " + email_from + "\n" + "Subject : " + email_subject + "\n")
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        f.write(body.decode('utf-8'))
                
            
            #Get attachment
            for part in email_message.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                fileName = part.get_filename()
                if bool(fileName):
                    folderPath = 'D:/FileKuliah/Progjar/Pertemuan-11/downloads/' + str(int(id_list[i])) + "/"
                    if(os.path.isdir(folderPath) == False):
                        os.mkdir(folderPath)
                    filePath = os.path.join(folderPath, fileName)
                    if not os.path.isfile(filePath) :
                        fp = open(filePath, 'wb')
                        fp.write(part.get_payload(decode=True))
                        fp.close()
        
        shutil.make_archive('downloads', 'zip', "D:/FileKuliah/Progjar/Pertemuan-11/downloads")
        dir = 'D:/FileKuliah/Progjar/Pertemuan-11/downloads/'
        for files in os.listdir(dir):
            path = os.path.join(dir, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

except Exception as e:
    print(str(e))