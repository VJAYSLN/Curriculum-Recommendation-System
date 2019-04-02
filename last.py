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
def Fun1(a):  
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
  plt.title('overall rating for'+a)
  plt.show()
            
Fun1("15MX11")
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
dataset=Dataset_for_15mx12     
print(dataset)
Fun1("15MX12")
