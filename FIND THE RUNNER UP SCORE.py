#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#runner_up_score



# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given  n scores. Store them in a list and find the score of the runner-up.



# Print the runner-up score.


n = int(input())
arr = map(int, input().split())
list_of_scores=list(arr)
max_score=max(list_of_scores)
list_without_max_score=[]
for i in list_of_scores:
    if i!=max_score:
        list_without_max_score.append(i)
runner_up_score=max(list_without_max_score)
 
print(list_of_scores)
print(list_without_max_score)
print(runner_up_score)

