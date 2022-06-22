#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 14:14:29 2022

@author: morozner
"""

objects = ['planet','WD','BH','NS','comet','RG','TZA','GCs','galaxy']
processes = ['GDF','DF','tides','kicks','RR']
environments = ['GCs','protoplanetary disk','atmospheres','AGN','GMC','field','DM halo']
categories = [objects, processes,environments]
categories_names = ['objects', 'processes','environments']



from tkinter import *
import random 

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, categories_names)
   lng.pack(side=TOP,  fill=X)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()))
   Button(root, text='Go!', command=root.quit).pack(side=RIGHT)
   root.mainloop()
   
   choices = list(lng.state())
   final_idea = ''
   
   for i in range(len(categories)):
       
       if choices[i] == 1:
           cat=categories[i]
           rand = random.randint(0, len(cat)-1)
           final_idea = final_idea+str(categories_names[i])+':'+str(cat[rand])+' '
           
   print(final_idea)
           
