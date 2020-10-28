import pandas as pd

data = pd.read_csv(r'C:\Users\alber\Desktop\SHIT.csv', index_col='Time')
Ydata = pd.DataFrame(data, columns= ['Data'])



#print(Ydata['Data'][0])
#print(data.index[0])
#print(Ydata)

#RocketData = Ydata['Data']
#TimeData = data.index


Xvalues = []
for x in data.index:
    Xvalues.append(x)
    pass


Yvalues = []
for x in Ydata['Data']:
    Yvalues.append(x)
    pass



print(Xvalues)
print('shit')
print(Yvalues)
