import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import requests
import pandas as pd
data = pd.read_csv("F:\\Downloads\\case.csv")
# print(data)
X = data.iloc[51:,1]
Y = data.iloc[51:,3].values
D = data.iloc[51:,5].values  
X = data.iloc[51:,0]  
# print(Y)
plt.figure(figsize = (24,8))
ax = plt.axes()
ax.grid(linewidth = 0.4, color = "#8f8f8f")
ax.set_facecolor("black")
ax.set_xlabel("\nDate:",color='#4bb4f2', size = 13)
ax.set_ylabel("No. of Total cases:",color='#4bb4f2', size = 24)
# plt.xticks(rotation='vertical',size='20',color='white')
# plt.yticks(size=20,color='white')
plt.tick_params(size=20,color='white')
for i,j in zip(X,Y):
    ax.annotate(str(j),xy=(i,j+40),
                color='white',size='13')
ax.plot(X,Y, marker = "o",color='#1F77B4', markersize = 7, linewidth=4,markeredgecolor='#035E9B')
plt.show()