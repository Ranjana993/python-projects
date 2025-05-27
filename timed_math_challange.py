import random
import time



OPERATOR = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PRPBLEMS = 5

def generate_problem():
  left = random.randint(MIN_OPERAND, MAX_OPERAND)
  right = random.randint(MIN_OPERAND, MAX_OPERAND)
  operator = random.choice(OPERATOR)

  expresssion = str(left) +" " + operator + " " + str(right)
  ans = eval(expresssion)
  return expresssion, ans

wrong = 0 
print("Welcome to the Timed Math Challenge!")
print("-------------------------------------------------")

start_time = time.time()
for i in range(TOTAL_PRPBLEMS):
  expression , ans = generate_problem()
  print("Problem#" + str(i+1) + ": " + expression)
  user_ans = int(input("Enter your answer: "))
  if user_ans == ans:
    print("Correct!")
  else:
    print("Incorrect! The correct answer is: " + str(ans))
    wrong+=1


end_time = time.time()
total_time = round(end_time - start_time ,2)
print("-----------------------------------------------")    
print("Challenge completed!")
print("You answered " + str(TOTAL_PRPBLEMS - wrong) + " out of " + str(TOTAL_PRPBLEMS) + " problems correctly.")
print("Total time taken: " + str(total_time) + " seconds.")
