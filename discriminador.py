import numpy as np
import scipy as sp
#import matplotlib.pyplot as plt

class Filter(object):

    def __init__(self, s, h, n, lr = 0.99999999993):
        self.s = np.mat(s)
        self.h = np.mat(h)
        self.ht = np.transpose(h)
        self.x = np.dot(self.s,self.ht)
        self.w = np.zeros(self.x.shape)
        self.wt = np.transpose(self.w)
        self.lr = lr
        self.epocs = n
        self.tam = np.size(self.x)

    def lms(self):
        num_epochs = 0
        error = False
        while num_epochs <= self.epocs:
            for i in range(0,self.tam):
                #y = np.dot(self.x,self.wt)
                y = self.x @ self.wt
                #print(y)
                #print(self.s[i])
                #if all(y[0] != self.s[i]):
                
                todos_diferentes = True
                for blbl in self.s:
                    
                    if blbl.item(0) >= y.item(0): # <= 0.00002:
                        todos_diferentes = False
                       # print("trueeeee")

                print(y.item(0), blbl.item(0))
                #print("fdssssssss")
                if todos_diferentes:    
                    self.w[i] = self.w[i] + self.lr*(self.s[i] - y)*self.x[i]
                  
                else:
                    self.w[i] = self.w[i] +  self.lr*(self.s[i] - y)*self.x[i]
                    break

            num_epochs += 1
            print(num_epochs)
        print(self.w)
        print(num_epochs)


    # n = 10
    # lr = 0.01
    #
    # for i in range (0, n):
    #     e = s - y
    #     w[i] = w[i] + lr*e*x[i]
