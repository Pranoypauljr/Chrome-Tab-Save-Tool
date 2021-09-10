from chrome_save import c
with open("tab.txt", "w") as file:
    for i in c:
        file.write(i+'\n')
    file.close()

# file execution number:2
# used to write tab links to a text file
