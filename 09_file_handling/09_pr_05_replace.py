with open('09_file_handling/script.txt' , 'r') as f:
    content = f.read()

content = content.replace('twinkle' , '#%$##%$')

with open('09_file_handling/script.txt' , 'w') as f:
    f.write(content)
