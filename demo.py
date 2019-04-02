# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 23:46:39 2018

@author: J N BALAKUMARAN
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:11:06 2018

@author: J N BALAKUMARAN
"""

dataset={
        "Alumni1":
            {
                'mfcs':3,
                'ppl':3,
                'stat':4,
                'csa':3,
                'ds':3,
                'python':4.5
            },
        "Alumni2":
            {
                'mfcs':3,
                'ds':3,
                'ppl':4,
                'stat':4,
                'csa':3,
                'python':3.5
            },
        "Alumni3":
            {
                'mfcs':4,
                'ds':3,
                'ppl':2,
                'stat':3,
                'csa':3,
                'python':4.5
            },
        "Alumni4":
            {
                'mfcs':3.5,
                'ds':3.5,
                'ppl':2,
                'csa':3,
                'python':4.5
                         
            },
        "Alumni5":
            {
                'mfcs':2.5,
                'stat':3,
                'ppl':2,
                'csa':3
            }
                
        }
            


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:35:35 2018

@author: J N BALAKUMARAN
"""

#from recommendation_data import dataset
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
print("Before :",dataset)
new=user_recommendations('Alumni5')
dataset['Alumni5'].update(new)
dataset['Alumni5']['ds']=round(dataset['Alumni5']['ds'],1)
dataset['Alumni5']['python']=round(dataset['Alumni5']['python'],1)
#print(dataset)
new=user_recommendations('Alumni4')
dataset["Alumni4"].update(new)
dataset['Alumni4']['stat']=round(dataset['Alumni4']['stat'],1)
print("After updated:",dataset) 
csa=ppl=mfcs=ds=stat=python=0
for key in dataset:
    ppl+=dataset[key]['ppl']
    csa+=dataset[key]['csa']
    stat+=dataset[key]['stat']
    mfcs+=dataset[key]['mfcs']
    ds+=dataset[key]['ds']
    python+=dataset[key]['python']
    
print("ppl:",ppl,"csa:",csa,"stat:",stat,"mfcs:",mfcs,"ds:",ds,"python:",python)
mean=[]
print("length of dataset",len(dataset))
mean.append(ppl/len(dataset))
mean.append(csa/len(dataset))
mean.append(round(stat/len(dataset),1))
mean.append(mfcs/len(dataset))
mean.append(round(ds/len(dataset),1))
mean.append(round(python/len(dataset)))
print(mean)
mean.sort()
mean.reverse()
print(mean)
objects = ('python','stat','mfcs','ds','csa','ppl')
y_pos = np.arange(len(objects))
plt.bar(y_pos, mean, align='center', alpha=0.75)
plt.xticks(y_pos, objects)
plt.ylabel('rating')
plt.xlabel('courses')
plt.title('overall rating for sem1')

plt.show()



# -*- coding: utf-8 -*-


dataset={
        "Inustry1":
            {
                'oops':3,
                'microprocessor':3,
                'ads':4,
                'dbms':3,
                'ot':3,
                'computerfundamental':4.5
            },
        "Industry2":
            {
                'oops':3,
                'ads':3,
                'microprocessor':3,
                'dbms':4,
                'ot':3,
                'computerfundamental':3.5
            },
        "Industry3":
            {
                'oops':4,
                'ads':3,
                'microprocessor':2,
                'ot':3,
                'dbms':3,
                'computerfundamental':4.5
            },
        "Industry4":
            {
                'oops':3.5,
                'ads':3.5,
                'microprocessor':2,
                'ot':3,
                'computerfundamental':4.5
                         
            },
        "Industry5":
            {
                'oops':2.5,
                'ot':3,
                'microprocessor':2,
                'dbms':3
            }
                
        }

for i in dataset:
   print(dataset[i].items(),"\n")
            


# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 19:35:35 2018

@author: J N BALAKUMARAN
"""

#from recommendation_data import dataset
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
		

new=user_recommendations('Industry5')
dataset['Industry5'].update(new)
dataset['Industry5']['ads']=round(dataset['Industry5']['ads'],1)
dataset['Industry5']['computerfundamental']=round(dataset['Industry5']['computerfundamental'],1)
#print(dataset)

#print(dataset)
new=user_recommendations('Industry4')
dataset["Industry4"].update(new)
dataset['Industry4']['stat']=round(dataset['Industry4']['dbms'],1)
print(dataset) 
ot=microprocessor=oops=ads=dbms=computerfundamental=0
for key in dataset:
    ot+=dataset[key]['ot']
    microprocessor+=dataset[key]['microprocessor']
    dbms+=dataset[key]['dbms']
    ads+=dataset[key]['ads']
    computerfundamental+=dataset[key]['computerfundamental']
    oops+=dataset[key]['oops']
    
print("ot:",ot,"oops:",oops,"dbms:",dbms,"microprocessor:",microprocessor,"ads:",ads,"computerfundamental:",computerfundamental)
mean=[]
print("length of dataset",len(dataset))
mean.append(ot/len(dataset))
mean.append(oops/len(dataset))
mean.append(round(dbms/len(dataset),1))
mean.append(microprocessor/len(dataset))
mean.append(round(ads/len(dataset),1))
mean.append(round(computerfundamental/len(dataset)))
print(mean)
mean.sort()
mean.reverse()
print(mean)
objects = ('comp.fundmtls','ads','dbms','oops','ot','mprocessor')
y_pos = np.arange(len(objects))
plt.bar(y_pos, mean, align='center', alpha=0.75)
plt.xticks(y_pos, objects)
plt.ylabel('rating')
plt.xlabel('courses')
plt.title('overall rating for sem2')

plt.show()
