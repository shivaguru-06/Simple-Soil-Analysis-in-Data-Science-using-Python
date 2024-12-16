#Soil Analysis Using DataScience
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Welcome")
print("\n")
print("Different types of soil on normal Climatic Condition")
print("\n")
print("Types of Soil")
print("\n")
s=["Red Soil","Black soil","Alluvial soil","Laterite soil","Coastal Sandy soil"]
soil=pd.Series(s,index=[1,2,3,4,5])
print(soil,end="")
print("\n")

print("Enter the type of soil in your area :")
soiltype=int(input())
if(soiltype==1):
    print('''
Crops which grow in Red Soil:
    1.Cotton
    2.Wheat
    3.Pulses:Gram,pigeon pea,and red gram
    4.Jowar
    5.Linseed
    6.Millet
    7.Potatoes
''')

elif(soiltype==2):
    print('''
Crops which grow in Black Soil:
    1.Cotton
    2.Wheat
    3.Groundnut
    4.Sugarcane
    5.Rice
    6.Linseed
    7.Sunflower
''')

elif(soiltype==3):
    print('''
Crops which grow in Alluvial Soil:
    1.Rice
    2.Wheat
    3.Pulses:Gram,pigeon pea,and red gram
    4.Fruits
    5.Jute
    6.Oilseeds
    7.Turmeric
''')

elif(soiltype==4):
    print('''
Crops which grow in Laterite Soil:
    1.Coffee
    2.Tea
    3.Rubber
    4.Coconut
    5.Pineapple
    6.Cashew
    7.Tobacco
''')

elif(soiltype==5):
    print('''
Crops which grow in Coastal Sandy Soil:
    1.Carrot
    2.Beetroot
    3.Cucumber
    4.Muskmelon
    5.Watermelon
    6.Raddish
    7.Cactus
''')    
else:
    print("No crops to grow")

print("\n")

print("Do you need further details of soil: yes/No")
p=input()

if(p=='yes'):
    if(soiltype==1):
       Soilcontent=["Moisture","Chemical composition","pH level"]
       percentage=[16.2,10.4,5.2]
       plt.pie(percentage,labels=Soilcontent,autopct="%5.2f%%")
       plt.title("Red soil content prediction")
       plt.show()
       
    elif(soiltype==2):
       Soilcontent=["Moisture","Chemical composition","pH level"]
       percentage=[19.6,8.4,5.6]
       plt.pie(percentage,labels=Soilcontent,autopct="%5.2f%%")
       plt.title("Black soil content prediction")
       plt.show()

    elif(soiltype==3):
       Soilcontent=["Moisture","Chemical composition","pH level"]
       percentage=[11.2,8.4,8.2]
       plt.pie(percentage,labels=Soilcontent,autopct="%5.2f%%")
       plt.title("Alluvial soil content prediction")
       plt.show()


    elif(soiltype==4):
       Soilcontent=["Moisture","Chemical composition","pH level"]
       percentage=[10.5,4.4,8.2]
       plt.pie(percentage,labels=Soilcontent,autopct="%5.2f%%")
       plt.title("Laterite soil content prediction")
       plt.show()

    elif(soiltype==5):
       Soilcontent=["Moisture","Chemical composition","pH level"]
       percentage=[16.2,11.1,2.2]
       plt.pie(percentage,labels=Soilcontent,autopct="%5.2f%%")
       plt.title("Coastal Sandy soil content prediction")
       plt.show()

    else:
        print("Sorry! There was no soil found")

       

print("Thank you!!!")



