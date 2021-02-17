power = 5
upperbound = len(str(len(str(9**power))*(9**5)))*(9**power) + 1

def calculate_digit_power_sum(n):
  s = 0
  while(n):
    digit = n % 10
    s += digit**power
    n //= 10
  return s

s = 0
for i in range(2, upperbound):
  if ( i == calculate_digit_power_sum(i) ):
    s += i

print(s)