#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_valid_string(s):
    # Count the frequency of each character
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Check if all frequencies are the same
    values = list(freq.values())
    if len(set(values)) == 1:
        return "YES"  # All characters have the same frequency
    
    # Check if removing one character makes all frequencies the same
    for char in freq:
        freq[char] -= 1
        updated_values = list(freq.values())
        if len(set(updated_values)) == 1:
            return "YES"  # Removing one character makes all frequencies the same
        freq[char] += 1  # Reset the frequency for the next iteration

    return "NO"  # No valid condition satisfied


# In[3]:


print(is_valid_string("abc"))          
print(is_valid_string("aabbc"))        
print(is_valid_string("aabbcc"))       
print(is_valid_string("aabbbccccdd"))


# In[ ]:




