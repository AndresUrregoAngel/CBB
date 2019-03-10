import glob
from numpy import genfromtxt
#import matplotlib.pyplot as plt
from matplotlib.pyplot import *

def avarage(file):
    acumulate = 0
    for number in file:
        acumulate += number
    return acumulate / len(file)


path = "E:\\Sources\\data\\*.csv"
files = glob.glob(path)

for i in files:
    my_data = genfromtxt(i, delimiter=',')
    #print(i)


figure(1)
subplot(131)
plot(my_data.mean(axis=0))
axis([0,40,0,20])
ylabel('mean')
subplot(132)
plot(my_data.min(axis=0))
axis([0,40,0,20])
ylabel('min')
subplot(133)
plot(my_data.max(axis=0))
axis([0,40,0,20])
ylabel('max')
