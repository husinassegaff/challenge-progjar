from ftplib import FTP

f = FTP('localhost')

print('Welcome: ', f.getwelcome())

f.login('husin')
print('Current directory: ', f.pwd())
names = f.nlst()
print('Files in current directory: ', str(names))
f.quit
