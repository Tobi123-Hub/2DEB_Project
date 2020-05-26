f = open("input.txt","r") #Åpna fila vi skal telle bokstaver i

f_out = open("output.txt","w") #Åpne utskriftsfil for å lagre data

file_content = f.read() #Lagre innhold i fila til file_content som en string

count = 0

for i in file_content:
    if (i == 'a') or (i == 'A') or (i == 'e') or (i == 'E') or (i == 'i') or (i == 'I') or (i == 'o') or (i == 'O') or (i == 'u') or (i == 'U') or (i == 'y') or (i == 'Y'):
        count = count + 1
        
print(count)

f_out.write("A or a: ") #Skriv til output.txt om hvor mange store og små A'er vi fant
f_out.write(str(count))

f.close() #Lukka fila som vi skal telle i
f_out.close()
