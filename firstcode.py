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

    #this function takes two parameters a and b and calls Algorithm function to calculate GCD of a and b
    def my_print (self,a,b):
        print(f"GCD of {a} and {b} : {self.Algorithm(a,b)}")
        #printing GCD
def main():
    obj = EAlgorithm()
    obj.my_print(12,15)

if __name__ == "__main__":
  main()
