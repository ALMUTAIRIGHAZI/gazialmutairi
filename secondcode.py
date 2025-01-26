#performing encapsulation by creating a class to hold functions to perform Euclidean Algorithm
class EAlgorithm:
    def __init__(self):
        pass
    # this function perform the Euclidean Algorithm to determine GCD of two positive numbers
    # @param – a and b; are two positive integers
    # @return- the greatest common divisor of a and b
    #this function calculates GCD of a and b by repeatedly finding the mod of a/b division where b is
    # the remainder form previous division , this continues until remainder is zero and returns a
    def Algorithm (self,a,b):
        if ( a == 0 ):
             return b
        elif (b ==0):
             return a
        else:
            for i in range(1,a+1): #infite loop to calculate GCD, the loop will stop when the if condition becomes true
                if b==0: #the base condition
                   return a
                a,b = b,a%b #performing the algorithm of Euclidean Algorithm, for next iteration a becomes b (the remainder from
           #prevoius division) and b becomes remainder of current division
        return a
    #this function takes input from user and call the Algorithm function to calculate
    #gcd of inputs
    def users_input(self):
        a = int(input("Enter the first positive integer: "))
        if a < 0:
            raise ValueError("a must be positive") #throwing error if number is negative
        b = int(input("Enter the second positive integer: "))
        if b < 0:
            raise ValueError("b must be positive")
        print(f"GCD of {a} and {b} : {self.Algorithm(a, b)}")
def main():
    obj = EAlgorithm()
    obj.users_input()
if __name__ == "__main__":
  main()
