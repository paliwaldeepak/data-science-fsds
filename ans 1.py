#!/usr/bin/env python
# coding: utf-8

# In[3]:


def find_highest_frequency_word_length(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(c for c in s if c.isalnum() or c.isspace()).lower()
    
    # Split the string into words
    words = s.split()
    
    # Count the frequency of each word
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    # Find the highest frequency
    max_freq = 0
    for word in freq:
        if freq[word] > max_freq:
            max_freq = freq[word]
    
    # Find the length of the highest-frequency word
    max_freq_word_length = 0
    for word in freq:
        if freq[word] == max_freq and len(word) > max_freq_word_length:
            max_freq_word_length = len(word)
    
    return max_freq_word_length


# In[8]:


s = "write write write all the number from from from 1 to 100"
print(find_highest_frequency_word_length(s))


# In[9]:


s = "my name name name is deepak deepak"
print(find_highest_frequency_word_length(s))

