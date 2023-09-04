import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib import style

style.use('ggplot')
#style.use('fivethirtyeight')
#style.use('dark_background')
#style.use('classic')
#style.use('Solarize_Light2')
#data= pd.read_csv("team_datas.csv")
#print(data)
#df = pd.DataFrame(data)
#ender_counts = df["T1_3pt_Attempts","T2_2pt_Attempts"].value_counts()
#print(df.to_string())
#w= 0.4
#subset = df[['3pts_Attempts','3pts_Made']]
#subset = df.loc[:, ['Team names','3pts_Attempts',"3pts_Made"]]
#print(subset)
#ind = subset.set_index("Team names")
#print(ind)
#subset.plot(kind='bar')
#subset.plot(kind='bar',x="Team names",bottom="hoopers")
#row1 = subset.loc[[1]]

#plt.bar(subset,row1,width=w,label="hoopers" )
#plt.bar(subset,row1,w,label="hoopers" )
x = ["Points","3pts_Attempts",  "3pts_Made",  "2pts_Attempts",  "2pts_Made",  "FT_Attempts",  "FT_Made",  "Off_rebounds",  "Def_rebounds",  "Blocks"]
Hoopers = [82,22, 6, 42, 26, 17, 9, 11, 23, 3]
Raptors   = [52,20, 4, 43, 12, 25, 15, 5, 16, 1]

w = 0.4
bar1= np.arange(len(x))
bar2 = [i + w for i in bar1]
#plt.bar(x,hoopers,w,label="hoopers")
#plt.bar(x,kwara,w,bottom=hoopers,label="kwara")
plt.bar(bar1,Hoopers,w,label="Hoopers",color="green")
plt.bar(bar2,Raptors,w,label="Raptors")
plt.xticks(bar1+w/2,x,color="blue",fontsize=8)

for i in range(len(Hoopers)):
    plt.text(bar1[i], Hoopers[i], str(Hoopers[i]), ha='center', va='bottom',color="green",fontsize=12,)
    plt.text(bar2[i], Raptors[i], str(Raptors[i]), ha='center', va='bottom',color="green")



plt.ylim(0, max(Hoopers + Raptors) * 1.1)
#plt.xlabel("Teams")
plt.ylabel("Stats",color="red")
"""x = ["A", "B", "C", "D", "E"]
boys =[100, 40, 60, 240, 300]
girls= [200, 70,30,120,15]
w = 0.4
bar1 = np.arange(len(x))
bar2 = [i + w for i in bar1]

plt.bar(bar1,boys,width=0.4,label="boys")
plt.bar(bar2,girls,width=0.4,label="girls")

plt.xticks(bar1+w/2,x)
plt.xlabel("courses")
plt.ylabel("students")"""

"""x = ["USA", "RUSSIA", "GRB", "CHINA", "GERMANY"]
gold =[20, 10, 6, 24, 30]
silver= [100, 50,30,120,150]
bronze= [200, 100,60,240,300]
bronze_b = list(np.add(gold,silver))
w =0.2
bar1 = np.arange(len(x))
bar2 = [i + w for i in bar1]
bar3 = [i + w for i in bar2]

plt.bar(bar1,gold,width=w,label="gold")
plt.bar(bar2,silver,width=w,label="silver")
plt.bar(bar3,bronze,width=w,label="bronze")
#plt.bar(x,silver,width=0.4,bottom=gold,label="silver")
#plt.bar(x,bronze,0.4,bottom=bronze_b,label="bronze")

#plt.xticks(bar1+w/2,x)
plt.xlabel("Countries")
plt.ylabel("Medals")"""

"""x = ["A", "B", "C", "D", "E"]
boys =[100, 40, 60, 240, 300]
girls= [200, 70,30,120,15]

plt.bar(x,boys,width=0.2,label="boys")
plt.bar(x,girls,width=0.2,bottom=boys,label="girls")

plt.xlabel("courses")
plt.ylabel("students")"""
plt.title("Game Stats".title(), fontsize=15)
plt.grid(False)
plt.legend()
plt.show()


"""name_of_countries = np.array(["Spain", "Japan", "France", "Netherlands", "Sweden"])

goals_scored = np.array([15,15, 12, 12, 9 ])

bar_color = ['green', 'green', 'blue', 'blue', "red"]

fig, ax = plt.subplots()
brazil_logo = "spain.PNG"
pic1 = plt.imread(brazil_logo)
japan_logo = "japan.PNG"
pic2 = plt.imread(japan_logo)
netherland_logo = "france.PNG"
pic3 = plt.imread(netherland_logo)
sweden_logo = "netherlands.PNG"
pic4 = plt.imread(sweden_logo)
austrialia_logo = "sweden.PNG"
pic5= plt.imread(austrialia_logo)


style.use('Solarize_Light2')

image_box1 = OffsetImage(pic1,zoom=.3)
xy = (0,13.1)
ab_annotation = AnnotationBbox(image_box1, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box2 = OffsetImage(pic2,zoom=.3)
xy = (0.98,13.1)
ab_annotation = AnnotationBbox(image_box2, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box3 = OffsetImage(pic3,zoom=.3)
xy = (1.98,10.2)
ab_annotation = AnnotationBbox(image_box3, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box4 = OffsetImage(pic4,zoom=.3)
xy = (2.95,10.2)
ab_annotation = AnnotationBbox(image_box4, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box5 = OffsetImage(pic5,zoom=.3)
xy = (3.97,7.2)
ab_annotation = AnnotationBbox(image_box5, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)

for j in range(len(goals_scored)):
    plt.text(x = j - 0.1 , y = goals_scored[j] + 0.1, s = goals_scored[j], size = 15,color="red")



ax.bar(name_of_countries, goals_scored,color=bar_color)
ax.set_yticklabels([])
plt.xticks(name_of_countries,color='orange',fontsize=13)
plt.ylabel("Number of goals scored",color="green")
plt.title("Goals by countries", color="green",fontsize=16,fontweight='bold',pad=20)
plt.show()"""