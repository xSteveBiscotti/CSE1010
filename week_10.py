#!/usr/bin/env python
# coding: utf-8

# ## Computing the mean and media

# In[ ]:


nums = [2, 3, 4, -1, 6,9]
def get_mean(num_list):
    sum_t = 0
    for number in num_list:
        sum_t+=number
    return sum_t/len(num_list)

print(get_mean(nums))


# In[ ]:


def get_mean2(num_list):
    return sum(num_list)/len(num_list)

print(get_mean(nums))


# In[ ]:


def get_median(num_list):
    sorted_list = sorted(num_list)
    if len(sorted_list)%2==0:
        # even number of items
        return (sorted_list[len(sorted_list)//2-1]+sorted_list[len(sorted_list)//2])/2
    else:
        # odd number of items
        return sorted_list[(len(sorted_list)-1)//2]
    


# In[ ]:


print(get_median(nums))


# In[ ]:




