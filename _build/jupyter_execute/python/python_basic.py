#!/usr/bin/env python
# coding: utf-8

# # Python

# ### print session info
# 
# ```python
# !pip install session_info
# 
# import session_info
# 
# session_info.show()
# ```

# ## Algorithms & Data Structures

# ### Complexity

# ```python
# import numpy as np
# 
# np.random.shuffle(x)
# 
# %timeit -r1 -n1 code
# 
# big_number = 10_000_000
# ```

# Built-in Python `sort()` uses ...
# 
# batch multiplication (loop vs. vectorized)

# ## General

# ### Basic Functions

# ```python
# # print all list methods
# dir(list)
# 
# range()
# zip()
# enumerate()
# isinstance(object, type)
# 
# # when comparing float, to avoid rounding errors
# math.isclose()
# np.isclose() 
# 
# # execute shell commands by appending !
# !flake8 file.py
# 
# copy()
# deepcopy()
# ```

# ### NumPy

# | Function | Description |
# |----------|-------------|
# np.arange()| sequence ranging from a to b 
# np.linspace() | linearly spaced sequence
# np.ones 
# np.zeros
# np.full | fill dimension with values
# np.random.rand() | fill with random values
# np.transpose()
# np.T
# np.mean()
# np.astype(int)
# np.shape
# np.reshape()
# np.newaxis
# np.ravel()
# np.flatten()

# ### `if` statement

# ```python
# # default
# if condition1:
#     ...
# elif condition2:
#     ...
# else:
#     ...
#     
# # inline
# ... if ... else ...
# ```

# ### Loops

# ```python
# # for loop
# for i in sequence: 
#     ...
#     
# # while loop
# while condition:
#     ...
# ```

# ### Exceptions

# ```python 
# 
# # define custom errors
# class CustomError(Exception):
#     pass
# # use custom error 
# if some_condition:
#     raise CustomError
#     
#     
# try:
#     # test to see if it throws errors
# except Exception as ex: 
#     # catch specific exception
# except:
#     # catch general exceptions
# else:
#     # do if no errors are caught
# finally:
#     # do something after everything ends,
#     # regardless of errror or non-error
# 
# ```

# ### Defining custom functions

# ```python
# # default
# def function(arg1, arg2, ...):
#     # content
#     return output
# 
# # anonymous function
# lambda x: x+1
# ```

# We can supply `*args` for arbitrary number of positional arguments, `**kwargs` for keyword arguments.

# ### Defining custom classes

# ```python
# class CustomClass(Inheritance):
#     
#     # class attributes
#     name = ""
#     age = 20
#     
#     # initializer 
#     def __init__(self, arg1, arg2):
#         super().__init__ # inherit
#         self.name = arg1
#         self.age = arg2
#     
#     # instance method
#     def function(self):
#         ...
#     
#     @classmethod
#     def function(cls, *arg):
#         retrun cls(...)
# 
#     @staticmethod
#     def function():
#         # helper functions that are better when shipped together
#         # for clarity
#     
#     @property
#     def prop(self):
#         return ...
#         # save return of function as an attribute
#         # e.g. np.shape()
#         
#     @<attribute>.setter
#     def prop(self, *args):
#         # set new values for property
#         
#     @<attribute>.deleter
#     def prop(self):
#         # set to None to delete
#         
#         
# ```

# ### Testing

# ```python
# assert expression, "Error message"
# ```

# ## Data Wrangling

# ```python 
# pd.read_csv(path)
# pd.read_csv(url)
# 
# df.head()
# df.info()
# df.describe(include='all')
# df.dtypes
# 
# # renaming columns
# df.rename(columns= {"old_col1" : "new_col1",
#                     "old_col2" : "new_col2"})
# df.columns = list_of_column_names
# 
# # set column as index
# df = df.set_index(col)
# 
# df = df.reset_index()
# 
# df.sort_values(by='col', ascending=True)
# df.sample()
# df.min(numeric_only=True)
# df.idxmin()
# 
# 
# df.drop(columns=list_of_col)
# ```

# ```python
# # pivot longer
# df.melt(id_vars= , 
#         value_vars= , 
#         var_name=, 
#         ignore_index=False)
# 
# # pivot wider
# df.pivot(index= ,
#          columns= ,
#          values= )
# 
# # append data frame vertically
# pd.concat((df1, df2), axis=0)
# 
# #append data frame horizontally
# pd.concat((df1, df2), axis=1, ignore_index=True)
# 
# ```

# | Method | Syntax |
# |--------|--------|
# | Select column | `df[col_label]` | 
# | Select row slice | `df[row_1_int:row_2_int]` | 
# | Select row/column by label | `df.loc[row_label(s), col_label(s)]` |
# | Select row/column by integer | `df.iloc[row_int(s), col_int(s)]` |
# | Select by row integer & column label | `df.loc[df.index[row_int], col_label]` |
# | Select by row label & column integer | `df.loc[row_label, df.columns[col_int]]` | 
# | Select by boolean | `df[bool_vec]` | 
# | Select by boolean expression | `df.query("expression")` | 

# ## Toolbox

# ### Timer wrapper for functions (by Arman)

# ```python
# import time 
# 
# def timer(f): 
#     def wrapper():  
#         t1 = time.time()
#         result = f()  
#         t2 = time.time()
#         print(f"{my_function.__name__} ran in {t2 - t1:.3f} sec") 
#         return result
#     return wrapper
# 
# @timer
# f()
# ```

# ### Array broadcastability (by Arman)

# ```python
# def broadcastable(a, b):
#     print("The shape of a is:" + f"{a.shape}".rjust(10))
#     print("The shape of b is:" + f"{b.shape}".rjust(10))
#     print("")
#     try:
#         print(f"The shape of a + b is: {(a + b).shape}")
#     except:
#         print(f"ERROR: arrays are NOT broadcast compatible!")
# ```

# ## Documentation

# ### NumPy/Scipy 

# ```python
# def function_name(param1, param2, param3):
#     """First line is a short description of the function.
# 
#     A paragraph describing in a bit more detail what the
#     function does and what algorithms it uses and common
#     use cases.
# 
#     Parameters
#     ----------
#     param1 : datatype
#         A description of param1.
#     param2 : datatype
#         A description of param2.
#     param3 : datatype
#         A longer description because maybe this requires
#         more explanation and we can use several lines.
# 
#     Returns
#     -------
#     datatype
#         A description of the output, datatypes and behaviours.
#         Describe special cases and anything the user needs to
#         know to use the function.
# 
#     Examples
#     --------
#     >>> function_name(3,8,-5)
#     2.0
#     """
#     # function content
# ```
