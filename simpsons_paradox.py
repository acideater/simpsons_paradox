#!/usr/bin/env python
# coding: utf-8

# # Simpson's Paradox
# Use `admission_data.csv` for this exercise.

# In[2]:



import pandas as pd
import numpy as np

# Load and view first few lines of dataset

df = pd.read_csv('admission_data.csv')
df.head()


# ### Proportion and admission rate for each gender

# In[3]:



gender = df.groupby(['gender']).agg({'student_id':'count'})
print(gender)


# In[4]:


# Proportion of students that are female
# Proportion of students that are male

total = len(df['student_id'])
prop = gender/total 
print(prop)


# In[26]:


# Admission rate for females

f_admitted = df[df.gender=='female'].admitted.value_counts()[True]
f_applied = df[df.gender=='female'].admitted.value_counts().sum()
admission_female = f_admitted/f_applied
print(admission_female)


# In[27]:


# Admission rate for males

m_admitted = df[df.gender=='male'].admitted.value_counts()[True]
m_applied = df[df.gender=='male'].admitted.value_counts().sum()
admission_male = m_admitted/m_applied

print(admission_male)


# ### Proportion and admission rate for physics majors of each gender

# In[29]:


# What proportion of female students are majoring in physics?

f_physics = df[df.gender=='female'].major.value_counts()['Physics']
f_physics_total = df[df.gender=='female'].major.value_counts().sum()
f_physics_prop = f_physics/f_physics_total

print(f_physics_prop)


# In[8]:


# What proportion of male students are majoring in physics?
m_physics = df[df.gender=='male'].major.value_counts()['Physics']
m_physics_total = df[df.gender=='male'].major.value_counts().sum()
m_physics_prop = m_physics/m_physics_total
print(m_physics_prop)


# In[21]:


# Admission rate for female physics majors

mask = (df.gender == 'female')&(df.major == 'Physics')

f_admitted = df[mask].admitted.value_counts()[True]
f_applied = df[mask].admitted.value_counts().sum()
admission_f_phy = f_admitted/f_applied
print(admission_f_phy)


# In[19]:


# Admission rate for male physics majors

mask = (df.gender == 'male')&(df.major == 'Physics')

m_admitted = df[mask].admitted.value_counts()[True]
m_applied = df[mask].admitted.value_counts().sum()
admission_m_phy = m_admitted/m_applied
print(admission_m_phy)


# ### Proportion and admission rate for chemistry majors of each gender

# In[50]:


# What proportion of female students are majoring in chemistry?
f_chem = df[df.gender=='female'].major.value_counts()['Chemistry']
f_chem_total = df[df.gender=='female'].major.value_counts().sum()
f_chem_prop = f_chem/f_chem_total
print(f_chem_prop)


# In[51]:


# What proportion of male students are majoring in chemistry?
m_chem = df[df.gender=='male'].major.value_counts()['Chemistry']
m_chem_total = df[df.gender=='male'].major.value_counts().sum()
m_chem_prop = m_chem/m_chem_total
print(m_chem_prop)


# In[22]:


# Admission rate for female chemistry majors
mask = (df.gender == 'female')&(df.major == 'Chemistry')

f_admitted = df[mask].admitted.value_counts()[True]
f_applied = df[mask].admitted.value_counts().sum()
admission_f_chem = f_admitted/f_applied
print(admission_f_chem)


# In[23]:


# Admission rate for male chemistry majors
mask = (df.gender == 'male')&(df.major == 'Chemistry')

m_admitted = df[mask].admitted.value_counts()[True]
m_applied = df[mask].admitted.value_counts().sum()
admission_m_chem = m_admitted/m_applied
print(admission_m_chem)


# ### Admission rate for each major

# In[24]:


# Admission rate for physics majors
phy_admitted = df[df.major=='Physics'].admitted.value_counts()[True]
phy_applied = df[df.major=='Physics'].admitted.value_counts().sum()
admission_phy = phy_admitted/phy_applied

print(admission_phy)


# In[25]:


# Admission rate for chemistry majors
chem_admitted = df[df.major=='Chemistry'].admitted.value_counts()[True]
chem_applied = df[df.major=='Chemistry'].admitted.value_counts().sum()
admission_chem = chem_admitted/chem_applied

print(admission_chem)


# In[ ]:




