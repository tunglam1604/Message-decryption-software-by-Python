#QUESTION 2
#Rmit University - Semester 2, 2017
#COSC2539 - Security in Computing and Information Technology
#Instructor: Denis Rinfret
#Date: August 5th, 2017
#Conductors: Tung Lam Minh - s3598768 & Tuan Huynh Doan - s3463207

######################################################################################################################

#PROGRAM HOW-TO-USE EXPLANATION AND CRYPTANALYSIS

# A. CRYPTANALYSIS

#In this question, we need to decrypt message with algorithm: Columnar Transposition and the key: unknown.
# However, we know 1 thing that in Columnar Transposition, the key is the divisor of the message length .
#In message 2, the length of message is 882
# ⇒ key is the divisor of 882 = {1   2    3    6    7    9  14    18     21     42     49     63     98    126    147    294    441    882 }

#Also, the number of rows = length of message ( 882)  / key

#We then test with all possible keys above until we can find the correct key ( correct key = 18)

#With correct key = 18, we get decrypted message as below

#HEALTH CARE SERVICES AND SAFETY CONCERN

#MOVING AWAY FROM HOME, THE ALTERATIONS IN CLIMATE, IN LIVING ENVIRONMENT ARE SIGNIFICANT FACTORS AFFECTING ONE'S HEALTH CONDITION. IT IS IMPORTANT FOR INTERNATIONAL STUDENTS TO TAKE CARE OF THEIR HEALTH. IT IS RECOMMENDED THAT BEFORE TRAVELLING TO VIETNAM, YOU SHOULD PURCHASE PRIVATE HEALTH INSURANCE TO HELP COVER THE COST OF TREATMENT AT PRIVATE HEALTHCARE ESTABLISHMENTS.

#AMONG THE WIDE RANGE OF HOSPITALS AND DIFFERENT STANDARDS OF HEALTHCARE, PRIVATE HOSPITALS ARE GENERALLY ON PAR WITH THOSE IN THE WESTERN COUNTRIES AND  ACCEPT INTERNATIONAL HEALTH INSURANCE. THE MAJORITY OF DOCTORS ARE FROM THE US, KOREA, JAPAN AND FRANCE, AS WELL AS OVERSEAS-TRAINED VIETNAMESE DOCTORS.

#AT RMIT VIETNAM, THE HEALTH AND SAFETY OF THE STUDENTS IS A TOP PRIORITY. WE HAVE 24-HOUR SECURITY, HEALTH CENTRES AND COUNSELLING SERVICES ON CAMPUS.


# B. PROGRAM HOW-TO-USE EXPLANATION

#In this program, we need to notice 2 parts:

#   1. print("LENGTH OF MESSAGE 2: " + str(len(message))+ "\n"+"-----------------------------------------------------"+"\n")

#       This part is to count the length of message 2 so that we can have all possible keys .
#       After counting, we get the message 2 length = 882

#       ⇒ The key = divisor of 882 =  {1   2    3    6    7    9  14    18     21     42     49     63     98    126    147    294    441    882 }

#       ⇒ Number of rows = length of message 2 (882) / key



#   2. key =18

#       We need to replace number “18” with all possible keys ( 1   2    3    6    7    9  14    18     21     42     49     63     98    126    147    294    441    882 )  for testing purpose. When we get the desire key, we will leave the correct key number (key=18) here

#       ⇒ After testing with all possible keys , we get the decrypted message with the key = 18 and the algorithm : Columnar Transposition




#######################################################################################################################



###BELOW IS THE SOURCE CODE TO DECRYPT MESSAGE 2


#OPEN FILE "MSG2.ENC" , REMOVE "<" AND ">"
file = open('msg2.enc', 'r')
s = file.read()
s1 = s.replace("<","")
message = s1.replace('>','')
#############################

#Replace the key with the divisor of 882 ( because the length of message 2 is 882 ) for testing purpose only.
# After getting the result, please leave the correct key here ( key =18)

#Divisor of 882 = {1	2	3	6	7	9	14	18	21	42	49	63	98	126	147	294	441	882 }

key= 18

###############################################

#CREATE STRING TO STORE DECRYPTED MESSAGE
decrypt=''

######## PRINT LENGTH OF MESSAGE 2

print("LENGTH OF MESSAGE 2: " + str(len(message))+ "\n"+"-----------------------------------------------------"+"\n")
######################

#FUNCTION TO DECRYPT COLUMNAR TRANSPOSITION CIPHER

#Note: the number of rows = length of message ( 882) / key

for i in range (int(len(message)/key)):
    for a in range (key):
        decrypt += message[i+(a*(int(len(message)/key)))]

###PRINT DECRYPTED MESSAGE
print('Your decrypted message is: '+"\n"+"----------------------------------------------------"+"\n"+decrypt)

#CLOSE FILE
file.close()

#######################################################################################################################
