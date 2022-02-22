# read.py

f = open('textfile.txt', 'r')
data = f.read()
f.close()

# read-with.py
with open('submission.html', 'r') as f:
    data = f.read()


# write.py
data = 'Hello, world!'

f = open('file.txt', 'w')
f.write(data)
f.close()


# write-with.py
with open('file.txt', 'w') as f:
    f.write('Hello, world!')
