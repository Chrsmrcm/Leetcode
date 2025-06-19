'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
-Starting with any positive integer, replace the number by the sum of the squares of its digits.
-Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
-Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
def isHappy(self, n: int) -> bool:
    hashmap = {}
    #teehee
    unhappy = True
    while unhappy:

        if n == 1:
            return True

        #split, square and sum
        n = self.parse(n)
        #check if sum is a previous sum therefore a loop
        loop = hashmap.get(n,0)
        if loop > 0:
            return False
        #else add it to the hashmap
        else:
            hashmap[n] = 1            

def parse(self,number:int) -> int:
    val = 0
    for number in (list(str(number))):
        val += int(number)**2
    return val