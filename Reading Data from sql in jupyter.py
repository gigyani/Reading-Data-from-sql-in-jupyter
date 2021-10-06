#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3 as sq3
import pandas.io.sql as pds
import pandas as pd


# # Database connections

# In[2]:


path = 'classic_rock.db'     # Initialize path to SQLite database
con = sq3.Connection(path)   # We now have a live connection to our SQL database


# # Reading data

# In[8]:


# Write the query
query = '''
SELECT * 
FROM rock_songs;
'''

# Execute the query
observations = pds.read_sql(query, con)


# In[6]:


observations.head()


# # SQL Supported query

# In[11]:


# We can also run any supported SQL query
# Write the query
query = '''
SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays  
    FROM rock_songs
    GROUP BY Artist, Release_Year
    ORDER BY num_songs desc;
'''

# Execute the query
observations = pds.read_sql(query, con)

observations.head()


# # Common parameters

# There are a number of common paramters that can be used to read in SQL data with formatting:
# 
#   1. coerce_float: Attempt to force numbers into floats
#   2. parse_dates: List of columns to parse as dates
#   3.chunksize: Number of rows to include in each chunk
#     
# Let's have a look at using some of these parameters

# In[12]:


query='''
SELECT Artist, Release_Year, COUNT(*) AS num_songs, AVG(PlayCount) AS avg_plays  
    FROM rock_songs
    GROUP BY Artist, Release_Year
    ORDER BY num_songs desc;
'''

# Execute the query
observations_generator = pds.read_sql(query,
                            con,
                            coerce_float=True,            # Doesn't efefct this dataset, because floats were correctly parsed
                            parse_dates=['Release_Year'], # Parse Release_Year as a date
                            chunksize=5                   # Allows for streaming results as a series of shorter tables
                           )

for index, observations in enumerate(observations_generator):
    if index < 5:
        print(f'Observations index: {index}'.format(index))
        display(observations)

