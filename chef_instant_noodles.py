"""Chef and Instant Noodles
Chef has invented
1-minute Instant Noodles. As the name suggests, each packet takes exactly
1 minute to cook.
Chef's restaurant has X stoves and only 1 packet can be cooked in a single stove
at any minute.
How many customers can Chef serve in Y minutes if each customer orders exactly
1 packet of noodles?


Input Format
The first and only line of input contains two space-separated integers
X and
Y — the number of stoves and the number of minutes, respectively.
Output Format
Print a single integer, the maximum number of customers Chef can serve in
Y minutes"""

# Read input
X, Y = map(int, input().split())
total_customers = X * Y
print(total_customers)




languages = int(input())
courses_per_language = 2
total_courses = languages * courses_per_language
print(total_courses)



