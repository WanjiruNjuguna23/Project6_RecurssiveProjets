class Math:

    #def __init__(self,

    def power(self, base, exp):
        if (exp == 1):  # if the exponential power is equal to 1, the base
            # number is returned
            return(base)
        if (exp != 1):  # if the exponential power isn't equal to 1,
            # the base number multiplied with the power function is called
            # recursivelu with the arguments as the base and power minus 1
            return(base*self.power(base,exp-1))
        #base = int(input("Enter base: "))
        #exp = int(input("Enter exponential value: "))
        ##print("Result: ", power(base, exp))

    def baseConversion(self, base, exp):
        # base case
        if 0<= base < exp:
            return str(base)
        #recursive cases
        else:
            return self.baseConversion(base//exp, exp) + '' + str(base%exp)

    def recur_factorial(self, exp):
        if exp == 1:
            return exp
        else:
            return exp*self.recur_factorial(exp-1)

    def combination(self,n, k):
        if k == 1:
            return n
        elif n<k:
            return 0
        else: #recursive case
            return self.combination(n-1, k-1) + self.combination(n-1, k)


if __name__ == "__main__":
    main()
