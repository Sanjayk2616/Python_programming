""" 
operators
an operator is a symbol which is used to perform a task

Types of operators
1)Arthimetic operators
  + -> addition
  - -> subtraction
  * -> multiplication
  % -> remainder(modulus)
  / -> division(float)
  // -> floor divisor(int)
  ** -> exponent(power of)



"""
a = 2
b = 3
print(a//b)

#q1
#write a program take the input from the user and print the area , perimeter of rectangle square triangle circle
length = float(input())
breadth = float(input())
area = length * breadth
perimeter = 2*(length + breadth)
print(area)
print(perimeter)

side = float(input())
area = side**2
perimeter = 4*side
print(area)
print(perimeter)

b = float(input())
h = float(input())
x = float(input())
y = float(input())
z = float(input())
area = (b*h)/2
perimeter = x + y + z
print(area)
print(perimeter)

r = float(input())
area = 3.14*(r**2)
perimeter = 2 * 3.14 * r
print(area)
print(perimeter)

#shopping bill calculation
#books b
#file f        are products
#pens p

b_price = float(input())
b_quan = int(input())

f_price = float(input())
f_quan = int(input())

p_price = float(input())
p_quan = int(input())

bill = ((b_price*b_quan)+(p_price*p_quan)+(f_price*f_quan))
print(bill)

#atm withdrawal
account_balance = float(input())
withdrawal_amount = float(input())
account_balance = account_balance - withdrawal_amount
print(account_balance)

#students marks average
subject1 = int(input())
subject2 = int(input())
subject3 = int(input())
subject4 = int(input())
subject5 = int(input())
sum = subject1 + subject2 + subject3 + subject4 + subject5
print(sum/5)

#salary calculation
basic_salary = int(input())
bonus = int(input())
final_salary = basic_salary + bonus
print(final_salary)


#fuel cost calculation
distance = float(input())
mileage = float(input())
fuel_price = float(input())
print(mileage*fuel_price)

#chocolate distribution
total_chocolates = int(input())
total_students = int(input())
per_student = (total_chocolates // total_students)
remain = (total_chocolates % total_students)
print(per_student,remain)

#restaurant bill splitting
total_bill = float(input())
no_of_friends = int(input)
bill_per_person = (total_bill/no_of_friends)
print(bill_per_person)

#electricity bill
units_consumed = int(input())
price_per_unit = int(input())
electricity_bill = units_consumed*price_per_unit
print(electricity_bill)

#discount calculation
original_price = float(input())
discount = float(input())
final_price = (original_price - (discount * original_price))
print(final_price)

#time conversion
total_seconds = int(input())
minutes = total_seconds / 60
remaining_seconds = total_seconds % 60
print(minutes,remaining_seconds)

#monthly savings
monthly_salary = float(input())
monthly_expenses = float(input())
savings = monthly_salary - monthly_expenses
print(savings)

#simple intrest calculation
# principal_amount p, interest_rate i, time_period t
p = int(input())
i = float(input())
t = float(input())
simple_intrest = (p*i*t)/100
print(simple_intrest)

#calculate complete weeks and remaining days
total_days = int(input())
complete_weeks = total_days // 7
remaining_days = total_days % 7
print(complete_weeks)
print(remaining_days)

# total ticket cost
ticket_price = float(input())
number_of_tickets = int(input())
total_cost = (ticket_price * number_of_tickets)
print(total_cost)

# final product price
product_price = float(input())
gst = float(input())
final_price = product_price * (1 + (gst/100))
print(final_price)

# extracting  last two digits
transaction_id = int(input())
print(transaction_id % 100)

#number of buses required 
total_students = int(input())
bus_capacity = int(input())
no_of_buses = (total_students / bus_capacity)

"""total earnongs
number_of_deliveries nd
payment_per_delivery pd
 """
nd = int(input())
pd = float(input())
print(nd * pd)

# remaining storage space
total_storage = float(input())
file_size = float(input())
number_of_files = float(input())
print(total_storage - (file_size * number_of_files))

# many bottles each person receives
total_bottles = int(input())
number_of_people = int(input())
bottles_recieve = total_bottles // number_of_people
bottles_remain = total_bottles % number_of_people
print(bottles_recieve , bottles_remain)
