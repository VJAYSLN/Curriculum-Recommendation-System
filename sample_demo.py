# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:35:35 2018

@author: J N BALAKUMARAN
"""

from recommendation_data import dataset
from math import sqrt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def pearson_correlation(person1,person2):

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
		# don't compare me to myself
		if other == person:
			continue
		sim = pearson_correlation(person,other)
		#print (">>>>>>>",sim)

		# ignore scores of zero or lower
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
	return recommendataions_list
		

#scores=most_similar_users('student',5)
#print(scores)
new=user_recommendations('student')
dataset["student"].update(new)
dataset['student']['ds']=round(dataset['student']['ds'],1)
#print(dataset)
new=user_recommendations('industry')
dataset["industry"].update(new)
dataset['industry']['stat']=round(dataset['industry']['stat'],1)
print(dataset) 
csa=ppl=mfcs=ds=stat=0
for key in dataset:
    ppl+=dataset[key]['ppl']
    csa+=dataset[key]['csa']
    stat+=dataset[key]['stat']
    mfcs+=dataset[key]['mfcs']
    ds+=dataset[key]['ds']
    
print("ppl:",ppl,"csa:",csa,"stat:",stat,"mfcs:",mfcs,"ds:",ds)
mean=[]
print("length of dataset",len(dataset))
mean.append(ppl/len(dataset))
mean.append(csa/len(dataset))
mean.append(stat/len(dataset))
mean.append(mfcs/len(dataset))
mean.append(ds/len(dataset))
print(mean)
mean.sort()
mean.reverse()
print(mean)
objects = ('ppl','stat','csa','ds','mfcs')
y_pos = np.arange(len(objects))
plt.bar(y_pos, mean, align='center', alpha=0.55)
plt.xticks(y_pos, objects)
plt.ylabel('rating')
plt.xlabel('courses')
plt.title('overall rating')

plt.show()