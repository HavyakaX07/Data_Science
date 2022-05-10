#!/usr/bin/env python
# coding: utf-8

# # Creating Interactive Widgets

# ## In order to create interacitve widgets we need ipywidgets library lets install it 

# In[1]:


get_ipython().system('pip install ipywidgets')


# ## we need to enable it 

# In[2]:


get_ipython().system('jupyter nbextension enable --py widgetsnbextension --sys-prefix')


# ### importing all the modules

# In[3]:


from ipywidgets import *


# In[4]:


import ipywidgets as wdg


# ### Creating int slider

# int_widgets=wdg.IntSlider(value=2,
#                          min=0,
#                          max=10,
#                          step=1,
#                          description='This is Integer slider',
#                          continuous_update=True,
#                          orientation='Horizontal')

# In[6]:


int_widgets


# In[7]:


int_widgets.value #Gives current value.


# ### Creating int range slider

# In[15]:


int_widgets_1=wdg.IntRangeSlider(value=[2,5],
                         min=0,
                         max=10,
                         step=1,
                         description='This is Integer slider',
                         continuous_update=True,
                         orientation='Horizontal') #also use vertical


# In[16]:


int_widgets_1


# In[11]:


int_widgets_1.value


# ### creating text box

# In[17]:


t=wdg.Text()


# In[18]:


t


# In[30]:


#Creating integer box
int_box=wdg.BoundedIntText(value=0,
                         min=0,
                         max=100,
                         step=5,
                         description='Integer box')


# In[31]:


int_box


# ### check box dropdown radio buttons creating

# In[33]:


#Check box
ch=wdg.Checkbox(value=False,
               description='I like this')


# In[34]:


ch


# In[35]:


#dropdown
dd=wdg.Dropdown(options=['None','Cricket','Vollyball','Football','Kabbaddi'],
               value='None',
               description='Select One')
dd


# In[36]:


#Radio buttons
rb=wdg.RadioButtons(options=['None','Cricket','Vollyball','Football','Kabbaddi'],
                   value='None',
                   description='Select One')
rb


# In[38]:


def click_button(button):
    print('Button clicked!!!')
button=wdg.Button(description='Click me',
                 button_style='success',
                 tooltip='click me magic will happen')
button


# In[39]:


button.on_click(click_button)


# ### Joining two widgets

# In[50]:


pl=wdg.Play(value=10,
           min=0,
           max=1000,
           step=1)
pl
int_widg_1=wdg.IntSlider()
wdg.jslink((pl,'value'),(int_widg_1,'value'))
wdg.VBox([pl,int_widg_1])


# ### we can add widgets through functions also

# In[51]:


def f(x):
    return x
interact(f,x=10) #by seeing the data type only it will add the correspondiing widget


# In[52]:


interact(f,x=True)


# In[53]:


interact(f,x='Hello world')


# ### we can also make use of @interact decorator on top of the function

# In[54]:


@interact(x=10,y=True)
def h(x,y):
    return (x,y)


# ### we can also apply filter on the data frame.

# In[55]:


#creating dummy data frame
import pandas as pd
import numpy as np
index_c=[1,2,3]
cl_list=['Maths','Bio','Chem']
data=np.random.randint(35,99,9).reshape(3,3)
my_df=pd.DataFrame(data,index_c,cl_list)


# In[56]:


my_df


# In[64]:


@interact
def filterBySubjectandMarks(cl='Maths',marks=80):
    return (my_df.loc[my_df[cl]>marks])


# In[ ]:




