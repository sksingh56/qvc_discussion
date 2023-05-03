# QVC

<details>

  <summary> Requirement </summary>

# Requirement A: Managing Data Dictionary #

Lets assume that there is an arbitary dictionary d. 

e.g. 

data1 = {'key11': { 'key21': 'a','key22': 'b',}, 
        'key13': {'key31': 'd','key32':{'key21': 'e', 'key22': 'f',},},
        'key12': 'c',  
         }

## Q1- How can you update leaves (values) of a dictionary ?

 e.g. values 'a', 'b',....'f'.#     
 such that the maps 'a' -> 'aa', 'b'->'bb' and so on are applied! 

## Q2- Write up a function that does this algorithmically for an arbitrary dictionary ?

   2.1 your function can just update d 
   
   2.2 your function can return a dictionary without mutating d

Now, what if we had other data types 

d2 = { 'key11':{'key21': 'a', 'key22': 'b',},
       'key12': 'c',
       'key13': { 'key31': 'd', 'key32':{ 'key21': 'e','key22': 'f', },},    
       'key14': [1,2,3], 1 : (2,3), }

## Q3. Can you generalize your function to deal with the cases above in d2 ? 
   
   where list and strings are doubled or in general multiplied by n=2 
   
   e.g. 'a' ->'aa',# [1,2,3] -> [1,2,3,1,2,3]  
   
   and tuples are not modified.#---------------------# 
   
   3.1 your function can just update d2# 
   
   3.2 your function can return a dictionary without mutating d2#--------------------# 
   
   Hint: a neat style of coding with doc strings and type indication is appreciated.  
   Hint2: The dictionaries above are small but what if you have a large dictionary # with 10-times nested sub dictionaries.

# Requirement B

We are going to create some features for a # pandas dataframe based on a simillar approach. 

There are three coding assignments: Q1, Q2 & Q3 ## Product groups in QVC fashion assortments have SKN numbers to identify them. ## Here are some data on sales and inventory. 

Our task is to decide on which lifecycle the ## product will be in.
 """
 "skn": "302129",      --> product ID"
 dropship" : False,   --> if this product is from an external vendor
 "date": pd.Timestamp("2023-04-23"),   --> basically today
 "sales_per_day": 10,  --> estimated sales per day for next 30 days. 
 "price": 13,          --> unit price of the item in euro
 "current_stock" : 200, --> stock count as of today 
 "date_new_stock_arrival": pd.Timestamp("2023-06-03"), --> items new stock arrival date :)"new_stock": 300,  --> new stock size of the item 
 "reorder" : True, --> checks if the item is reorderable
 "days_stock_age" : 90, --> the age of the old stock"""
 
 import pandas as pd
 import numpy as np
 
 dropship = False## 
 WARNING : This is just a test dataset## 
 Your solution should work for any dataset with the same structure
 ```
 data = pd.DataFrame.from_records(    data =   [
        {#0
            "skn": "302129",
            "dropship" : False, 
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 10,
            "price": 13, 
            "current_stock" : 200, 
            "date_new_stock_arrival": pd.Timestamp("2023-06-03"),
            "new_stock": 300, 
            "reorder" : True,
            "days_stock_age" : 90, 
        },
        {#1
            "skn": "332121",
            "dropship" : True, 
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 5,
            "price": 150, 
            "current_stock" : 20, 
            "date_new_stock_arrival": pd.Timestamp("2023-05-10"),
            "new_stock": 10, 
            "reorder" : True,
             "days_stock_age" : 100, 
        },
        {#2
            "skn": "112124",
            "dropship" : False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 1000, 
            "current_stock" : 100, 
            "date_new_stock_arrival": pd.Timestamp("2023-05-15"),
            "new_stock": 10, 
            "reorder" : True, 
             "days_stock_age" : 20, 
        },
        {#3
            "skn": "192123",
            "dropship" : False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 29, 
            "current_stock" : 50, 
            "date_new_stock_arrival": pd.Timestamp("2023-05-15"),
            "new_stock": 100, 
            "reorder" : True, 
             "days_stock_age" : 120, 
        },
        {#4
            "skn": "762129",
            "dropship" : False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 77, 
            "current_stock" : 15, 
            "date_new_stock_arrival": pd.Timestamp("2023-05-05"),
            "new_stock": 10, 
            "reorder" : True, 
             "days_stock_age" : 10, 
        },
        {#5
            "skn": "762134",
            "dropship" : False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 99, 
            "current_stock" : 20, 
            "date_new_stock_arrival": pd.Timestamp("2023-06-03"),
            "new_stock": 10, 
            "reorder" : True, 
            "days_stock_age" : 30, 
        },
        {#6
            "skn": "762134",
            "dropship" : False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 299, 
            "current_stock" : 200, 
            "date_new_stock_arrival": np.nan,
            "new_stock": 0, 
            "reorder" : False, 
            "days_stock_age" : 200, 
        }
    ]

``` 


## Q1. Prepare the data via calculatin the following new columns 
    
      - stockout_days : stock will be consumed in how many days from today (date)
      - stock_arrival_days : new stock will arrive in how many days from today(date)

```
lifecycle_tree = {
    '(is item dropship ?)': 
        {
        'YES':  'Scenario: Price RRP', 
        'NO' : 
            {
                '( is stock age < 100 ?)':
                {
                    'YES':
                        { 
                            '(Can item stock be reordered ?)':
                                {

                                    'YES': 
                                        {
                                            '(is stock_arrival_days - stockout_days > 7 days)': 
                                                {
                                                    'YES' : 'Scenario: Inventory Turnover Margin-%20',
                                                    'NO'  : 'Scenario: Margin Optimisation with Market Constraints'
                                                }
                                        },

                                    'NO': 'Scenario: Margin Optimisation' 
                                }
                        },
                    'NO': 'Scenario: Markdown'
                }
            }
        }
}
```
## Q2.  Write up a function that takes in each row and returns two strings lifecycle scenario and path 
     # e.g. # return 'Scenario: Markdown' , 
     '(is item dropship ?)_NO_( is stock age < 100 ?)_NO'def lifecylcle( tree, path , data_row):        """ this will eventually return scenario, scenario_path """

## Q3 Apply the function to data, so that there are two new columns in data called  'scenario', 'scenario_path'# for every product SKN. 

</details>

<details>
  <summary> Steps To Install Git Repo and Docker Build </summary>

 #  Steps to install Git Repo and Docker Build on your Local Machine:
   1) Clone the repository in your project directory
        
        ```
        prompt>  git clone git@github.com:sksingh56/qvc.git
        ```
   2) Run Docker compose build
       
       ```
        prompt> docker-compose build
       ```

   3) Set Docker Compose to run test 
      
       ```
        prompt> docker-compose run test sh
        ```

   4) Run All the test
       
       ```
        pytest
       ```

   5) Run specific test for dictionary
   
       ```
        pytest -k dict
       ```
   6) Run specific test for pandas   
       ```
        pytest -k pandas
       ```  
</details>

<details>

  <summary> Cloud Architecture Discussion  </summary>
  
  [Mindmap](https://lucid.app/documents/view/52808558-9553-4714-b199-adec1f897864) / [Mindmap Github URL](architecture/mindmap.png)

  [Proposed Architect Solution](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=qvc_proposed_solution.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XZW8OP-nE_HWGQGmZ5kshrCBEO5WQhWk%26export%3Ddownload)
  
  
  ##Option 1: Oracle migration using the Lift and Shift approach. 
  
  We need to migrate two years' worth of data, with a daily volume of 10GB, which could result in migrating 7-8TB of data. The cost and time required to migrate data over VPN or dedicated network connections is likely to be significant. Additionally, continuous migration of data in small chunks could impact the schedules of the EDM (Enterprise Data Management) processes. Therefore, the Lift and Shift approach would be a good choice

  [Oracle database migration: Lift and shift](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/oracle-migrate/oracle-migration-lift-shift)

 [Design And Performance For Oracle Migrations](https://learn.microsoft.com/en-us/azure/synapse-analytics/migration-guides/oracle/1-design-performance-migration)  
  
</details>

<details>
<summary> QVC SQL Query Solution </summary>

[Entity Relationship Diagram](sql/qvc_entity_relation_ship.drawio.png)

[SQL query implementation](sql/SQL.md)

</details>

<details>

  <summary> Python Requirment(Pandas) A Solution </summary>

  [Code To Handle Dict Data Frame For Requirment A](scripts/dict_handling.py)
  
  [Script Having Common Module](tests/conftest.py)

  [Pytest Script For Unit Testing of Dictionary For Requirement A](tests/test_dict.py) 

</details>



<details>
  <summary> Python requirment(Pandas) B solution </summary>

  [code to handle pandas data frame for Requirment B](scripts/pandas_df.py) 

  [script having common module](tests/conftest.py)

  [pytest script for unit test script pandas dataframe for requirement B](tests/test_pandas_df.py)

</details>
