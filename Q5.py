file = open('msg5.enc', 'r')
s = file.read()

s1 = s.replace("<","")
message1 = s1.replace('>','')
message = message1.upper()


########## Count Character Frequency
def char_frequency(str):
    count = {}
    for n in str:
        keys = count.keys()
        if n in keys:
            count[n] += 1
        else:
            count[n] = 1
    return count

print(char_frequency(message))

print("\n")
###################################
######Decrypt Start Here

mes0=list(message)
mes1=list(message)


for i in range(len(mes0)):

#Replace the letter in " " in 2 line of code below with any testing character .
# The first one is the letter in the message, the 2nd one is the new replaced character
    if mes0[i]==" ":
        mes1[i]=" "



############################
####################

print("Decrypt Message: "+"\n")
print("".join(mes1))

print("\n")
###############################################################

mes2=list(message)
mes3=list(message)

for i in range(len(mes2)):
    if mes2[i]==" ":
        mes3[i]=" "
print("Message after 1st decrypted time with space: "+"\n")
print("".join(mes3))

file.close()
