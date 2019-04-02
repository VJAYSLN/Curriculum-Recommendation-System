# -*- coding: utf-8 -*-

from math import sqrt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from sample_dt import Dataset_A
from datasett import dataset
print(Dataset_A)
Dataset=Dataset_A

"""def worth():
    Dataset=Dataset_A
    wor=nwor=0
    i=0
    while i<len(Dataset):
        if(Dataset[i][0]==1):
            wor+=1
        else:
            nwor+=1
        i+=1
    print("Worth course \nout of ",len(Dataset))
    print("Worth",wor,"\nNot worth",nwor)
    
worth()"""

def coll_filter():
    def pearson_correlation(person1,person2):
        both_rated = {}
        for item in dataset[person1]:
            if item in dataset[person2]:
                both_rated[item] = 1
                
        number_of_ratings = len(both_rated)	
        
        if number_of_ratings == 0:
            return 0
        # Add up all the preferences of each user
        person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
        person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])
        
        person1_square_preferences_sum = sum([pow(dataset[person1][item],2) for item in both_rated])
        person2_square_preferences_sum = sum([pow(dataset[person2][item],2) for item in both_rated])

        product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])
        
        numerator_value = product_sum_of_both_users - (person1_preferences_sum*person2_preferences_sum/number_of_ratings)
        denominator_value = sqrt((person1_square_preferences_sum - pow(person1_preferences_sum,2)/number_of_ratings) * (person2_square_preferences_sum -pow(person2_preferences_sum,2)/number_of_ratings))
        if denominator_value == 0:
            return 0
        else:
            r = numerator_value/denominator_value
            return r
    def most_similar_users(person,number_of_users):
        scores = [(pearson_correlation(person,other_person),other_person) for other_person in dataset if  other_person != person ]
        scores.sort()
        scores.reverse()
        return scores[0:number_of_users]
    def user_recommendations(person):
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
                if item not in dataset[person] or dataset[person][item] == 0:
                    totals.setdefault(item,0)
                    totals[item] += dataset[other][item]* sim
                    simSums.setdefault(item,0)
                    simSums[item]+= sim
        rankings = [(total/simSums[item],item) for item,total in totals.items()]
        rankings.sort() 
        rankings.reverse()
        recommendataions_list = [(recommend_item,score) for score,recommend_item in rankings]
        return recommendataions_list
    new=user_recommendations('Alumni5')
    dataset['Alumni5'].update(new)
    dataset['Alumni5']['ds']=round(dataset['Alumni5']['ds'],1)
    dataset['Alumni5']['python']=round(dataset['Alumni5']['python'],1)
    new=user_recommendations('Alumni4')
    dataset["Alumni4"].update(new)
    dataset['Alumni4']['stat']=round(dataset['Alumni4']['stat'],1)
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
    print("length of dataset",len(Dataset))
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
        
coll_filter()
"""def lab():
    i=0
    laby=labn=0
    while i<len(Dataset):
        if(Dataset[i][3]==1):
            laby+=1
        else:
            labn+=1
        i+=1
    print("\n\nLab for this course\nOut of ",len(Dataset))
    print("lab needed",laby,"\nNot needed",labn)
lab()
def content():
    i=0
    cy=cn=0
    while i<len(Dataset):
        if(Dataset[i][2]==1):
            cy+=1
        else:
            cn+=1
        i+=1
    print("\n\nContent of this course\nout of",len(Dataset))
    print("Content ok:",cy,"\nNot ok:",cn)
content()

def precourse():
    course_list=[]
    py=pn=0
    i=0
    while i<len(Dataset):
        s=str(Dataset[i][3])
        s=s.lower()
        if(s=='no' or s=='-'):
            pn+=1
        else:
            py+=1
            if(s not in course_list):
                course_list.append(Dataset[i][3])
        i+=1
    print("Precourses list\n")
    print(course_list,"\n precourse :",py,"\n No precourses required",pn)
    def lab():
        i=0
        laby=labn=0
        while i<len(Dataset):
            if(Dataset[i][6]==1):
                laby+=1
            else:
                labn+=1
            i+=1
        print("\n\nLab for this course\nOut of ",len(Dataset))
        print("lab needed",laby,"\nNot needed",labn)
    lab()
precourse()

def suggest():
    course_list=[]
    py=pn=0
    i=0
    while i<len(Dataset):
        s=str(Dataset[i][7])
        s=s.lower()
        if(s=='no' or s=='-'):
            pn+=1
        else:
            py+=1
            if(s not in course_list):
                course_list.append(Dataset[i][3])
        i+=1
    print("\n\nOther course Suggestion\n")
    print(course_list,"\nSuggested:",py,"\nNot suggested:",pn)
    def lab():
        i=0
        laby=labn=0
        while i<len(Dataset):
            if(Dataset[i][9]==1):
                laby+=1
            else:
                labn+=1
            i+=1
        print("\n\nLab for this course\nOut of ",len(Dataset))
        print("lab needed",laby,"\nNot needed",labn)
    lab()
    def prereq():
        course_list=[]
        py=pn=0
        i=0
        while i<len(Dataset):
            s=str(Dataset[i][10])
            s=s.lower()
            if(s=='no' or s=='-'):
                pn+=1
            else:
                py+=1
                if(s not in course_list):
                    course_list.append(Dataset[i][3])
            i+=1
        print("Precourses list\n")
        print(course_list,"\n precourse :",py,"\n No precourses required",pn)
    prereq()
suggest()"""
    
    
        
    
    