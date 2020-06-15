#import numpy and matplotlib
import numpy as np  
import matplotlib.pyplot as plt  
import random
import time
	
#load the dataset  
train_data = np.genfromtxt('dataset.csv', delimiter=',')

#remove the header row 
train_data = np.delete(train_data,0,0)  

#take SAT Score as X vector 
X = train_data[:,0] 
#take GPA as Y vector 
Y = train_data[:,1]  

#visualize data using matplotlib  
plt.scatter(X,Y) 
plt.xlabel('SAT Score')
plt.ylabel('GPA') 
#plt.show() 

#initialize m and c
#m=0
#c=0
m = random.random()
c = random.random()

L = 0.0001  # The learning Rate 
iterations = 1000  # The number of iterations to perform gradient descent   

n = float(len(X)) # Number of elements in X   

# Performing Gradient Descent  
for i in range(iterations):      
	Y_pred = m*X + c  # The current predicted value of Y     
	#D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative with respect to m     
	#D_c = (-2/n) * sum(Y - Y_pred)  # Derivative with respect to c     
	
	D_m =(-1/n)*sum(X*(Y-Y_pred)/abs(Y - Y_pred)) #Derivative with respect to m     
	D_c=(-1/n)*sum((Y-Y_pred)/abs(Y - Y_pred))# Derivative with respect to c   
	
	m = m - L * D_m  # Update m     
	c = c - L * D_c  # Update c  
	print ("m = ",m) 
	print ("c = ",c)
	
	plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') 	
	plt.pause(1e-17)
	time.sleep(0.1)	
	
	
	
	
#output m and c 
#print ("m = ",m) 
#print ("c = ",c)


#Final predictions 
Y_pred = m*X + c   

#Draw the best fitting line 
#plt.scatter(X, Y)  
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='green') #plot the best line with green color
#plt.xlabel('SAT Score')
#plt.ylabel('GPA')   
plt.show() 
 
  
 