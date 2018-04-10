#QUESTION 1
#Rmit University - Semester 2, 2017
#COSC2539 - Security in Computing and Information Technology
#Instructor: Denis Rinfret
#Date: August 5th, 2017
#Conductors: Tung Lam Minh - s3598768 & Tuan Huynh Doan - s3463207

######################################################################################################################

#PROGRAM HOW-TO-USE EXPLANATION AND CRYPTANALYSIS


# A. CRYPTANALYSIS

#In Question 1,  we need to decrypt the message with Ceasar Algorithm and the key unknown.
# However, we know one thing that key is between 1 and 50.
# Key cannot be 0 because with key 0, the decrypted message will be the same as the encrypted message.
# Also, we need to notice one thing that with Ceasar algorithm , we can shift forward or backward.
# With alphabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789 We can shift from A → 9 or 9 → A
#Shift from A→ 9 happens most rather than 9--> A ⇒ Therefore, we test Shift forward from A→9 first .
# If we do not get any message, we then test with shift backward from 9→A

#At this point, we use our program to test each key from 1--> 50 with the situation: shifting from A-->9 .
# After a while testing with the key from 1→ 38 , we do not get any message. However, with the key 39, we get the message like below:


#LIVING IN VIETNAM

#LOCATED IN SOUTH EAST ASIA, VIETNAM OCCUPIES THE SOUTH OF THE INDOCHINA PENINSULA WITH THE SHAPE OF AN ELONGATED 'S'. A TROPICAL COUNTRY, VIETNAM HAS DIVERSE SCENERY: FROM SOARING MOUNTAINS TO WHITE SANDY BEACHES, FROM TROPICAL FORESTS TO MYSTERIOUS CAVES.

#$VIETNAM IS ALSO WHERE YOU CAN FIND A FEAST OF HISTORY AND CULTURE. VIETNAMESE CULTURE IS DISTINCT: A FUSION  OF CHINESE, JAPANESE, AMERICAN AND FRENCH CULTURES.

#THE COUNTRY IS DIVIDED INTO THREE AREAS: NORTH VIETNAM, CENTRAL VIETNAM AND SOUTH VIETNAM. WHILE THE NORTH IS KNOWN FOR ITS OLD AND HISTORIC CAPITAL, CENTRAL VIETNAM IS FAMOUS FOR ITS SPECTACULAR BEACHES AND LAGOONS. COMING TO THE SOUTH, YOU WILL ENCOUNTER DYNAMIC HO CHI MINH CITY'S MODERN LIFE. LIVING AND STUDYING IN VIETNAM WILL YOU AN OPPORTUNITY TO EXPLORE A UNIQUE, HISTORIC, EXOTIC, YET RAPIDLY DEVELOPING COUNTRY.,



#⇒ With the key = 39, we get decrypted message. Therefore, we do not need to test other key


# B. PROGRAM HOW-TO-USE EXPLANATION

#In this program, we need to notice two parts:

#   1. key =39
#       We need to replace number “39” with the number between 1->50 for testing purpose.
#       When we get the desire key, we will leave the correct key number (key=39) here

#   2. decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#       In ceasear, we have 2 situation, shiting forward from A->9 and shifitng backward from 9->A:
#           For shifting forward from A->9: decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#           For shifting backward from 9->A: decrypt += alphabet[(alphabet.index(a)- key)%(len(alphabet))]
#       In this case, we test with the situation shifting forward from A->9 first,
#       so we will use : decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]

#   ⇒ We test the key from 1->50 with the shifting forward from A->9 and get the decrypted message with key =39



######################################################################################################################




###BELOW IS THE SOURCE CODE TO DECRYPT MESSAGE 1



#OPEN FILE "MSG1.ENC" , REMOVE "<" AND ">" AND CONVERT ALL LETTERS INTO UPPERCASE

file = open('msg1.enc', 'r')
s = file.read()
s1 = s.replace("<","")
message1 = s1.replace('>','')
message = message1.upper()

#######################

#ALPHABET LETTERS

alphabet="""ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""

##############################

#Replace the key from 1->50 for testing purpose only.
# After getting the result, please leave the correct key here ( key =39)

key =39

###############
#CREATE STRING TO STORE DECRYPTED MESSSAGE
decrypt=''

################################
#FUNCTION TO DECRYPT CEASER CIPHER

for a in message:
    if a in alphabet:

#### In ceasear, we have 2 situations, shiting forward from A->9 and shifitng backward from 9->A:
#           For shifting forward from A->9: decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#           For shifting backward from 9->A: decrypt += alphabet[(alphabet.index(a)- key)%(len(alphabet))]
#       In this case, we test with the situation shifting forward from A->9 first,
#       so we will use : decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]

        decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]

#######################################

#PRINT DECRYPTED MESSAGE
print('Your decrypted message is: '+"\n"+"----------------------------------------------------"+"\n"+decrypt)

#CLOSE FILE
file.close()

#######################################################################################################################
