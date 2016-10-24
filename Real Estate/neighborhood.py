# westlimit=-97.630756; southlimit=30.496073; eastlimit=-97.612903; northlimit=30.508941

import matplotlib.pyplot as plt
import matplotlib.cm
import pandas as pd #this is the standard
import numpy as np

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

df1 = []

#import data
df=pd.read_csv('property_locations')
df.head()
#Format Data
df['Lng'] = df['Lng'].str.lstrip('[').str.rstrip(']') #Remove first and last character. The brackets were annoying
df['Latitude'] = df['Latitude'].str.lstrip('[').str.rstrip(']') #Remove first and last character. The brackets were annoying
df['LP$SqFt'] = df['LP$SqFt'].str.lstrip('$')

df['Lng']= pd.to_numeric(df['Lng']) #convert to a float
df['Latitude']= pd.to_numeric(df['Latitude']) #convert to a float


least_long = df['Lng'].min() - .01
most_long = df['Lng'].max() + .01
print(least_long)
print(most_long)

least_lat = df['Latitude'].min() - .01
most_lat = df['Latitude'].max() + .01
print(least_lat)
print(most_lat)


#create map
m = Basemap(resolution='i', # c, l, i, h, f or None
            projection='merc',  area_thresh = 0.1,
            lat_0=30, lon_0=-97,
            llcrnrlon=least_long, llcrnrlat= least_lat, urcrnrlon=most_long, urcrnrlat=most_lat)
            
#Define map properties
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')



print(df)
#plot points
#x, y, colour= m(df['Lng'].values, df['Latitude'].values)
#m.plot(x, y, 'o', colour ,  markersize=6)
m.plot(df['Lng'].values, df['Latitude'].values,  'o',   c={df['c']}, latlon= True)
plt.show()

# i=0

# while i <24:
# 	for list in df['Address']:
# 		lon= df.get_value(i, 'Lng', takeable=False)
# 		lat= df.get_value(i, 'Latitude', takeable=False)
# 		colour= df.get_value(i, 'c', takeable=False)
# 		#print(colour)
# 		m.plot(lon, lat, 'o', c=colour)
# 		i+=1
plt.show()