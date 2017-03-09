'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.

def interest(balance, iteration):
    balance += balance * .2/12
    if iteration < 7:
        interest(balance, iteration +1)
    if iteration == 6:
        print('Your balance is:', round(balance,2), 'after', iteration, 'months.')

interest(10000, 1)
#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.

def interest2(balance, iteration):
    balance += balance *.2/12
    balance -= 100
    if iteration < 37:
        interest2(balance, iteration + 1)
    if iteration == 36:
        print('Your balance is:', round(balance, 2), 'after', iteration, 'months.')

interest2(5000, 1)

#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.
#write an exception for it

def pay_off(payment, balance, iteration):
    balance += balance * 0.2/12
    balance -= 100
    if balance <= 0:
        payment = True
        print('You payed your balance off after', iteration,' months.')
    if not payment:
        try:
            pay_off(False, balance, iteration + 1)
        except:
            print('Your balance has not been payed off after:', iteration, 'months.')


pay_off(False, 10000, 1)



#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on.  Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.

def total(boxes, iteration, rows):
    if iteration == 0:
        boxes = 0
    boxes += rows
    if rows > 0:
        total(boxes, iteration + 1, rows-1)
    if rows == 0:
        print('There are', boxes, 'boxes in the pyramid.')

total(0, 0, int(input('Enter the number of rows in your pyramid: ')))