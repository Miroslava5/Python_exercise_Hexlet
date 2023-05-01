

def is_happy_ticket(number):
    if len(number) % 2 != 0:
        return False
    elif number == '':
        return None
    index = 0
    sum1 = 0
    sum2 = 0
    while index < len(number) / 2:
        sum1 += int(number[index])
        sum2 += int(number[-1 - index])
        index += 1 
    return True if sum1 == sum2 else False

print(is_happy_ticket('')) # True
print(is_happy_ticket('0')) # True
print(is_happy_ticket('42')) # False
print(is_happy_ticket('12345678')) # False
     
     #Решения учителя
#def is_happy_ticket(ticket):
 #   balance = 0
  #  middle = len(ticket) // 2
   # for i in range(middle):
    #    balance += int(ticket[i]) - int(ticket[i + middle])
    #return balance == 0


#   Альтернативное решение с помощью zip
#   https://docs.python.org/3.10/library/functions.html#zip
#
#   def is_happy_ticket(ticket):
#       balance = 0
#       middle = len(ticket) // 2
#       for left, right in zip(ticket[:middle], ticket[middle:]):
#           balance += int(left) - int(right)
#       return balance == 0