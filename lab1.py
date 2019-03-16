
# coding: utf-8

# In[2]:


import re
import pandas as pd
import time


# In[3]:


# шифровка текста
def code(text):
    code_text = ''

    for i, j in enumerate(text):
        if j in dict_alphabet:
            code_text += dict_alphabet[j]
        else:
            code_text += ' '

    return code_text


# In[4]:


key_word = list('мир') 


# In[5]:


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'  # обычный алфавит


# In[6]:


code_alphabet = key_word + [i for i in alphabet if i not in key_word]  # шифрованный алфавит


# In[8]:


dict_alphabet = dict(zip(list(alphabet), code_alphabet))  # словарь алфавит : шифрованный алфавит


# In[10]:


text = ''


# In[11]:


with open('war_peace_clean.txt', 'r', encoding='utf-8') as f:
    text = f.read() # обычный текст


# In[12]:


code_text = code(text) # зашифрованный текст


# In[13]:


print(code_text)


# In[14]:


# частота букв
letters = pd.DataFrame([ [i, text.count(i), code_text.count(i), 
                          dict_alphabet[i], code_text.count(dict_alphabet[i])]  for i in alphabet], 
                       columns = ['letter', 'text', 'code_text', ' code_letter', 'code_text'])


# In[15]:


print('\n\nЧАСТОТА БУКВ\n\n')
print(letters)


# In[16]:


# биграммы
bigrams = pd.DataFrame( [[i+j, text.count(i+j), code_text.count(i+j)]  
                         for j in alphabet for i in alphabet], columns = ['bigram', 'text', 'code_text'])


# In[17]:


print('\n\n ТОП 5 БИГРАМ В ТЕКСТЕ\n\n')
print(bigrams.sort_values('text', ascending=False).head().to_string(index=False))


# In[18]:


print('\n\n ТОП 5 БИГРАМ В ЗАШИФРОВАННОМ ТЕКСТЕ\n\n')
print(bigrams.sort_values('code_text', ascending=False).head().to_string(index=False))

