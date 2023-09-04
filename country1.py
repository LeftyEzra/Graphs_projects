"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib import style
style.use('Solarize_Light2')
#style.use('dark_background')
name_of_countries = np.array(["Zambia", "Morroco", "Italy", "Vietnam", "panama"])

goals_scored = np.array([11, 10, 8, 12, 11 ])

bar_color = ['orange', 'teal', 'blue', 'red', "orange"]

fig, ax = plt.subplots()
brazil_logo = "zambia.PNG"
pic1 = plt.imread(brazil_logo)
japan_logo = "morroco.PNG"
pic2 = plt.imread(japan_logo)
germany_logo = "italy.PNG"
pic3 = plt.imread(germany_logo)
brazil_logo = "vietnam.PNG"
pic4 = plt.imread(brazil_logo)
southafrica_logo = "panama.PNG"
pic5= plt.imread(southafrica_logo)




image_box1 = OffsetImage(pic1,zoom=.19)
xy = (0,1)
ab_annotation = AnnotationBbox(image_box1, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box2 = OffsetImage(pic2,zoom=.19)
xy = (0.98,1)
ab_annotation = AnnotationBbox(image_box2, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box3 = OffsetImage(pic3,zoom=.19)
xy = (1.98,1)
ab_annotation = AnnotationBbox(image_box3, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box4 = OffsetImage(pic4,zoom=.19)
xy = (2.95,1)
ab_annotation = AnnotationBbox(image_box4, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)


image_box5 = OffsetImage(pic5,zoom=.19)
xy = (3.93,1)
ab_annotation = AnnotationBbox(image_box5, xy, xybox=None,boxcoords="offset points",frameon=False)
ax.add_artist(ab_annotation)

#bg_img = "women_fifa.png"
#pic = plt.imread(bg_img)



for j in range(len(goals_scored)):
    plt.text(x = j - 0.1 , y = goals_scored[j] + 0.1, s = goals_scored[j], size = 15,color="red")



ax.bar(name_of_countries, goals_scored,color=bar_color)
#ax.imshow(pic, extent=[-0.8,5,0,5])
ax.set_yticklabels([])
plt.xticks(name_of_countries,color='green',fontsize=14)
plt.ylabel("Number of goals borrowed".title(),color="red",fontsize=14,fontweight="bold",)
plt.title("Goals  conceded by countries".title(), color="red",fontsize=16,fontweight='bold',pad=20)
plt.show()"""
