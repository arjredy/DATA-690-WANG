#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# Prompts a user to enter 10 integers. If the user enters anything other than integers, remind her that only integers are allowed and let her retry. Don't allow the user to enter more than 10 or less than 10 integers. Display the 10 integers back to the user at the end. Calculate the following statistics from the 10 integers entered:
# 
# 1. Minimum
# 
# 2. Maximum
# 
# 3. Range
# 
# 4. Mean
# 
# 5. Variance
# 
# 6. Standard Deviation

# In[1]:


# Import math Library
import math


# In[2]:


# Function to accept the input
def askInput():
  return list(map(int,input("Please enter 10 integers seperated by a space\n").split()))

# Function to find the mean
def mean(elements):
  return sum(elements)/len(elements)

# Function to find the SD
def standard_deviation(variance):
  return math.sqrt(variance)

# Function to find the Variance
def variance(elements,mean_value):
  result = 0
  for i in elements:
    result+= (i-mean_value)*(i-mean_value)
  return result/len(elements)


# In[3]:


n = 10
try:
  a =  askInput()
except:
  print("*************Only Integers are allowed. Please try again*****************\n")
  a = askInput()
if len(a)!=10:
  print("Required 10 integers. Please try again")
else: 
  print("Displaying Entered Elements\n")
  for i in a:
    print(i,end=" ")
  print("\n")
  print("Minimum Value in the list: ",str(min(a))+"\n")
  print("Maximum Value in the list: ",str(max(a))+"\n")
  print("Range: ",(min(a),max(a)),"\n")
  mean_value = mean(a)
  print("Mean of elements: ",mean_value,"\n")
  variance_value = variance(a,mean_value)
  print("Variance: %s"%(variance_value))
  print("Standard Deviation: %s"%(standard_deviation(variance_value)))
      
    # print("Please enter integers")

