file = open("ascii.txt","w",errors="ignore")
num = 0
limit = 700000

filer = ""
print("\t\t\t"+chr(187))
while num != (limit+2):
    filer =filer +("\n<\t"+chr(num)+"\t>\tthis is ascii number "+str(num))
    print( "ascii\t number "+str(num)+"\t"+chr(num))
    num = num + 1
    
file.write(filer)
file.close
