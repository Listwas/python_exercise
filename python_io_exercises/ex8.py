#Format variables using string.format() method
#Write a program to use the string.format() method to format the following three variables according to the expected output.

#Given:
#totalMoney = 1000
#quantity = 3
#price = 450

#Expected Output:
#I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = 1000
quantity = 3
price = 450
string = "I have {0} dollars so I can buy {1} football for {2} dollars."

print(string.format(totalMoney, quantity, price))
