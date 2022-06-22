# -*- coding: utf-8 -*-
#Mor Rozner 2022
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import random


objects = ['planet','WD','BH','NS','comet','RG','TZA','GCs','galaxy']
processes = ['GDF','DF','tides','kicks','RR']
environments = ['GCs','protoplanetary disk','atmospheres']
categories = [objects, processes,environments]
categories_names = ['objects', 'processes','environments']

final_idea = ''


for i in range(len(categories)):
    cat = categories[i]
    rand = random.randint(0, len(cat)-1)
    final_idea = final_idea+str(categories_names[i])+':'+str(cat[rand])+' '    

    
print(final_idea)
    
    




