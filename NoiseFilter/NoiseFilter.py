import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Import .csv -- make sure to lable the time column "Time" and the data values "Data"
#data = pd.read_csv(r'C:\Users\alber\Desktop\SHIT.csv', index_col='Time')
data = pd.read_csv(r'C:\Users\alber\Desktop\FuckMe.csv', index_col='Timee')
Ydata = pd.DataFrame(data, columns= ['Data'])

#Generate X-array form .csv
Xarray = []
for x in data.index:
    Xarray.append(x)
    pass

#Generate Y-array from .csv
Yarray = []
for x in Ydata['Data']:
    Yarray.append(x)
    pass


from scipy.stats import t

#Choose your input variables 
SampSze = 10         #Sample Size 
confidence = .95     #%confidence 


LenOfSimpXarray = len(Yarray)/SampSze    #theoretical length of simple X array to create


#do we want this rounding function??
start = math.ceil(SampSze/2 + Xarray[0])
pointsToCollect = np.arange(start, len(Xarray), SampSze)

#create an array for the x-axis to plot against the UB, LB, and AvgArry. This uses actual time values- just not all time values bc we are plotting an avg of Y-data before and after this time value
SimpXarray = []
for x in pointsToCollect:
    SimpXarray.append(Xarray[x])
    pass

print("pointsToCollect: ", pointsToCollect)
print("SimpXArray: ", SimpXarray)
print("   ")




#Initialize Variables/Arrays
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
        print(Itr - SampSze, "-", Itr, " TempArray: ", TempArray)       
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


        #create arrays 
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


#print("SimpXarray pre pop: ", SimpXarray)


#if indexes do not match up before plotting, we can just delete the last value of an index so plotting works
last = len(SimpXarray) - 1
if len(AvgArry) != len(SimpXarray):
    SimpXarray.pop(last)
    pass



print("SimpXarray post pop: ", SimpXarray)
print(" ")
print("AvgArry: ", AvgArry)
print(" ")
print("Xarray: ", Xarray)
print(" ")
print("Yarray: ", Yarray)


#print("Theoretical Len SimpXarray: ", LenOfSimpXarray)
#print("Len SimpXarray: ", len(SimpXarray))
#print("Len Xarray: ", len(Xarray))
#print("Len Yarray: ", len(Yarray))
#print("Len UB: ", len(UB))
#print("Len LB: ", len(LB))
#print("Len AvgArry: ", len(AvgArry))



plt.figure(figsize=(11, 9))
plt.plot(Xarray, Yarray, 'k')
plt.plot(SimpXarray, UB, 'r--', label="Upper Bound")
plt.plot(SimpXarray, LB, 'r--', label="Lower Bound")
plt.plot(SimpXarray, AvgArry, 'b--', label="Average")
plt.title("Filtering Shit")
plt.xlabel('Time')
plt.ylabel('Random SimpXarray data')
plt.legend()
plt.show()
