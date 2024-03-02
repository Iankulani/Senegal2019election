# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 03:33:04 2024

@author: IAN CARTER KULANI
"""
# -*- coding: utf-8 -*-
#This software prompts the user to enter total number of published centers,total number of registered votes, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward, it determines the candidate with the majority of votes and displays the results on the screen.
#NOTE:For a candidate to be a majority winner the candidate total valid votes should be greater than majority votes.

print("=================================SENEGAL ELECTION=================================\n")

Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
#Get Total number of votes cast
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes for All candidates
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get total valid votes for Macky Sall
Totalvalidvotesfor_MackySall=int(input("Enter Total Valid Votes for Macky Sall:"))
#Get total valid votes for Idrissa Seck
Totalvalidvotesfor_IdrissaSeck=int(input("Enter Total Valid Votes for Idrissa Seck:"))
#Get total valid votes for Ousmane Sonko
Totalvalidvotesfor_OusmaneSonko=int(input("Enter Total Valid Votes for Ousmane Sonko:"))
#Get total valid votes for Issa Sall
Totalvalidvotesfor_IssaSall=int(input("Enter Total Valid Votes for Issa Sall:"))
#Get total valid votes for Madicke Niang
Totalvalidvotesfor_MadickeNiang=int(input("Enter Total Valid Votes for Madicke Niang:"))
percent=100

if Totalvalidvotesfor_MackySall>Totalvalidvotes/2+1:
   print("congratulations Macky Sall You're the winner of 2019 Presiential Election\n\n")

#
elif Totalvalidvotesfor_IdrissaSeck>Totalvalidvotes/2+1:
   print("congratulations Idrissa Seck You're the winner of 2019 Presiential Election\n\n")

#
elif Totalvalidvotesfor_OusmaneSonko>Totalvalidvotes/2+1:
   print("congratulations Ousmane Sonko You're the winner of 2019 Presiential Election\n\n")

#
elif Totalvalidvotesfor_IssaSall>Totalvalidvotes/2+1:
   print("congratulations Issa Sall You're the winner of 2019 Presiential Election\n\n")
#
elif Totalvalidvotesfor_MadickeNiang>Totalvalidvotes/2+1:
     print("congratulations Madicke Niang You're the winner of 2019 Presiential Election\n\n")
#
else:
      print("No majority winner was found RUNOF may be required Thank you.\n\n")

#

print("____________________________________ELECTION STATISTICS___________________________________\n")      

#Calculating percentage


percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",percentage)
#Calculating percentage for total votes cast
percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",percentage)
#Calculating percentage for null_&_void votes
percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void in percentage=",percentage)
#Calculating percentage for Total Registered voters/turnout
percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",percentage)
#Calculating percentage for Macky Sall
percentage=round(Totalvalidvotesfor_MackySall*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Macky Sall in percentage=",percentage)
#Calculating percentage for Idrissa Seck 
percentage=round(Totalvalidvotesfor_IdrissaSeck*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Idrissa Seck in percentage=",percentage)
#Calculating percentage for Ousmane Sonko
percentage=round(Totalvalidvotesfor_OusmaneSonko*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Ousmane Sonko in percentage=",percentage)
#Calculating percentage for Issa Sall
percentage=round(Totalvalidvotesfor_IssaSall*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Issa Sall in percentage=",percentage)
#Calculating percentage for Madicke Niang
percentage=round(Totalvalidvotesfor_MadickeNiang*percent/Totalvalidvotes, 2);
print("Total Valid Votes For Madicke Niang in percentage=",percentage)
#
print("============================================================================================")








