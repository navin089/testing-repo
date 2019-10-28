#PF-Assgn-20
# A SIMPLE BANKING MANAGEMENT SYSTEM EXAMPLE ---
import pandas as pd
import numpy as np
import scipy as sp
def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    #Start writing your code here
    if (account_number//1000)==1 :
        if account_balance>100000 :
            if loan_type=="Car" and salary>25000 :
                if loan_amount_expected<=500000 and customer_emi_expected<=36 :
                    eligible_loan_amount=500000
                    bank_emi_expected=36
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else :
                    print("The customer is not eligible for the loan")
            elif loan_type=="House" and salary>50000 :
                eligible_loan_amount=6000000
                if loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=60 :
                    bank_emi_expected=60
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else :
                    print("The customer is not eligible for the loan")
           elif loan_type=="Business" and salary>75000 :
                eligible_loan_amount=7500000
                if loan_amount_expected<=eligible_loan_amount and customer_emi_expected<=84 :
                    bank_emi_expected=84
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else :
                   print("The customer is not eligible for the loan") 
            else :
                print("Invalid loan type or salary")
        else :
           print("Insufficient account balance") 
    else :
        print("Invalid account number")
    
    #Populate the variables: eligible_loan_amount and bank_emi_expected
calculate_loan(1005,90000,255000,"Business",7200000,80)
    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results


