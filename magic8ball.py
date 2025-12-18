#!/usr/bin/env python
# coding: utf-8

# In[3]:


Q = input('Please enter your question: ')

valid_starts = ('is', 'Is', 'Are', 'are', 'can', 'Can', "can't", "Can't", 'Should', 'should', 'Will', 'will', 'does', 'Does', 'was', 'Was', 'were', 'Were', 'am', 'Am', 'Could', 'could', 'Shall', 'shall', 'Would', 'would', 'May', 'may', 'might', 'Might', 'do', 'Do', 'Did', 'did')

while not Q.startswith(valid_starts):
    print('\nPlease enter a valid yes/no question.')
    Q = input('\nTry again:')

import random
answer = random.randint(1, 9)
if answer == 1:
    print('\nMagic 8 Ball: Yes, definitely!')
elif answer == 2:
    print('\nMagic 8 Ball: It is decidedly so.')
elif answer == 3:
    print('\nMagic 8 Ball: Without a doubt.')
elif answer == 4:
    print('\nMagic 8 Ball: Reply hazy, try again.')
elif answer == 5:
    print('\nMagic 8 Ball: Ask again later.')
elif answer == 6:
    print('\nMagic 8 Ball: Better not tell you now.')
elif answer == 7:
    print('\nMagic 8 Ball: My sources say no.')
elif answer == 8:
    print('\nMagic 8 Ball: Outlook not so good.')
else: 
    print('\nMagic 8 Ball: Very doubtful.')


# In[ ]:




