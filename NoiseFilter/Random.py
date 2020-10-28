import math
import matplotlib.pyplot as plt
import numpy as np



#Generate random data with noise, array is alled "Yarray"
#############################################################################
sample_rate = 50  # 50 Hz resolution
signal_lenght = 10*sample_rate  # 10 seconds
# Generate a random Yarray(t) signal with waves and noise. 
t = np.linspace(0, 10, signal_lenght)
g = 30*( np.sin((t/10)**2) )
Yarray  = 0.30*np.cos(2*np.pi*0.25*t - 0.2) 
Yarray += 0.28*np.sin(2*np.pi*1.50*t + 1.0)
Yarray += 0.10*np.sin(2*np.pi*5.85*g + 1.0)
Yarray += 0.09*np.cos(2*np.pi*10.0*t)
Yarray += 0.04*np.sin(2*np.pi*20.0*t)
Yarray += 0.15*np.cos(2*np.pi*135.0*(t/5.0-1)**2)
Yarray += 0.04*np.random.randn(len(t))
# Normalize between -0.5 to 0.5: 
Yarray -= np.min(Yarray)
Yarray /= np.max(Yarray)
Yarray -= 0.5
##############################################################################

print("Yarray: ", Yarray)
from scipy.stats import t

#Choose your input variables 
SampSze = 10                              #Sample Size 
confidence = .95                          #%confidence 

#Create X-Axis arrays
xxx = np.arange(0, len(Yarray), 1)                              #X-Axis time array for actual data
SimpXarray = np.arange(SampSze/2, len(Yarray), SampSze)         #X-Axis time array for UB, LB, Mean data

print("SimpXarray: ", SimpXarray)

#Initialize Variables 
UB = []                                
LB = []   
AvgArry = []
TempArray = []
Count = 0
Itr = SampSze
NumeratorArray = []

#Build UB and LB Arrays
while Count <= len(Yarray) - 1:
    
    TempArray.append(Yarray[Count])
       
    if Count == (Itr - 1):
        #print(Itr - SampSze, "-", Itr, " TempArray: ", TempArray)       
        mean = sum(TempArray) / len(TempArray)      
        #print("mean: ", mean)

        #Calculate Standard Deviation
        for n in TempArray:
            num = abs(n - mean)
            numnum = num**2
            NumeratorArray.append(numnum) 
            pass
        SD = math.sqrt(sum(NumeratorArray) / len(NumeratorArray))
        #print("Standard Dev: ", SD)

        a = 1 - confidence                     #A-Value
        p = a/2 + confidence                   #probability 
        df = SampSze - 1                       #degrees of freedom
        Tvalue = t.ppf(p, df)                  #T-Value 
        StdErr = SD/math.sqrt(SampSze)         #Standard Error
        Bound = Tvalue*StdErr                  # +/- Bound
        UpperBound = mean + Bound              #Upper Bound
        LowerBound = mean - Bound              #Lower Bound

        AvgArry.append(mean)
        UB.append(UpperBound)
        LB.append(LowerBound)

        #print("Bound ", Bound)
        #print("UpperBound ", UpperBound)
        #print("LowerBound ", LowerBound)

        Itr = Itr + SampSze
        TempArray = []
        NumeratorArray = []
        pass

    #print("  ")
    Count = Count + 1
    pass

print("length of data points: ", len(Yarray))
print("length of SimpXarray: ", len(SimpXarray))
#this length needs to be the same length of the new X array we trying to create
#from there, we need to go pick out the times wanted from the index of that array 

plt.figure(figsize=(11, 9))
plt.plot(xxx, Yarray, 'k')
plt.plot(SimpXarray, UB, 'r--', label="Upper Bound")
plt.plot(SimpXarray, LB, 'r--', label="Lower Bound")
plt.plot(SimpXarray, AvgArry, 'b--', label="Average")
plt.title("Filtering Shit")
plt.xlabel('Time (500 points)')
plt.ylabel('Random SimpXarray data')
plt.legend()
plt.show()
