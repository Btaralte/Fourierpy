import numpy as np 
import matplotlib.pyplot as plt
n = int(input("Enter upto how much term you want the infinite series to be approximated:"))
def function(x):
    sum = 0
    for i in range(0,n):
        sum = sum + (4/np.pi)*np.sin((2*i + 1)*x)/(2*i + 1)
    return sum
y = []
x = list(np.linspace(-2*np.pi,2*np.pi,100))
for i in range(0,len(x)):
    y.append(function(x[i]))
plt.plot(x,y)
plt.title("Fourier series visualisation for a rectangular waveform")    
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
    

