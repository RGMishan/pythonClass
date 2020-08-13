#!/usr/bin/env python
# coding: utf-8

# ### P7-Generate two or more random paragraphs using the given online website.
# ### & perform the following tasks on it.
# https://randomwordgenerator.com/paragraph.php

# In[1]:


print("Lab 7 Python")
print("Mishan Regmi 5BCA A '1841030'")


# In[2]:


import re


# In[3]:


para = open("paragraphRegex.txt","r+") 
reading = para.read()
print(reading)


# ### 01. Find the total number of paragraphs and total number of lines and words in each paragraph.

# In[4]:


paragraph = re.split(r'[\n]', reading)
lines = re.split(r'[.?]', reading)
words = re.split(r'[ \n,?.!]', reading)
print("The number of paragraph are", len(paragraph))
print("The number of lines are", len(lines))
print("The number of words are", len(words))


# ### 02. Find all the words that begin with vowel in the first paragraph & those which begin with
# ### consonants in the second paragraph.

# In[5]:


print("VOWEL")
print("-----------------------------------------")
para1 = re.split(r'[ \n]', paragraph[0])
countvow = 0
for word in para1:
    if re.search(r'^[aeiouAEIOU]', word):
        countvow += 1
        print(word)
print("-----------------------------------------")
print("CONSONANTS")
print("-----------------------------------------")
countconst = 0
para2 = re.split(r'[ \n]', paragraph[2])
for word in para2:
    if re.search(r'^[^aeiouAEIOU]', word):
        countconst += 1
        print(word)


# ### 03. Find all the words having numerals.

# In[6]:


countnum = 0
for w in range(len(words)):
    if re.search(r'[0-9]', words[w]):
        countnum += 1
        print(words[w])
print("\nWords having numerals are", countnum)


# ### 04. Find all the words which begin with letter 'data/Data/DATA'. If know such words exist then
# ### add such related words and repeat the search.

# In[7]:


countd = 0
words.append("This is my data ")
words.append("I am mining data ")
for i in range(len(words)):
    if re.search("data|Data|DATA", words[i]):
        countd += 1
        print(words[i])
print("\nWords which begin with letter 'data/Data/DATA' are", countd)


# ### 05. Find all the words which end with letter 'e'.

# In[8]:


countE = 0
for i in range(len(words)):
    if re.search(r'e$', words[i]):
        countE += 1
        print(words[i])
print("\nWords which end with letter 'e' are", countE )


# ### 06. Find all the words that begins with an vowel and ends with an vowel OR that begins with a
# ### consonant and ends with a consonant.

# In[9]:


countVowCon = 0
for w in range(len(words)):
    if re.search(r'^[aeiouAEIOU]', words[w]) and re.search(r'[aeiouAEIOU]$', words[w]) or re.search(r'^[^aeiouAEIOU]', words[w]) and re.search(r'[^aeiouAEIOU]$', words[w]):
        countVowCon += 1
        print(words[w])
print("\nWords that begins with an vowel and ends with an vowel OR that begins with a consonant and ends with a consonant are ",countVowCon)


# ### 07. Find all the words that have the letters 'to' in them, find the position of 'to' in each word.

# In[10]:


countTo = 0
for to in words:
    if re.search("to", to):
        countTo += 1
        print("The word : {} is in position : {}".format(to, to.index("to")))


# 
# ### 08. Find all the words that have capital letters in them.

# In[11]:


countCap = 0
for cap in words:
    if re.search("[A-Z]", cap):
        print(cap)
        countCap += 1
print("\nWords that have capital letters in them count is", countCap)


# ### 09. Find all the words that have special symbols in them.

# In[12]:


countSymbol = 0
for symbol in words:
    if re.search("[!@#$%^&*]", symbol):
        print(word)
        countSymbol += 1
print("\nWords that have special symbols in them count is",countSymbol)


# ### 10. Find the first occurence of fullstop in your input.

# In[13]:


print("The first occurance of full stop is after >>>",reading[0:reading.find('.')], "<<<this sentence.")


# ### 11. Find the words that dont have any vowel in them. If no such words exist add a few related
# ### words and repeat the task.

# In[14]:


countNoVowel = 0
for word in words:
    if not re.search(r'[aeiouAEIOU0-9]', word):
        print(word)
        countNoVowel += 1
print("\nWords that dont have any vowel in them count is", countNoVowel)


# ### 12. Find the first occurent of a word that does not begin with consonant but ends with 'ing' and has
# ### 'ta' in it.

# In[15]:


counting = 0
for word in words:
    if re.search("[aeiouAEIOU]", word) and re.search("ing$", word) and re.search("ta", word):
        print(word)
        counting += 1
print("\nWord that does not begin with consonant but ends with 'ing' and has 'ta' in it count is", counting)

