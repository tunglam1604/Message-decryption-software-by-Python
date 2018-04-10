#QUESTION 3
#Rmit University - Semester 2, 2017
#COSC2539 - Security in Computing and Information Technology
#Instructor: Denis Rinfret
#Date: August 5th, 2017
#Conductors: Tung Lam Minh - s3598768 & Tuan Huynh Doan - s3463207

######################################################################################################################

#PROGRAM HOW-TO-USE EXPLANATION AND CRYPTANALYSIS


# A. CRYPT ANALYSIS

#In this question, we need to decrypt message with unknown algorithm and the key = 20
#With the key =20 ⇒ we are sure that the message was not encrypted with Random Substitution and Vernam because those 2 algorithms provide the key in string of letters, not specific number
# ⇒ We therefore only need to test with Ceaser Cipher and Columnar Transposition
#With Ceaser, we do not get any message with the key = 20. Below is what we get when decrypt with Ceaser + key=20 :

# '-6""'6".,276:624(,'3U0XJYZ)-IY!()U"7.!,YYW!6'YW.6!",?-X4
# 6!?66
# "!,)?6,(-"6U'"UWU,1",WY
# Y6.?'UU'-"4
# 6YX?(X6"(;
# -
# -(,Y!.'6-0Y'6-V)U,)6?W06Y0

# 6?0 "6YY6-Y,"
# ?6!U,(,)VY0','"X".0;(XY6.6
# U7'Y;"!,16YY
# 6(--!Z,
# 6
# UX-UY6
# Y'-W66-,6--Y?"66"Y
# ,1,-0,'
# Y!W-!.()UU
# YW()6
# -(6
# 0
# 661,W X-46-2Y
# ZU?,)X.XY(! Y6Y2!-0!(YX66Y
# D,
# (6"6
# 6
# 6Y,06"'''V
# .6,XZU'Y,
# -!V-HYY6Z6,6?)"WU6YU-Y.!I1YZ
# ""-.
# 6U
# "X3
# ,YX0',6U-)6X"-!6
# Y-,Y,6
# Y"""Y6 ?U-)Y-!W
# XU20.Y'.''
# W'
# ?Y66?Y
# YY;,?-,16,,6;!U,ZUU,"",74'',UYX'.6'Y
# (
# 1,"1!,,'
# ?,61U,6U66!--'W6UY2,6Y!,YX0Y-)-;,"W!Y(
# Z(61 "
# Y,W
# !,Y!64Z'Y?"U? D!6,Z664!66,'.Y6Z!Y'
# --?Y4""Y6(!6'-.U6V'6'Y6YU,'Y,06Y.W6''8,6'U6'"Y7U(WY016)6
# )?--W'

# 6YU!"6
# W16Y
#
#UJ16!Y-,??6J

#We therefore, continue to test with Columnar Transposition + key=20. Now we get decrypted message:

#RMIT UNIVERSITY VIETNAM PROVIDES PROGRAM SPECIFIC INTERNSHIPS. DURING THE INTERNSHIP STUDENTS ARE ENROLLED INTO SPECIFIC INDUSTRY-BASED COURSES THAT INTEGRATE THE STUDENT'S THEORETICAL KNOWLEDGE WITH WORKPLACE EXPERIENCE. STUDENTS TAKE ON A RANGE OF FINITE PROJECTS THAT EMPLOYERS CAN HELP IDENTIFY, WHILE RMIT UNIVERSITY VIETNAM PROVIDES CLOSE ACADEMIC SUPERVISION. THIS GIVES A RICHER EDUCATIONAL EXPERIENCE AND IMPORTANT SKILLS MAKING STUDENTS MORE WORK-READY UPON GRADUATION.

#THE INTERNSHIPS HAVE PROVEN BENEFICIAL FOR A PLETHORA OF COMPANIES WHO HAVE BEEN ABLE TO "TRIAL RUN" RMIT UNIVERSITY VIETNAM STUDENTS FOR POSSIBLE OFFICIAL EMPLOYMENT LATER.


#B. PROGRAM HOW-TO-USE EXPLANATION

#In this program, we need to notice 3 parts:

#   1. key= 20:
#       We input number 20 here because the given key is 20

#   2. Ceaser Part: Below is the Ceaser Part to test decrypting message 3 with Ceaser + Key 20. This Part is in commented mode. To use it, We need to uncomment all lines below:

#       #ceaser=''
#       #ALPHABET LETTERS
#       #alphabet="""ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
#       #for a in message:
#           #if a in alphabet:

#       #### In ceasear, we have 2 situation, shiting forward from A->9 and shifitng backward from 9->A:
#       #       For shifting forward from A->9: decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#       #       For shifting backward from 9->A: decrypt += alphabet[(alphabet.index(a)- key)%(len(alphabet))]
#       #In this case, we test with the situation shifting forward from A->9 first,
#       #so we will use : decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]

#       #ceaser += alphabet[(alphabet.index(a)+key)%(len(alphabet))]


#       #PRINT CEASER DECRYPTED MESSAGE
#       #print('Your CEASER decrypted message is: '+"\n"+"----------------------------------------------------"+"\n"+ceaser +"\n")

#   3. Columnar Transposition Part:
# Below is the Columnar Transposition Part. We use it to test decrypting message 3 with Columnar Transposition + Key 20.

#           columnar=''


#           for i in range (int(len(message)/key)):
#              for a in range (key):
#                  columnar += message[i+(a*(int(len(message)/key)))]


#           print('Your COLUMNAR decrypted message is: '+"\n"+"----------------------------------------------------"+"\n"+columnar)





######################################################################################################################



###BELOW IS THE SOURCE CODE TO DECRYPT MESSAGE 3



#OPEN FILE "MSG3.ENC" , REMOVE "<" AND ">" AND CONVERT ALL LETTERS INTO UPPERCASE


file = open('msg3.enc', 'r')
s = file.read()
s1 = s.replace("<","")
message1 = s1.replace('>','')
message = message1.upper()

###

##WE INPUT NUMBER 20 BELOW AS THE GIVEN KEY = 20
key= 20
###

#CREATE STRING TO STORE DECRYPTED MESSAGE
columnar=''

#PLEASE UNCOMMENT THE LINE BELOW WHEN TESTING CEASER CIPHER
#ceaser=''


################


###########PLEASE ONLY UNCOMMENT THE BELOW PART (BETWEEN ########  AND ###### ) TO TEST CEASER CIPHER ONLY##################


#FUNCTION TO DECRYPT CEASER CIPHER


#ALPHABET LETTERS

#alphabet="""ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""


#for a in message:
#   if a in alphabet:

#### In ceasear, we have 2 situation, shiting forward from A->9 and shifitng backward from 9->A:
#           For shifting forward from A->9: decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]
#           For shifting backward from 9->A: decrypt += alphabet[(alphabet.index(a)- key)%(len(alphabet))]
#       In this case, we test with the situation shifting forward from A->9 first,
#       so we will use : decrypt += alphabet[(alphabet.index(a)+key)%(len(alphabet))]

#        ceaser += alphabet[(alphabet.index(a)+key)%(len(alphabet))]


#PRINT CEASER DECRYPTED MESSAGE
#print('Your CEASER decrypted message is: '+"\n"+"----------------------------------------------------"+"\n"+ceaser +"\n")

#print("#############################################################################"+"\n")


###########PLEASE ONLY UNCOMMENT THIS PART (BETWEEN ########  AND ###### ) TO TEST CEASER CIPHER ONLY##################


############


# FUNCTION TO DECRYPT COLUMNAR TRANSPOSITION

for i in range (int(len(message)/key)):
    for a in range (key):
        columnar += message[i+(a*(int(len(message)/key)))]

#PRINT COLUMNAR TRANSPOSITION DECRYPTED MESSAGE
print('Your COLUMNAR decrypted message is: '+"\n"+"----------------------------------------------------"+"\n"+columnar)

#CLOSE FILE
file.close()

####################################################################################
