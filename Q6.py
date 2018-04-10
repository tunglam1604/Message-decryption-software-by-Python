#QUESTION 6
#Rmit University - Semester 2, 2017
#COSC2539 - Security in Computing and Information Technology
#Instructor: Denis Rinfret
#Date: August 5th, 2017
#Conductors: Tung Lam Minh - s3598768 & Tuan Huynh Doan - s3463207

######################################################################################################################

#PROGRAM HOW-TO-USE EXPLANATION AND CRYPTANALYSIS


# A. CRYPTANALYSIS

#In this question, we need to decrypt message through 2 steps : First is Columnar Transposition and Second is Ceaser Cipher with the unknown key.
# As stated in the assignment description sheet, the message is encrypted through first Ceaser cipher and then columnar transposition
# ⇒ when decrypting, we need to decrypt through columnar transpositon first and then ceaser

#The key for both ceaser cipher and columnar are the same
# ⇒ We just need to find the key for ceaser and will then match it with columnar transposition

#For Ceaser cipher, we have 2 situations: shift forward or backward.

# With alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789 We can shift from A → 9 or 9 → A

# We therefore first need to test decrypting message with ceaser shiting forward from A-->9 and columnar transpositon with all possible keys from 1-->50.
# After testing a while, we do not get any desire message,

# we therefore move to the 2nd situation: shiting backward from 9-->A with all possible keys from 1→ 50 and columnar transposition.
#With the key 10, and shiting backward from 9→ A for ceaser We now get decrypted message:

#THE BACHELOR OF INFORMATION TECHNOLOGY PROGRAM IS ACCREDITED AT THE PROFESSIONAL LEVEL BY THE AUSTRALIAN COMPUTER SOCIETY (ACS), AN ORGANISATION THAT ACCREDITS INFORMATION AND COMMUNICATION TECHNOLOGY RELATED PROGRAMS IN AUSTRALIA.QQQQQQQQQ


#⇒ For Question 6: Algorithm : Columnar Transposition First, Ceaser Second (Ceaser shifiting backward from 9-->A), Key = 10. Decrypted message:

#THE BACHELOR OF INFORMATION TECHNOLOGY PROGRAM IS ACCREDITED AT THE PROFESSIONAL LEVEL BY THE AUSTRALIAN COMPUTER SOCIETY (ACS), AN ORGANISATION THAT ACCREDITS INFORMATION AND COMMUNICATION TECHNOLOGY RELATED PROGRAMS IN AUSTRALIA.QQQQQQQQQ


# B. PROGRAM HOW-TO-USE EXPLANATION

#In this program, we need to notice 3 parts:

#   1. key = 10

#       Replace the key from 1->50 ( with ceaser cipher, the key will be between 1->50 ) for testing purpose only. After getting the result, please leave the correct key here ( key =10)

#       We do not need to count the length of message and then find out the key by finding out the divisor of  message length like we normally find the key for columnar transposition cipher as we also have ceaser cipher in this question and both columnar transposition and ceaser cipher has the same key ==> We just need to find out the key for ceaser cipher and then match it with the key for columnar transposition

#   2. Columnar Transposition Part

#       Note: the number of rows = length of message / key

#COLUMNAR TRANSPOSITION CODE:

#           for i in range (int(len(message)/key)):
#             for a in range (key):
#              columnar += message[i+(a*(int(len(message)/key)))]

#   3. Ceaser Cipher Part
#       Note:
#           In ceasear, we have 2 situations, shiting forward from A->9 and shifitng backward from 9->A:
#               For shifting forward from A->9:
#                   decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#               For shifting backward from 9->A:
#                   decrypt += alphabet[(alphabet.index(a)- key)%(len(alphabet))]

#           In this case, we test with the situation shifting forward from A->9 first.
#            After first testing (with key between 1--> 50) , we do not get any decrypted message

 #          ==> We will move to the 2nd situation: shifting backward from 9->A:
#                   decrypt += alphabet[(alphabet.index(a)-key)%(len(alphabet))]

#  CEASER CIPHER CODE:
#        for a in columnar:
#        if a in alphabet:
#       decrypt += alphabet[(alphabet.index(a)-key)%(len(alphabet))]


######################################################################################################################


###BELOW IS THE SOURCE CODE TO DECRYPT MESSAGE 6


#OPEN FILE "MSG6.ENC2" , REMOVE "<" AND ">" AND CONVERT ALL LETTERS INTO UPPERCASE
file = open('msg6.enc2', 'r')
s = file.read()
s1 = s.replace("<","")
message1 = s1.replace('>','')
message = message1.upper()

#############

#ALPHABET LETTERS
alphabet="""ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""

#Replace the key from 1->50 ( with ceaser cipher, the key will be between 1->50 ) for testing purpose only.
# After getting the result, please leave the correct key here ( key =10)


#We do not need to count the length of message and then find out the key by finding out the divisor of  message length
#Like we normally find the key for columnar transposition cipher as we also have ceaser cipher in this question and both
#columnar transposition and ceaser cipher has the same key ==> We just need to find out the key for ceaser cipher and
#then match it with the key for columnar transposition


key = 10

###############
#CREATE STRING TO STORE DECRYPTED MESSSAGE

decrypt=''
columnar=''

########

#Columnar Cipher

#Note: the number of rows = length of message / key
for i in range (int(len(message)/key)):
    for a in range (key):
        columnar += message[i+(a*(int(len(message)/key)))]

#Caesar Cipher

#### In ceasear, we have 2 situations, shiting forward from A->9 and shifitng backward from 9->A:
#           For shifting forward from A->9: decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#           For shifting backward from 9->A: decrypt += alphabet[(alphabet.index(a)- key)%(len(alphabet))]
#   In this case, we test with the situation shifting forward from A->9 first.
#   After first testing (with key between 1--> 50) , we do not get any decrypted message
#   ==> We will move to the 2nd situation: shifting backward from 9->A: decrypt += alphabet[(alphabet.index(a)-key)%(len(alphabet))]


for a in columnar:
    if a in alphabet:
        decrypt += alphabet[(alphabet.index(a)-key)%(len(alphabet))]

#PRINT DECRYPTED MESSAGE
print('Your decrypted message is: '+"\n"+decrypt)

###CLOSE FILE
file.close()

##########################
