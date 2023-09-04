import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

data = pd.read_csv("tinazzecsv.csv")
df = pd.DataFrame(data)


#plotting Pandas as a graph
#pandas uses .plot() method to create figures
#style.use('ggplot')
#style.use('fivethirtyeight')
#style.use('dark_background')
#style.use('classic')
style.use('Solarize_Light2')
#style.use('bmh')
#style.use('tableau-colorblind10')


fig,ax = plt.subplots()
tinaze_logo = "tinazze_igresized.png"
pic5= plt.imread(tinaze_logo)

image_box5 = OffsetImage(pic5,zoom=0)
xy = (2,12)
ab_annotation = AnnotationBbox(image_box5, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)

plt.subplots_adjust(bottom=0.2)

"""xy = (6,9.5)
ax.annotate("This bar_graph represents the quantity of sizes sold.\n"
            "The red color bar represent sizes that only at one quantity.\n"
            "Purple bars for 2 quantities.\n"
            "The blue color represent items that don't use size or items that the\nsizes are not added.\n"
            "The teal color bar represents sizes that are sold at quantity 5.\n"
            "Orange color for 9 quantities.\n"
            "Green for the highest quantity at 19 pairs.\n"
            "Looking at this chart i can say the average your buyers are size 42 users."
            ,xy=xy,clip_on=True,color='green',fontsize=11)


size_counts = df["Size"].value_counts()
#color = ['green', 'orange', 'teal','blue','purple','purple','purple','red','red','red','red','red','red']
barhs = plt.bar(size_counts.index,size_counts.values,color='g')
values = [i for i in range(50)]
#df["Size"].plot(kind = 'hist',color='teal',rwidth=0.5,)


ax.set_xticks(size_counts.index)
plt.xlabel("Sizes bought",color='red',fontweight='bold',fontsize=10)
plt.xticks(rotation=65,color='orange',fontweight='bold',fontstyle='italic')

ax.set_yticks(size_counts.values)
plt.ylabel("Quantities",color="green",fontweight='bold',fontsize=14)
plt.yticks(rotation=360,color='green',fontstyle='italic')
plt.grid(False)"""

colors = ["g","orange",'red']
explode = (0.1,0,0,)
gender_counts = df["Gender"].value_counts()
barhs = plt.bar(gender_counts.index.tolist(),gender_counts.values.tolist(), color='green')
for j in range(len(gender_counts)):
        plt.text(x=j - 0.1, y=gender_counts[j] + 0.1, s=gender_counts[j], size=15, color="green")
plt.title("Gender buyers".title(), fontsize=15)
plt.xticks(rotation=45,fontsize=13,color="blue")
#df["Total"].plot(kind = 'hist',color='g')
#plt.setp(pcts,color='green',fontweight='bold')
#size_counts = df["Size"].value_counts()
"""patches,texts,pcts=plt.pie(size_counts.values,labels=size_counts.index,autopct='%1.1f%%',radius=1.1,
                            rotatelabels=True,pctdistance=0.8,colors=sns.color_palette('Set1'),
                            shadow=True,textprops={'fontsize':12},wedgeprops={'linewidth':0.5,'edgecolor':'white'})

for i, patch in enumerate(patches):
    texts[i].set_color(patch.get_facecolor())
plt.setp(pcts,color='black',fontweight='bold')
plt.setp(texts,fontweight=600)
plt.legend(patches,size_counts.index,loc='lower left',bbox_to_anchor=(1.2,0.5))


plt.title("size%".title(), fontsize=18,color="teal",pad=30,y=3)
plt.title("pie representing sizes of items sold".title(), fontsize=18,color="black",loc='left')"""
plt.show()
"""xy = (0.5,12)
ax.annotate("Analysis for the sales data and recommendations for Production, \n"
            "Base on this barchart findings, we can see that slippers is on fire\nand may be shoes. In other words, "
            "slippers dey sell well.\nThat is to say, it is important and crucial to capitalize on the\n"
            "success of slippers.\n"
            "Slippers has demonstrated a high demand and profitability.\n\n"
            "There may have been lower sales volumns of other items but\nthere could still be "
            "an improvement.",xy=xy,clip_on=True,color='green',fontsize=11)


description_counts= df["Description"].value_counts()
barhs = plt.bar(description_counts.index.tolist(),description_counts.values.tolist(), color='green')

for j in range(len(description_counts)):
    if j < 3:

        plt.text(x=j - 0.1, y=description_counts[j] + 0.1, s=description_counts[j], size=15, color="green")

    elif j >= 3:

        plt.text(x = j - 0.1 , y = description_counts[j] + 0.1, s = description_counts[j], size = 15,color="red")

plt.xlabel("Products",color='red',fontweight='bold',fontsize=10)
plt.xticks(rotation=90,fontsize=12,color='orange',fontweight='bold',fontstyle='italic')

plt.ylabel("Numbers of items sold",color="red",fontweight='bold',fontsize=14)
plt.yticks(rotation=360,color='green',fontstyle='italic')
plt.grid(False)"""
"""
barhs = plt.barh(description_counts.index.tolist(),description_counts.values.tolist(), color='teal')

for barh in ax.patches:
    width = barh.get_width()
    plt.text(0.5+barh.get_width(),barh.get_y()+0.55*barh.get_height(),'{:1}'.format(width),ha='center',va='center',color='yellow')

plt.xlabel("Numbers of items sold",color='red',fontweight='bold',fontsize=14)
plt.xticks(rotation=90,fontsize=12,color='orange',fontweight='bold',fontstyle='italic')

plt.ylabel("Descriptions",color="red",fontweight='bold',fontsize=14)
plt.yticks(rotation=360,color='orange',fontstyle='italic')
plt.grid(False)"""