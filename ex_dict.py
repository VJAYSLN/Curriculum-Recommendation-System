# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:29:05 2018

@author: J N BALAKUMARAN
"""
from math import sqrt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Dataset_for_15mx11={
                            'Alumni':
                                {
                                'Alumni1':4,
                                'Alumni2':5,
                                'Alumni3':5,
                                'Alumni4':4,
                                'Alumni5':5,
                                'Alumni6':5
                                },
                            "industry":
                                {
                                "industry1":4,
                                "industry2":5,
                                "industry3":4,
                                "inudstry4":5,
                                "industry5":4
                                },
                             "student":
                                {
                                "student1":5,
                                "student2":4,
                                "student3":5,
                                "student4":4,
                                "student5":5,
                                "student6":5
                                },
                            "faculty":
                                {
                                "faculty1":5,
                                "faculty2":4,
                                "faculty3":5,
                                "faculty4":5,
                                "faculty5":4,
                                "faculty6":5
                                },
                            "experts":
                                {
                                "expert1":5,
                                "expert2":4,
                                "expert3":4,
                                "expert4":5,
                                "expert5":5
                                }
                            }
dataset=Dataset_for_15mx11        
Dataset_for_15mx12={
                            'Alumni':
                                {
                                'Alumni1':4,
                                'Alumni2':5,
                                'Alumni3':5,
                                'Alumni4':4,
                                'Alumni5':5,
                                'Alumni6':5
                                },
                            "industry":
                                {
                                "industry1":4,
                                "industry2":5,
                                "industry3":4,
                                "inudstry4":5,
                                "industry5":4
                                },
                             "student":
                                {
                                "student1":5,
                                "student2":4,
                                "student3":5,
                                "student4":4,
                                "student5":5,
                                "student6":5
                                },
                            "faculty":
                                {
                                "faculty1":5,
                                "faculty2":4,
                                "faculty3":5,
                                "faculty4":5,
                                "faculty5":4,
                                "faculty6":5
                                },
                            "experts":
                                {
                                "expert1":5,
                                "expert2":4,
                                "expert3":4,
                                "expert4":5,
                                "expert5":5
                                }
                            }
#dataset=Dataset_for_15mx12     
print(dataset)

"""def pearson_correlation(person1,person2):

	# To get both rated items
	both_rated = {}
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item] = 1

	number_of_ratings = len(both_rated)		
	# Checking for number of ratings in common
	if number_of_ratings == 0:
		return 0

	# Add up all the preferences of each user
	person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
	person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])

	# Sum up the squares of preferences of each user
	person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
	person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])

	# Sum up the product value of both preferences for each item
	product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])
    
	# Calculate the pearson score
	numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
	denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))
	if denominator_value == 0:
		return 0
	else:
		 r = numerator_value/denominator_value
		 return r 

def most_similar_users(person,number_of_users):
	# returns the number_of_users (similar persons) for a given specific person.
	scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]

	# Sort the similar persons so that highest scores person will appear at the first
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]

def user_recommendations(person):

	# Gets recommendations for a person by using a weighted average of every other user's rankings
	totals = {}
	simSums = {}
	rankings_list =[]
	for other in dataset:
        
		if other == person:
			continue
		sim = pearson_correlation(person,other)
		if sim <=0: 
			continue
		for item in dataset[other]:

			# only score movies i haven't seen yet
			if item not in dataset[person] or dataset[person][item] == 0:

			# Similrity * score
				totals.setdefault(item,0)
				totals[item] += dataset[other][item]* sim
				# sum of similarities
              
				simSums.setdefault(item,0)
				simSums[item]+= sim
		# Create the normalized list

	rankings = [(total/simSums[item],item) for item,total in totals.items()]
	rankings.sort() 
	rankings.reverse()
	#print(rankings)
    # returns the recommended items
	recommendataions_list = [(recommend_item,score) for score,recommend_item in rankings]
	return recommendataions_list"""
		


#print(dataset)




alu=ind=exp=fac=stu=0
ac=ic=ec=sc=fc=0
for key in dataset:
    for i in dataset[key].values():
        if(key=="Alumni"):
            alu+=i
            ac+=1
        if(key=="industry"):
            ind+=i
            ic+=1
        if(key=="experts"):
            exp+=i
            ec+=1
        if(key=="student"):
            stu+=i
            sc+=1
        if(key=="faculty"):
            fac+=i
            fc+=1
        




print(alu,ind,exp,stu,fac)
mean=[]
print("length of dataset",len(dataset))
mean.append(round((alu/ac),1))
mean.append(round((ind/ic),1))
mean.append(round((exp/ec),1))
mean.append(round((stu/sc),1))
mean.append(round((fac/fc),1))
print(mean)
mean.sort()
mean.reverse()
print(mean)
objects = ('alumni','experts','students','faculty','industry')
y_pos = np.arange(len(objects))
plt.bar(y_pos, mean, align='center', alpha=0.75)
plt.xticks(y_pos, objects)
plt.ylabel('rating')
plt.xlabel('participants')
plt.title('overall rating for 15mx11')
plt.show()
