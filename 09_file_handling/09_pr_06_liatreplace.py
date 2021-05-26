word = ["little" , "star" , "wonder"]

with open('09_file_handling/script.txt' , 'r') as f:
    content = f.read()
for words in word:
    content = content.replace(words , "xyz")
    with open('09_file_handling/script.txt' , 'w') as f:
        f.write(content)
