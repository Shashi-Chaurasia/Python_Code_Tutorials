f = open("/home/shashi/Documents/Python_Code_Tutorials/Game/file/poem.txt" , 'r')
t = f.read()
if 'twinkle' in t:
    print("twinkle is present ")

else: 
    print("twinkle is not present in poem")

f.close()
