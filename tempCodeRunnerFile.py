# many bottles each person receives
total_bottles = int(input())
number_of_people = int(input())
bottles_recieve = total_bottles // number_of_people
bottles_remain = total_bottles % number_of_people
print(bottles_recieve , bottles_remain)