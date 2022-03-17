#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install bs4


# In[2]:


pip install requests


# In[45]:


import requests 
from bs4 import BeautifulSoup
url='https://pricebaba.com/search?category=ELEC-HMENT-TV&from=Televisions'


# In[46]:


response=requests.get(url)


# In[47]:


response


# In[48]:


data=BeautifulSoup(response.text)


# In[49]:


data


# In[50]:


tv=data.select('.ellips-line-ell-2')


# In[51]:


tv


# In[52]:


tv_new= []
for item in tv:
    tv_new.append(item.text)
    link="https://pricebaba.com/"+item["href"]


# In[53]:


tv_new


# In[54]:


amount=data.select('.d-block .txt-al-c')


# In[55]:


amount


# In[56]:


tv_amount=[]
for item in amount:
    tv_amount.append(item.text)


# In[57]:


tv_amount


# In[58]:


vfm=data.select('#productsCnt .p-v-s')


# In[59]:


vfm


# In[60]:


tv_vfm=[]
for item in vfm:
    tv_vfm.append(item.text)


# In[61]:


tv_vfm


# In[70]:


inch=data.select('.m-r-xs:nth-child(1) .d-block')


# In[71]:


inch


# In[72]:


tv_inch=[]
for item in inch:
    tv_inch.append(item.text)
    tv_inch
    


# In[73]:


tv_inch


# In[79]:


pixel=data.select('.m-r-xs:nth-child(2) .d-block')


# In[81]:


pixel


# In[85]:


tv_pixel=[]
for item in pixel:
    tv_pixel.append(item.text)
    


# In[86]:


tv_pixel


# In[89]:


import pandas as pd


# In[90]:


telivision=pd.DataFrame(tv_new,columns=['Tv Name'])


# In[91]:


telivision


# In[92]:


telivision['Price']=tv_amount


# In[94]:


telivision


# In[95]:


telivision ['TV inch']=tv_inch


# In[96]:


telivision


# In[97]:


telivision['TV Pixel']=tv_pixel


# In[98]:


telivision


# In[99]:


telivision['VFM']=tv_vfm


# In[100]:


telivision


# In[ ]:




