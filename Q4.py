#QUESTION 4
#Rmit University - Semester 2, 2017
#COSC2539 - Security in Computing and Information Technology
#Instructor: Denis Rinfret
#Date: August 5th, 2017
#Conductors: Tung Lam Minh - s3598768 & Tuan Huynh Doan - s3463207

######################################################################################################################

#PROGRAM HOW-TO-USE EXPLANATION AND CRYPTANALYSIS


# A. CRYPTANALYSIS

#For this question, we need to decrypt message with algorithm : Random Substitution and unknown key

#To decrypt message 4 with Random Substitution:

#   We first count the character frequency in message 4
#       '.': 30, 'O': 13, 'K': 38, '1': 40, 'D': 105, '\n': 8, 'L': 63, 'N': 42, '(': 35, ':': 27, 'R': 17, 'J': 23, 'P': 45, 'Q': 6, ',': 20, '8': 20, '?': 9, ' ': 13, 'Y': 16, 'I': 16, 'X': 7, '-': 4, '3': 8, 'T': 14, '2': 5, 'G': 4, 'S': 2, 'M': 1, '$': 3, '!': 1
#   We see that D is the character that appear most frequently in message 4 ⇒ We then replace it with the space “ “
#   We then continue testing and replacing all the characters that appear most frequently ( from the most to least) in message 7 with the common characters: e t a o i n s r h l d c u m f p g w y b v k x j q z
#   While replacing the characters, we also need to consider some specific words
#       1-letter word: I , a
#       2-letter words: it, is, an, he, me,  us, at, as by, if , by, go, of , on ,so, we,etc
#       3-letter words: are, the, and, for, but, not, any , all, can, you, our, one, etc.
#   We then need to guess the words after replacing some characters
#   After replacing most of the characters, we then proofread the message to replace the rest of characters

#⇒ For Question 4: Algorithm : Random Substitution.

#⇒ Keys:

#"D" ⇒ " "
#"L" ⇒ "E"
#"." ⇒ "R"
#"O" ⇒ "M"
#"K" ⇒ "I"
#"1" ⇒ "T"
#"(" ⇒ "A"
#"\n"⇒ "V"
#":" ⇒ "S"
#"\n" ⇒ "V"
#"," ⇒ "U"
#"8" ⇒ "Y"
#"R" ⇒ "G"
#"J" ⇒ "L"
#"P" ⇒ "O"
#"Q" ⇒ "B"
#"?" ⇒ "F"
#" " ⇒ "C"
#"Y" ⇒ "H"
#"I" ⇒ "D"
#"X" ⇒ "."
#"-" ⇒ "\n"
#"3" ⇒ "W"
#"2" ⇒ ","
#"G" ⇒ "K"
#"!" ⇒ "J"
#"$" ⇒ "'"
#"T" ⇒ "P"
#"S" => "-"
#"M" ⇒ "X"

#⇒ Decrypted Message:

#RMIT VIETNAM IS A GLOBAL UNIVERSITY OF TECHNOLOGY AND DESIGN...

#TECHNOLOGY NOW UNDERPINS SO MANY ASPECTS OF MODERN LIFE. WHETHER YOU ARE READING THE NEWS FROM YOUR LAPTOP, BUYING MOVIE TICKETS ON YOUR SMARTPHONE ON THE WAY TO THE CINEMA, OR USING A RECIPE APP ON YOUR TABLET WHILE YOU COOK - TECHNOLOGY HAS BECOME INTEGRATED WITH OUR DAILY EXISTENCE.

#TAKING A DEGREE IN A AN IT-RELATED FIELD MEANS LEARNING SKILLS THAT HELP TO SOLVE PEOPLE'S PROBLEMS IN CREATIVE, INNOVATIVE WAYS, USING TECHNOLOGY TO TRANSFORM PEOPLE'S WORLDS.  IF YOU'RE INTERESTED IN BEING A LEADER IN A CUTTING EDGE INDUSTRY, YOU MAY HAVE JUST FOUND YOUR FUTURE.


####

# B. PROGRAM HOW-TO-USE EXPLANATION

#In this program, we need to notice 1 part:

#if mes0[i]=="D":
#   mes1[i]=" "

#if mes0[i]=="L":
#   mes1[i]="E"

#if mes0[i]==".":
#   mes1[i]="R"

#if mes0[i]=="O":
#   mes1[i]="M"

#................................

#if mes0[i]=="S":
#   mes1[i]="-"

#if mes0[i]=="M":
#   mes1[i]="X"



#⇒ These are the keys.

#For example of 2 lines of code below:

#   if mes0[i]=="M":
#   	mes1[i]="X"

#Replace the letter in " " in 2 line of code with any testing character .
#The first one is the letter in the message 7, the 2nd one is the new replaced character

######################################################################################################################


###BELOW IS THE SOURCE CODE TO DECRYPT MESSAGE 4

#OPEN FILE "MSG4.ENC" , REMOVE "<" AND ">" AND CONVERT ALL LETTERS INTO UPPERCASE


file = open('msg4.enc', 'r')
s = file.read()
s1 = s.replace("<","")
s2=s1.upper()
message = s2.replace('>','')

####

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

#CREATE STRING TO STORE DECRYPT MESSAGE
mes0=list(message)
mes1=list(message)
####


for i in range(len(mes0)):

#Replace the letter in " " in 2 line of code below with any testing character .
# The first one is the letter in the message, the 2nd one is the new replaced character
    if mes0[i]=="D":
        mes1[i]=" "

    if mes0[i]=="L":
        mes1[i]="E"

    if mes0[i]==".":
        mes1[i]="R"

    if mes0[i]=="O":
        mes1[i]="M"

    if mes0[i]=="K":
        mes1[i]="I"

    if mes0[i]=="1":
        mes1[i]="T"

    if mes0[i]=="(":
        mes1[i]="A"

    if mes0[i]=="\n":
        mes1[i]="V"

    if mes0[i]==":":
        mes1[i]="S"

    if mes0[i]=="\n":
        mes1[i]="V"

    if mes0[i]==",":
        mes1[i]="U"

    if mes0[i]=="8":
        mes1[i]="Y"

    if mes0[i]=="R":
        mes1[i]="G"

    if mes0[i]=="J":
        mes1[i]="L"

    if mes0[i]=="P":
        mes1[i]="O"

    if mes0[i]=="Q":
        mes1[i]="B"

    if mes0[i]=="?":
        mes1[i]="F"

    if mes0[i]==" ":
        mes1[i]="C"

    if mes0[i]=="Y":
        mes1[i]="H"

    if mes0[i]=="I":
        mes1[i]="D"

    if mes0[i]=="X":
        mes1[i]="."

    if mes0[i]=="-":
        mes1[i]="\n"

    if mes0[i]=="3":
        mes1[i]="W"

    if mes0[i]=="2":
        mes1[i]=","

    if mes0[i]=="G":
        mes1[i]="K"

    if mes0[i]=="!":
        mes1[i]="J"

    if mes0[i]=="$":
        mes1[i]="'"

    if mes0[i]=="T":
        mes1[i]="P"

    if mes0[i]=="S":
        mes1[i]="-"

    if mes0[i]=="M":
        mes1[i]="X"


############################
####################

#PRINT DECRYPTED MESSAGE
print("Decrypt Message: "+"\n")
print("".join(mes1))

######

#CLOSE FILE
file.close()

###########################################################
