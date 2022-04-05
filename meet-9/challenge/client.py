import ftplib
import zipfile
import os
while(True):
    print('Welcome to FTP Client')
    print('1. Login')
    print('2. Quit')
    choice = input('Enter your choice>> ')
    if choice == '1':
        print('Enter your username>> ')
        username = input()
        print('Enter FTP server IP>> ')
        server_ip = input()
        try:
            ftp = ftplib.FTP(server_ip)
            ftp.login(username)
            print('Login successful')
            print('Input Command>> ')
            command = str(input())
            if(command == "LIST"):
                names = ftp.nlst()
                print('List of files in the directory: ' + str(names))

            elif(command == "DOWNLOAD"):
                print('Enter the file name to download>> ')
                filename = str(input())
                fd = open(filename, 'wb')
                ftp.retrbinary('RETR ' + filename, fd.write, 1024)
                fd.close()
                print('File downloaded successfully')
            
            elif(command == "UPLOAD"):
                print('Enter the file name to upload>> ')
                filename = str(input())
                fd = open(filename, 'rb')
                ftp.storbinary('STOR ' + filename, fd, 1024)
                fd.close()
                print('File uploaded successfully')
            
            elif(command == "CREATE_DIR"):
                print('Enter the directory name to create>> ')
                dirname = str(input())
                ftp.mkd(dirname)
                print('Directory created successfully')
            
            elif(command == "CWD"):
                print('Current working directory is ' + ftp.pwd())
            
            elif(command == "UPTRACT"):
                print('Enter the file name to extract>> ')
                filename = str(input())
                filename = filename.strip('\n')
                # zipfile.Zipfile.extractall(os.path.join('D:/FileKuliah/Progjar/Pertemuan-9/', filename))
                dir_name = 'D:/FileKuliah/Progjar/Pertemuan-9/' + filename[:-4]
                with zipfile.ZipFile(filename, 'r') as zip_ref:
                    zip_ref.extractall(dir_name)
                ftp.mkd(filename[:-4])
                work_dir = '/' + filename[:-4]
                ftp.cwd(work_dir)
                print('Current working directory is ' + ftp.pwd())
                for item in os.listdir(dir_name):
                    dir_name = dir_name + '/'
                    if os.path.isfile(os.path.join(dir_name, item)):
                        fd = open(dir_name + item, 'rb')
                        ftp.storbinary('STOR ' + item, fd, 1024)
                        fd.close()
                print('File uploaded successfully')
            ftp.quit()
        except:
            print('Login failed')
    elif choice == '2':
        break
    else:
        print('Invalid choice')
