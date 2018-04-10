#QUESTION 7
#Rmit University - Semester 2, 2017
#COSC2539 - Security in Computing and Information Technology
#Instructor: Denis Rinfret
#Date: August 5th, 2017
#Conductors: Tung Lam Minh - s3598768 & Tuan Huynh Doan - s3463207

######################################################################################################################

#PROGRAM HOW-TO-USE EXPLANATION AND CRYPTANALYSIS


# A. CRYPTANALYSIS

#For this question, we need to decrypt message with unknown algorithm ( but not Vernam) and unknown key
#First of all, We will need to test decrypting the message with both Ceaser Cipher and Columnar Transposition. ⇒ We do not get any decrypted message with both Ceaser Cipher and Columnar Transposition
#Secondly, We do not need to test decrypting message with Vernam because as stated, the algorithm is not Vernam
#⇒ We finally have Random Substitution for the algorithm

#To decrypt message 7 with Random Substitution:
#   We first count the character frequency in message 7
#       'H': 81, 'T': 105, 'J': 77, '7': 33, 'K': 17, '$': 82, '2': 71, '-': 20, 'F': 141, '4': 34, '0': 38, 'A': 55, 'Q': 35, '1': 19, 'N': 2, 'U': 42, '"': 43, '9': 10, 'P': 2, 'L': 23, 'Y': 9, ' ': 6, 'B': 3, 'Z': 15, 'D': 8, 'C': 1, 'S': 3, '6': 1, '?': 1, '8': 2, '\n': 1
#   We see that F is the character that appear most frequently in message 7 ⇒ We then replace it with the space “ “
#   We then continue testing and replacing all the characters that appear most frequently ( from the most to least) in message 7 with the common characters: e t a o i n s r h l d c u m f p g w y b v k x j q z
#   While replacing the characters, we also need to consider some specific words
#       1-letter word: I , a
#       2-letter words: it, is, an, he, me,  us, at, as by, if , by, go, of , on ,so, we,etc
#       3-letter words: are, the, and, for, but, not, any , all, can, you, our, one, etc.
#   We then need to guess the words after replacing some characters
#   After replacing most of the characters, we then proofread the message to replace the rest of characters


#⇒ For Question 7: Algorithm : Random Substitution.

#==>Key:

#   "F" → " "
#   "T" → "E"
#   "J" → "A"
#   "2" → "N"
#   "4" → "D"
#   "H" → "T"
#   "7" → "C"
#   "K" → "H"
#   "$" → "I"
#   "-" → "G"
#   "0" → "L"
#   "A" → "R"
#   "Q" → "M"
#   "1" → "V"
#   "N" → "\n"
#   "U" → "S"
#   '''"''' → "O"
#   "9" → "P"
#   "L" → "U"
#   "P" → "Q"
#   " " → "."
#   "B" → "W"
#   "Z" → "F"
#   "D" → "B"
#   "C" → "K"
#   "?" → "X"
#   "S" → ","
#   "6" → "'"
#   "8" → "-"


# ==> Decrypted message:

#    TEACHING AND LEARNING AT RMIT VIETNAM

#    RMIT VIETNAM IS COMMITTED TO PROVIDING QUALITY EDUCATION. THE DEGREE YOU WILL RECEIVE AFTER SUCCESSFUL COMPLETION OF YOUR STUDIES IN VIETNAM IS A GLOBAL RMIT UNIVERSITY DEGREE. THE LEARNING OUTCOMES AND ASSESSMENTS FOR COURSES TAUGHT IN VIETNAM ARE EQUIVALENT TO THOSE DELIVERED AT RMIT MELBOURNE. ACADEMIC STAFF EMPLOYED AT RMIT INTERNATIONAL UNIVERSITY VIETNAM WORK IN COLLABORATION WITH ACADEMIC STAFF FROM RMIT UNIVERSITY MELBOURNE TO CUSTOMISE THE MATERIALS THAT ARE PREPARED IN MELBOURNE FOR DELIVERY IN VIETNAM, AND TO FACILITATE THE TEACHING AND LEARNING PROCESSES AT RMIT VIETNAM. THE ACADEMIC'S ROLE AT RMIT VIETNAM IS FOCUSED ON ADDING VALUE TO THE TEACHING AND LEARNING PROCESS THROUGH CREATIVE FACILITATED LEARNING. THE TEACHING AND LEARNING MODEL AT RMIT VIETNAM IS BASED ON INTERNATIONAL BEST PRACTICE AND INCLUDES CLASSROOM LEARNING EXPERIENCES, FACILITATED ON-LINE AND SELF-DIRECTED LEARNING BY STUDENTS, AND PEER LEARNING.



# B. PROGRAM HOW-TO-USE EXPLANATION


#In this program, we need to notice 1 part:

#       if mes0[i]=="F":
#         mes1[i]=" "

#      if mes0[i]=="T":
#          mes1[i]="E"

#      if mes0[i]=="J":
#          mes1[i]="A"

#      if mes0[i]=="2":
#          mes1[i]="N"

#      if mes0[i]=="4":
#          mes1[i]="D"

#      ...............

#    if mes0[i]=="6":
#        mes1[i]="'"

#    if mes0[i]=="8":
#        mes1[i]="-"


#⇒ These are the keys.

#For example of 2 lines of code below:

 #  if mes0[i]=="8":
 #      mes1[i]="-"

#Replace the letter in " " in 2 line of code with any testing character .
#The first one is the letter in the message 7, the 2nd one is the new replaced character



######################################################################################################################


###BELOW IS THE SOURCE CODE TO DECRYPT MESSAGE 7

#OPEN FILE "MSG7.ENC" , REMOVE "<" AND ">" AND CONVERT ALL LETTERS INTO UPPERCASE
file = open('msg7.enc', 'r')
s = file.read()
s1 = s.replace("<","")
message1 = s1.replace('>','')
message=message1.upper()
decrypt=''
#######

##########Count Character Frequency

def char_count(str):
    count = {}
    for char in str:
        keys = count.keys()
        if char in keys:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(char_count(message))


print("\n")
###################################

######Decrypt Start Here

#CREATE STRING TO STORE DECRYPT MESSAGE
mes0=list(message)
mes1=list(message)
##

for i in range(len(mes0)):
#Replace the letter in " " in 2 line of code below with any testing character .
# The first one is the letter in the message, the 2nd one is the new replaced character
    if mes0[i]=="F":
        mes1[i]=" "

    if mes0[i]=="T":
        mes1[i]="E"

    if mes0[i]=="J":
        mes1[i]="A"

    if mes0[i]=="2":
        mes1[i]="N"

    if mes0[i]=="4":
        mes1[i]="D"

    if mes0[i]=="H":
        mes1[i]="T"

    if mes0[i]=="7":
        mes1[i]="C"

    if mes0[i]=="K":
        mes1[i]="H"

    if mes0[i]=="$":
        mes1[i]="I"

    if mes0[i]=="-":
        mes1[i]="G"

    if mes0[i]=="0":
        mes1[i]="L"

    if mes0[i]=="A":
        mes1[i]="R"

    if mes0[i]=="Q":
        mes1[i]="M"

    if mes0[i]=="1":
        mes1[i]="V"

    if mes0[i]== "N":
        mes1[i]="\n"

    if mes0[i]=="U":
        mes1[i]="S"

    if mes0[i]=='''"''':
        mes1[i]="O"

    if mes0[i]=="9":
        mes1[i]="P"

    if mes0[i]=="L":
        mes1[i]="U"

    if mes0[i]=="P":
        mes1[i]="Q"

    if mes0[i]==" ":
        mes1[i]="."

    if mes0[i]=="B":
        mes1[i]="W"

    if mes0[i]=="Z":
        mes1[i]="F"

    if mes0[i]=="D":
        mes1[i]="B"

    if mes0[i]=="C":
        mes1[i]="K"

    if mes0[i]=="?":
        mes1[i]="X"

    if mes0[i]=="S":
        mes1[i]=","

    if mes0[i]=="6":
        mes1[i]="'"

    if mes0[i]=="8":
        mes1[i]="-"

############################
####################

#PRINT DECRYPTED MESSAGE
print("Decrypt Message: "+"\n")
print("".join(mes1))

#################

#CLOSE FILE
file.close()

###########################################################
