import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import datetime
import numpy as np

url = "https://w1.weather.gov/obhistory/KORD.html"
get_obj = requests.get(url).text
soup = BeautifulSoup(get_obj,'lxml')
#print(soup.prettify())
get_table = soup.find('table',{'cellspacing':'3'})
#print(get_table.prettify())
data = get_table.find_all('tr',align='center')
#print(data)
full_list = []
for ele in data:
    #print(ele)
    temp = ele.find_all('td')
    #print(temp)
    full_list.append(temp)

clean_lst = full_list[3:75]

for idx,ele in enumerate(clean_lst):
    print(idx)
    print(ele)

date_lst = []
weather_lst = []
for idx,lst in enumerate(clean_lst):
    temp = []
    for ele in lst:
        text = ele.renderContents()
        text.strip()
        temp.append(text.decode('utf-8'))
    print(temp)
    date_lst.append(datetime.datetime.strptime("04/"+temp[0]+"/2020"+","+temp[1], '%m/%d/%Y,%H:%M'))
    weather_lst.append(int(temp[7]))

print(date_lst)
print(weather_lst)

print(date_lst[::-1])
print(weather_lst[::-1])



#plt.plot(date_lst[::-1],weather_lst[::-1],'r--')
#pyplot.locator_params(axis='y', nbins=6)
#pyplot.locator_params(axis='x', nbins=10)
#plt.show()

to_table_dates, to_table_weather = date_lst[::-1],weather_lst[::-1]

fig, ax = plt.subplots()
ax.plot(to_table_dates,to_table_weather,label = "Temperature in $F$", marker = '.', linestyle = ':',color = 'c')
ax.set_title("Temperature at O'Hare Int'l for the last 72 hours")
fig.autofmt_xdate()
ax.set_xlabel("Dates")
ax.set_ylabel("Temperatures in $F$")
plt.yticks(np.arange(min(to_table_weather) - 10, max(to_table_weather) + 10, 4.0))
ax.legend()
plt.show()





#print(to_df_lst)