from ftplib import FTP

f = FTP('localhost')


f.login('husin')
fd = open('test.txt', 'wb')
f.retrbinary('RETR test.pdf', fd.write, 1024)
fd.close()
f.quit
