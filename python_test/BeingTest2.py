class num2test(object):
    def print_Multiplication_table(self):
        for i in range(1,10):
            for j  in range(1,i+1):
                print ' %s * %s = %s ' % (i,j,i*j),
                if i == j:
                    print '\n'
