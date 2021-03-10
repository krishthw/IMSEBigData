# This is a code to generate line plot/bar plot for weather data
# need to have 4 columns "Date","Minimum Temperature","Mean Temperature","Maximum Temperature"
# Date shoud be in %m/%d/%y format

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

# impoart data
df=pd.read_csv("January_66502.csv") # all data("2017_2021_weatherdata.csv")
# in case you have "no data." in columns change type "object" to "float64"
# this will introduce NaN to any strings present
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
# meandf.drop('MY', axis=1, inplace=True)
meandf.set_index(meandf['Month_Year'],inplace=True)

# save monthly data values in csv
meandf.to_csv(r'meandata.csv', index = False)

# *** bar/line plot  ***
meandf['baseline']=meandf['Mean Temperature'].mean() # set the baseline to yearly/ or monthly mean

plt.rcParams.update({'font.size':15})
ax=meandf.plot(x='Month_Year',y=['Minimum Temperature','Mean Temperature','Maximum Temperature','baseline'],
           stacked=False,figsize=(20,10),kind='line', # (change kind to 'bar' for bar plot)
           color=['powderblue','orange','red','black'],
           linewidth=3.0,
           title='Temperature Data for 2017 to 2021 - Manhattan KS 66502')
ax.set_ylabel("Average Temperature (°F)")

# **** bar plot with baseline set to Average 5 year mean temperature ****
# to change Month_Date column to datetime, Do not excute following line when plotting only for January to get nice plot
# meandf['Month_Year'] = pd.to_datetime(meandf['Month_Year'])
# custum color 
domain = ['Minimum Temperature','Mean Temperature','Maximum Temperature']
range_ = ['powderblue','orange','red']

plot=alt.Chart(meandf).transform_fold(['Minimum Temperature','Mean Temperature','Maximum Temperature'],
                                ).mark_bar().encode(
    x='Month_Year',y2='baseline',
    color=alt.Color('key:N', scale=alt.Scale(domain=domain, range=range_)),
    column='key:N',
    y=alt.Y('value:Q', axis=alt.Axis(title='Average Temperature (°F)'))).properties(
    width=300,height=400,title='Temperature Data for 2017 to 2021 - Manhattan KS 66502')
plot.configure_title(anchor='middle')
