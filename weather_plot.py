# This is a code to generate line plot for weather data
# need to have 4 columns "Date","Minimum Temperature","Mean Temperature","Maximum Temperature"
# Date shoud be in %m/%d/%y format

#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# impoart data
df=pd.read_csv("weatherdata.csv")

# in case you have "no data." in columns change type "object" to "float64" , this will introduce NaN to any strings present
df['Minimum Temperature']=pd.to_numeric(df['Minimum Temperature'], errors='coerce')
df['Mean Temperature']=pd.to_numeric(df['Mean Temperature'], errors='coerce')
df['Maximum Temperature']=pd.to_numeric(df['Maximum Temperature'], errors='coerce')
# create a new column containing year
df['Month_Year'] = pd.to_datetime(df['Date'],format='%m/%d/%y').apply(lambda x: x.strftime('%b %Y'))
# calculate monthly values
meandf=df.groupby(by=['Month_Year'])[['Minimum Temperature','Mean Temperature','Maximum Temperature']].mean().round(2)
# reset index
meandf.reset_index(inplace=True) 
# create a datetime column "MY" to use for sorting
meandf['MY']=pd.to_datetime(meandf['Month_Year'], format='%b %Y')
# sort by month and year
meandf=meandf.sort_values(by='MY')
# delete the extra columns
meandf.drop('MY', axis=1, inplace=True)
meandf.set_index(meandf['Month_Year'],inplace=True)

# save monthly data values in csv
meandf.to_csv(r'meandata.csv', index = False)

# plotting
plt.rcParams.update({'font.size':15})
ax=meandf.plot(stacked=False,figsize=(20,10),
           kind = 'bar',
           color=['powderblue','orange','red'],
           linewidth=3.0,
           title='Temperature')
ax.set_ylabel("Average Temperature (°F)")
