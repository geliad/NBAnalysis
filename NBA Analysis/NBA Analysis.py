
# coding: utf-8

# In[2]:


#take data from last 10 years
#investigate trends, patterns that you see in their performance
#Games Played, Minutes per Game, FG%(Field Goals), PPG (Points per Game)
#www.superdatascience.com/python download basketball dataset

#Instructions for this dataset:
# Simply copy ALL the lines in this script by pressing 
# CTRL+A on Windows or CMND+A on Mac and run the Jupyter cell
# Once you have executed the commands the following objects
# will be created:
# Matrices:
# - Salary
# - Games
# - MinutesPlayed
# - FieldGoals
# - FieldGoalAttempts
# - Points
# Lists:
# - Players
# - Seasons
# Dictionaries:
# - Sdict
# - Pdict
#We will understand these inside the course.


#Comments:
#Seasons are labeled based on the first year in the season
#E.g. the 2012-2013 season is preseneted as simply 2012

#Notes and Corrections to the data:
#Kevin Durant: 2006 - College Data Used
#Kevin Durant: 2005 - Proxied With 2006 Data
#Derrick Rose: 2012 - Did Not Play
#Derrick Rose: 2007 - College Data Used
#Derrick Rose: 2006 - Proxied With 2007 Data
#Derrick Rose: 2005 - Proxied With 2007 Data

#Import numpy
import numpy as np

#Seasons
Seasons = ["2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
Sdict = {"2005":0,"2006":1,"2007":2,"2008":3,"2009":4,"2010":5,"2011":6,"2012":7,"2013":8,"2014":9}

#Players
Players = ["KobeBryant","JoeJohnson","LeBronJames","CarmeloAnthony","DwightHoward","ChrisBosh","ChrisPaul","KevinDurant","DerrickRose","DwayneWade"]
Pdict = {"KobeBryant":0,"JoeJohnson":1,"LeBronJames":2,"CarmeloAnthony":3,"DwightHoward":4,"ChrisBosh":5,"ChrisPaul":6,"KevinDurant":7,"DerrickRose":8,"DwayneWade":9}

#Salaries
KobeBryant_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
JoeJohnson_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
LeBronJames_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
CarmeloAnthony_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
DwightHoward_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
ChrisBosh_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
ChrisPaul_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
KevinDurant_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
DerrickRose_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
DwayneWade_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]

#Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary, ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])

#Games 
KobeBryant_G = [80,77,82,82,73,82,58,78,6,35]
JoeJohnson_G = [82,57,82,79,76,72,60,72,79,80]
LeBronJames_G = [79,78,75,81,76,79,62,76,77,69]
CarmeloAnthony_G = [80,65,77,66,69,77,55,67,77,40]
DwightHoward_G = [82,82,82,79,82,78,54,76,71,41]
ChrisBosh_G = [70,69,67,77,70,77,57,74,79,44]
ChrisPaul_G = [78,64,80,78,45,80,60,70,62,82]
KevinDurant_G = [35,35,80,74,82,78,66,81,81,27]
DerrickRose_G = [40,40,40,81,78,81,39,0,10,51]
DwayneWade_G = [75,51,51,79,77,76,49,69,54,62]

#Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G, KevinDurant_G, DerrickRose_G, DwayneWade_G])

#Minutes Played
KobeBryant_MP = [3277,3140,3192,2960,2835,2779,2232,3013,177,1207]
JoeJohnson_MP = [3340,2359,3343,3124,2886,2554,2127,2642,2575,2791]
LeBronJames_MP = [3361,3190,3027,3054,2966,3063,2326,2877,2902,2493]
CarmeloAnthony_MP = [2941,2486,2806,2277,2634,2751,1876,2482,2982,1428]
DwightHoward_MP = [3021,3023,3088,2821,2843,2935,2070,2722,2396,1223]
ChrisBosh_MP = [2751,2658,2425,2928,2526,2795,2007,2454,2531,1556]
ChrisPaul_MP = [2808,2353,3006,3002,1712,2880,2181,2335,2171,2857]
KevinDurant_MP = [1255,1255,2768,2885,3239,3038,2546,3119,3122,913]
DerrickRose_MP = [1168,1168,1168,3000,2871,3026,1375,0,311,1530]
DwayneWade_MP = [2892,1931,1954,3048,2792,2823,1625,2391,1775,1971]

#Matrix
MinutesPlayed = np.array([KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP, KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

#Field Goals
KobeBryant_FG = [978,813,775,800,716,740,574,738,31,266]
JoeJohnson_FG = [632,536,647,620,635,514,423,445,462,446]
LeBronJames_FG = [875,772,794,789,768,758,621,765,767,624]
CarmeloAnthony_FG = [756,691,728,535,688,684,441,669,743,358]
DwightHoward_FG = [468,526,583,560,510,619,416,470,473,251]
ChrisBosh_FG = [549,543,507,615,600,524,393,485,492,343]
ChrisPaul_FG = [407,381,630,631,314,430,425,412,406,568]
KevinDurant_FG = [306,306,587,661,794,711,643,731,849,238]
DerrickRose_FG = [208,208,208,574,672,711,302,0,58,338]
DwayneWade_FG = [699,472,439,854,719,692,416,569,415,509]

#Matrix
FieldGoals  = np.array([KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG, KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])

#Field Goal Attempts
KobeBryant_FGA = [2173,1757,1690,1712,1569,1639,1336,1595,73,713]
JoeJohnson_FGA = [1395,1139,1497,1420,1386,1161,931,1052,1018,1025]
LeBronJames_FGA = [1823,1621,1642,1613,1528,1485,1169,1354,1353,1279]
CarmeloAnthony_FGA = [1572,1453,1481,1207,1502,1503,1025,1489,1643,806]
DwightHoward_FGA = [881,873,974,979,834,1044,726,813,800,423]
ChrisBosh_FGA = [1087,1094,1027,1263,1158,1056,807,907,953,745]
ChrisPaul_FGA = [947,871,1291,1255,637,928,890,856,870,1170]
KevinDurant_FGA = [647,647,1366,1390,1668,1538,1297,1433,1688,467]
DerrickRose_FGA = [436,436,436,1208,1373,1597,695,0,164,835]
DwayneWade_FGA = [1413,962,937,1739,1511,1384,837,1093,761,1084]

#Matrix
FieldGoalAttempts = np.array([KobeBryant_FGA, JoeJohnson_FGA, LeBronJames_FGA, CarmeloAnthony_FGA, DwightHoward_FGA, ChrisBosh_FGA, ChrisPaul_FGA, KevinDurant_FGA, DerrickRose_FGA, DwayneWade_FGA])

#Points
KobeBryant_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
JoeJohnson_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
LeBronJames_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
CarmeloAnthony_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
DwightHoward_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
ChrisBosh_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
ChrisPaul_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
KevinDurant_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
DerrickRose_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
DwayneWade_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]

#Matrix
Points = np.array([KobeBryant_PTS, JoeJohnson_PTS, LeBronJames_PTS, CarmeloAnthony_PTS, DwightHoward_PTS, ChrisBosh_PTS, ChrisPaul_PTS, KevinDurant_PTS, DerrickRose_PTS, DwayneWade_PTS])  

#Copyright: These datasets were prepared using publicly available data.
#           However, theses scripts are subject to Copyright Laws. 
#           If you wish to use these Python scripts outside of the Python Programming Course
#           by Kirill Eremenko, you may do so by referencing www.superdatascience.com in your work.


# In[3]:


import numpy as np
mydata = np.arange(0,20)
mydata
np.reshape(mydata, (5,4)) #Default is opposite to R!!
MATR1 = np.reshape(mydata, (5,4), order = 'C')
MATR1
MATR2 = np.reshape(mydata, (5,4), order = 'F')
MATR2

mydata.reshape(5,4)


# ---

# In[4]:


#DICTIONARIES 
Games[0] #Kobi


# In[5]:


Games[2] #Labron


# In[6]:


dict1 = {'key1':'val1', 'key2':'val2','key3':'val3'} 


# In[7]:


#Sdict = xeroumen see pio row en i kathe season!
#Players dict = xeroumen se pio row en o kathe paixtis!
#Rows en oi paixtes, Columns en oi xronies, GIAUTO KAI KANOUME 2 DICTIONARIES!!!


# In[8]:


Games


# In[9]:


Pdict['DerrickRose']
Games[8] 
Games[Pdict["DerrickRose"]]


# In[10]:


Games[Pdict['DerrickRose']][Sdict['2012']]
Games[Pdict['DerrickRose'],Sdict['2012']]


# In[11]:


Points[Pdict["LeBronJames"]].mean() #.max(), .min()


# In[12]:


Points[Pdict["KobeBryant"]].mean()


# In[13]:


Salary[Pdict["LeBronJames"],Sdict['2009']]


# ---

# In[14]:


FieldGoals


# In[15]:


Games


# In[16]:


#Field goals per games
import warnings
warnings.filterwarnings('ignore')

FieldGoalsPerGame = np.matrix.round(FieldGoals/Games)


# In[17]:


FieldGoalsPerGame[Pdict['KobeBryant'],Sdict['2009']]


# In[18]:


MinutesPerGame = np.matrix.round(MinutesPlayed/Games)


# In[19]:


FieldGoalsPerAttempt = np.matrix.round(FieldGoals / FieldGoalAttempts, 2) * 100
FieldGoalsPerAttempt


# ---

# In[40]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']=10,6


# In[41]:


plt.plot(Salary[0]/Games[0], c = 'black', ls = '--', marker = 's',ms = 17, label = 'Players[0]')
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()
Salary[0]


# In[42]:


plt.plot(Salary, label = Players)
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()


# In[43]:


# we want to add all the players and a LEGEND!
#SALARY MATRIX
plt.plot(Salary[0], c = 'black', ls = '--', marker = 's',ms = 7, label = Players[0])
plt.plot(Salary[1], c = 'red', ls = '--', marker = 'o',ms = 7, label = Players[1])
plt.plot(Salary[2], c = 'green', ls = '--', marker = '^',ms = 7, label = Players[2])
plt.plot(Salary[3], c = 'blue', ls = '--', marker = 'd',ms = 7, label = Players[3])
plt.plot(Salary[4], c = 'magenta', ls = '--', marker = 's',ms = 7, label = Players[4])
plt.plot(Salary[5], c = 'black', ls = '--', marker = 'o',ms = 7, label = Players[5])
plt.plot(Salary[6], c = 'red', ls = '--', marker = '^',ms = 7, label = Players[6])
plt.plot(Salary[7], c = 'green', ls = '--', marker = 'd',ms = 7, label = Players[7])
plt.plot(Salary[8], c = 'blue', ls = '--', marker = 's',ms = 7, label = Players[8])
plt.plot(Salary[9], c = 'magenta', ls = '--', marker = 'o',ms = 7, label = Players[9])
plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()


# In[44]:


#GAMES MATRIX
plt.plot(Games[0], c = 'black', ls = '--', marker = 's',ms = 7, label = Players[0])
plt.plot(Games[1], c = 'red', ls = '--', marker = 'o',ms = 7, label = Players[1])
plt.plot(Games[2], c = 'green', ls = '--', marker = '^',ms = 7, label = Players[2])
plt.plot(Games[3], c = 'blue', ls = '--', marker = 'd',ms = 7, label = Players[3])
plt.plot(Games[4], c = 'magenta', ls = '--', marker = 's',ms = 7, label = Players[4])
plt.plot(Games[5], c = 'black', ls = '--', marker = 'o',ms = 7, label = Players[5])
plt.plot(Games[6], c = 'red', ls = '--', marker = '^',ms = 7, label = Players[6])
plt.plot(Games[7], c = 'green', ls = '--', marker = 'd',ms = 7, label = Players[7])
plt.plot(Games[8], c = 'blue', ls = '--', marker = 's',ms = 7, label = Players[8])
plt.plot(Games[9], c = 'magenta', ls = '--', marker = 'o',ms = 7, label = Players[9])
plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()


# In[45]:


#FIELD GOALS PER GAMES/ACCURACY AND MINUTES PER GAME VISUALIZE
plt.plot(FieldGoalsPerGame[0], c = 'black', ls = '--', marker = 's',ms = 7, label = Players[0])
plt.plot(FieldGoalsPerGame[1], c = 'red', ls = '--', marker = 'o',ms = 7, label = Players[1])
plt.plot(FieldGoalsPerGame[2], c = 'green', ls = '--', marker = '^',ms = 7, label = Players[2])
plt.plot(FieldGoalsPerGame[3], c = 'blue', ls = '--', marker = 'd',ms = 7, label = Players[3])
plt.plot(FieldGoalsPerGame[4], c = 'magenta', ls = '--', marker = 's',ms = 7, label = Players[4])
plt.plot(FieldGoalsPerGame[5], c = 'black', ls = '--', marker = 'o',ms = 7, label = Players[5])
plt.plot(FieldGoalsPerGame[6], c = 'red', ls = '--', marker = '^',ms = 7, label = Players[6])
plt.plot(FieldGoalsPerGame[7], c = 'green', ls = '--', marker = 'd',ms = 7, label = Players[7])
plt.plot(FieldGoalsPerGame[8], c = 'blue', ls = '--', marker = 's',ms = 7, label = Players[8])
plt.plot(FieldGoalsPerGame[9], c = 'magenta', ls = '--', marker = 'o',ms = 7, label = Players[9])
plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()
FieldGoalsPerGame


# In[46]:


plt.plot(MinutesPerGame[0], c = 'black', ls = '--', marker = 's',ms = 7, label = Players[0])
plt.plot(MinutesPerGame[1], c = 'red', ls = '--', marker = 'o',ms = 7, label = Players[1])
plt.plot(MinutesPerGame[2], c = 'green', ls = '--', marker = '^',ms = 7, label = Players[2])
plt.plot(MinutesPerGame[3], c = 'blue', ls = '--', marker = 'd',ms = 7, label = Players[3])
plt.plot(MinutesPerGame[4], c = 'magenta', ls = '--', marker = 's',ms = 7, label = Players[4])
plt.plot(MinutesPerGame[5], c = 'black', ls = '--', marker = 'o',ms = 7, label = Players[5])
plt.plot(MinutesPerGame[6], c = 'red', ls = '--', marker = '^',ms = 7, label = Players[6])
plt.plot(MinutesPerGame[7], c = 'green', ls = '--', marker = 'd',ms = 7, label = Players[7])
plt.plot(MinutesPerGame[8], c = 'blue', ls = '--', marker = 's',ms = 7, label = Players[8])
plt.plot(MinutesPerGame[9], c = 'magenta', ls = '--', marker = 'o',ms = 7, label = Players[9])
plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
plt.show()


# In[47]:


#FUNCTIONS:
def graph(color):
    for i in range(0,10):
        plt.plot(Games[i], c = color, ls = '--', marker = 's',ms = 7, label = Players[i])
plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
graph('black')


# In[48]:


def myplot(playerlist):
    for name in playerlist:
        plt.plot(Games[Pdict[name]], c = 'black', ls = '--', marker = 's',ms = 7, label = name)
    plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
    plt.show()


# In[49]:


myplot(["KobeBryant", "LeBronJames", "DerrickRose"])


# In[50]:



def myplot(playerlist):
    #Dictionary = {'key1':'val1', 'key2':'val2','key3':'val3'}
    Col = {"KobeBryant":"black","JoeJohnson":"red","LeBronJames":"green","CarmeloAnthony":"blue","DwightHoward":"magenta","ChrisBosh":"black","ChrisPaul":"red","KevinDurant":"green","DerrickRose":"blue","DwayneWade":"magenta"}
    Mar = {"KobeBryant":"s","JoeJohnson":"o","LeBronJames":"^","CarmeloAnthony":"d","DwightHoward":"s","ChrisBosh":"o","ChrisPaul":"^","KevinDurant":"d","DerrickRose":"s","DwayneWade":"o"}
    for name in playerlist:
        plt.plot(Games[Pdict[name]], c = Col[name], ls = '--', marker = Mar[name],ms = 7, label = name)
    plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
    plt.show()
    
myplot(["CarmeloAnthony", "DerrickRose"])


# In[51]:



#I specify a default value, so If I don't enter any players , default value will be entered by default
def myplot(data , playerlist = Players):
    #Dictionary = {'key1':'val1', 'key2':'val2','key3':'val3'}
    Col = {"KobeBryant":"black","JoeJohnson":"red","LeBronJames":"green","CarmeloAnthony":"blue","DwightHoward":"magenta","ChrisBosh":"black","ChrisPaul":"red","KevinDurant":"green","DerrickRose":"blue","DwayneWade":"magenta"}
    Mar = {"KobeBryant":"s","JoeJohnson":"o","LeBronJames":"^","CarmeloAnthony":"d","DwightHoward":"s","ChrisBosh":"o","ChrisPaul":"^","KevinDurant":"d","DerrickRose":"s","DwayneWade":"o"}
    for name in playerlist:
        plt.plot(data[Pdict[name]], c = Col[name], ls = '--', marker = Mar[name],ms = 7, label = name)
    plt.legend(loc = 'upper left', bbox_to_anchor=(1,1))
    plt.xticks(list(range(0,10)),Seasons, rotation = 'vertical')
    plt.show()
    
myplot(Points,["KobeBryant", "LeBronJames", "DerrickRose"])


# In[52]:


myplot(Salary)


# In[53]:


#BASKETBALL INSIGHTS!!!
myplot(Games)


# In[54]:


myplot(Salary)
myplot(Salary/Games)
myplot(Salary/FieldGoals)


# In[55]:


#INGAME METRICS
myplot(MinutesPlayed)
myplot(Points)


# In[56]:


#NORMALIZE
myplot(FieldGoals / Games)
#ACCURACY! O DwightHoward has the best accuracy ! Let's see more
myplot(FieldGoals/ FieldGoalAttempts) 
# Looking at this one, we see that he makes ta fewest attempts that's why he has high accuracy
myplot(FieldGoalAttempts / Games) 
myplot(Points / Games)


# In[57]:


myplot(MinutesPlayed / Games)
myplot(Games)


# In[58]:


myplot(FieldGoals/MinutesPlayed)


# In[59]:


myplot(Points/FieldGoals) 
#We observe that the players started shooting more 3pt, that's why the Pts/FG has increased!

