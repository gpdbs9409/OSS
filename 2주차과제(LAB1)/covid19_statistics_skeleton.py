#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Skeleton code
def normalize_data(n_cases, n_people, scale):
    # TODO) Calculate the number of cases per its population
    norm_cases = []
    for idx, n in enumerate(n_cases):
        norm_cases.append(n / (n_people[idx] / scale))
    return norm_cases

# Given data
regions = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam',
           'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227, 13530519, 3359527, 3322373, 2938429, 2630254, 2393626, 2118183, 1838353,
            1792476, 1597179, 1536270, 1454679, 1441970, 1124459, 675883, 365309]
n_covid = [644, 529, 38, 29, 148, 28, 41, 62, 23, 27, 27, 33, 16, 40, 20, 5, 4]

# Calculate total population and total new cases
sum_people = sum(n_people)
sum_covid = sum(n_covid)

# Normalize COVID-19 data per 1 million people
norm_covid = normalize_data(n_covid, n_people, 1000000)  # The new cases per 1 million people

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print()
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = (n_covid[idx] / sum_covid) * 100  # Calculate the ratio of new cases to the total
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))
print('')


# In[13]:


# Print COVID-19 new cases by region
print('Korean COVID-19 New Cases by Region')
print('| Region | New Cases | Ratio (%) | New Cases per 1M People |')
print('| ------ | --------- | --------- | ------------------------ |')
for idx, cases_per_million in enumerate(norm_covid):
    ratio = (n_covid[idx] / sum_covid) * 100 
    print('| %s | %d | %.1f | %.1f |' % (regions[idx], n_covid[idx], ratio, cases_per_million))



# In[ ]:




