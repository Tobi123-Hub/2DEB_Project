import matplotlib.pyplot as plt

f = open("input.txt","r") #Åpna fila vi skal telle bokstaver i

f_out = open("output.txt","w") #Åpne utskriftsfil for å lagre data

file_content = f.read() #Lagre innhold i fila til file_content som en string


vokal_array = ['a', 'e', 'i', 'o', 'u', 'y']
n = len(vokal_array)
telle_array = [0]*n




for i in file_content:
    index = 0
    for k in vokal_array:
        if (i.lower() == k):
            telle_array[index] = telle_array[index] + 1
        index = index + 1


index = 0
for k in vokal_array:
    f_out.write(k) #Skriv til output.txt om hvor mange store og små A'er vi fant
    f_out.write(": ")
    f_out.write(str(telle_array[index]))
    f_out.write("\n")
    index = index + 1
    
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['a', 'e', 'i', 'o', 'u', 'y']
vokaler = [telle_array[index]]
ax.bar(langs,vokaler)
plt.show()


f.close() #Lukka fila som vi skal telle i
f_out.close()
