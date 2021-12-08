# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:32:54 2021

@author: Cristian
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# from scipy.interpolate import make_interp_spline

# Read in file for criterion percentages
data_m1 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m2 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m6 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m7 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m8 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m9 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m11 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 11/Processed Data/separate-criterion-percentages-mouse1-5days.csv")
data_m5 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Processed Data/12-3-criterion-percentages-mouse5-6days.csv")
data_m3 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/Processed Data/separate-criterion-percentages-mouse3-3days.csv")
data_m4 = pd.read_csv(
    r"C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/Processed Data/separate-criterion-percentages-mouse4-3days.csv")

cs_p1_list_m1 = list(data_m1['CS+1'])
cs_p2_list_m1 = list(data_m1['CS+2'])
cs_m1_list_m1 = list(data_m1['CS-1'])
cs_m2_list_m1 = list(data_m1['CS-2'])

cs_p1_list_m2 = list(data_m2['CS+1'])
cs_p2_list_m2 = list(data_m2['CS+2'])
cs_m1_list_m2 = list(data_m2['CS-1'])
cs_m2_list_m2 = list(data_m2['CS-2'])

cs_p1_list_m6 = list(data_m6['CS+1'])
cs_p2_list_m6 = list(data_m6['CS+2'])
cs_m1_list_m6 = list(data_m6['CS-1'])
cs_m2_list_m6 = list(data_m6['CS-2'])

cs_p1_list_m7 = list(data_m7['CS+1'])
cs_p2_list_m7 = list(data_m7['CS+2'])
cs_m1_list_m7 = list(data_m7['CS-1'])
cs_m2_list_m7 = list(data_m7['CS-2'])

cs_p1_list_m8 = list(data_m8['CS+1'])
cs_p2_list_m8 = list(data_m8['CS+2'])
cs_m1_list_m8 = list(data_m8['CS-1'])
cs_m2_list_m8 = list(data_m8['CS-2'])

cs_p1_list_m9 = list(data_m9['CS+1'])
cs_p2_list_m9 = list(data_m9['CS+2'])
cs_m1_list_m9 = list(data_m9['CS-1'])
cs_m2_list_m9 = list(data_m9['CS-2'])

cs_p1_list_m11 = list(data_m11['CS+1'])
cs_p2_list_m11 = list(data_m11['CS+2'])
cs_m1_list_m11 = list(data_m11['CS-1'])
cs_m2_list_m11 = list(data_m11['CS-2'])

cs_p1_list_m5 = list(data_m5['CS+1'])
cs_p2_list_m5 = list(data_m5['CS+2'])
cs_m1_list_m5 = list(data_m5['CS-1'])
cs_m2_list_m5 = list(data_m5['CS-2'])

cs_p1_list_m3 = list(data_m3['CS+1'])
cs_p2_list_m3 = list(data_m3['CS+2'])
cs_m1_list_m3 = list(data_m3['CS-1'])
cs_m2_list_m3 = list(data_m3['CS-2'])

cs_p1_list_m4 = list(data_m4['CS+1'])
cs_p2_list_m4 = list(data_m4['CS+2'])
cs_m1_list_m4 = list(data_m4['CS-1'])
cs_m2_list_m4 = list(data_m4['CS-2'])
# g1 diff odors
# g2 cs+ cs- avg + std
# g3 cs+ all mice (halo control)/ cs- all mice (halo control)
# g4 cs+ halo-control/ cs- halo-control

x_vals = [i for i in range(0, len(cs_p1_list_m1))]
x_vals_2 = [i for i in range(0, len(cs_p1_list_m3))]
x_vals_3 = [i for i in range(0, len(cs_p1_list_m5))]

plt.plot(x_vals, cs_p1_list_m1, color='yellow')
plt.plot(x_vals, cs_p2_list_m1, color='orange')
plt.plot(x_vals, cs_m1_list_m1, color='brown')
plt.plot(x_vals, cs_m2_list_m1, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/Processed Data/4-odor-1c-mouse1.png')

plt.plot(x_vals, cs_p1_list_m2, color='yellow')
plt.plot(x_vals, cs_p2_list_m2, color='orange')
plt.plot(x_vals, cs_m1_list_m2, color='brown')
plt.plot(x_vals, cs_m2_list_m2, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/Processed Data/4-odor-1c-mouse2.png')

plt.plot(x_vals, cs_p1_list_m6, color='yellow')
plt.plot(x_vals, cs_p2_list_m6, color='orange')
plt.plot(x_vals, cs_m1_list_m6, color='brown')
plt.plot(x_vals, cs_m2_list_m6, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/Processed Data/4-odor-1c-mouse6.png')

plt.plot(x_vals, cs_p1_list_m7, color='yellow')
plt.plot(x_vals, cs_p2_list_m7, color='orange')
plt.plot(x_vals, cs_m1_list_m7, color='brown')
plt.plot(x_vals, cs_m2_list_m7, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/Processed Data/4-odor-1c-mouse7.png')

plt.plot(x_vals, cs_p1_list_m8, color='yellow')
plt.plot(x_vals, cs_p2_list_m8, color='orange')
plt.plot(x_vals, cs_m1_list_m8, color='brown')
plt.plot(x_vals, cs_m2_list_m8, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/Processed Data/4-odor-1c-mouse8.png')

plt.plot(x_vals, cs_p1_list_m9, color='yellow')
plt.plot(x_vals, cs_p2_list_m9, color='orange')
plt.plot(x_vals, cs_m1_list_m9, color='brown')
plt.plot(x_vals, cs_m2_list_m9, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/Processed Data/4-odor-1c-mouse9.png')

plt.plot(x_vals, cs_p1_list_m11, color='yellow')
plt.plot(x_vals, cs_p2_list_m11, color='orange')
plt.plot(x_vals, cs_m1_list_m11, color='brown')
plt.plot(x_vals, cs_m2_list_m11, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 11/Processed Data/4-odor-1c-mouse11.png')

plt.plot(x_vals_3, cs_p1_list_m5, color='yellow')
plt.plot(x_vals_3, cs_p2_list_m5, color='orange')
plt.plot(x_vals_3, cs_m1_list_m5, color='brown')
plt.plot(x_vals_3, cs_m2_list_m5, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Processed Data/4-odor-1c-mouse5.png')

plt.plot(x_vals_2, cs_p1_list_m3, color='yellow')
plt.plot(x_vals_2, cs_p2_list_m3, color='orange')
plt.plot(x_vals_2, cs_m1_list_m3, color='brown')
plt.plot(x_vals_2, cs_m2_list_m3, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/Processed Data/4-odor-1c-mouse3.png')

plt.plot(x_vals_2, cs_p1_list_m4, color='yellow')
plt.plot(x_vals_2, cs_p2_list_m4, color='orange')
plt.plot(x_vals_2, cs_m1_list_m4, color='brown')
plt.plot(x_vals_2, cs_m2_list_m4, color='green')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/Processed Data/4-odor-1c-mouse4.png')

# This is the avg cs + cs - graph make this for all the 10 mice as was done above
cs_p_list_m1 = np.add(cs_p1_list_m1, cs_p2_list_m1)
cs_p_list_m1 = [i / 2 for i in cs_p_list_m1]
cs_m_list_m1 = np.add(cs_m1_list_m1, cs_m2_list_m1)
cs_m_list_m1 = [i / 2 for i in cs_m_list_m1]

cs_p_list_m2 = np.add(cs_p1_list_m2, cs_p2_list_m2)
cs_p_list_m2= [i / 2 for i in cs_p_list_m2]
cs_m_list_m2 = np.add(cs_m1_list_m2, cs_m2_list_m2)
cs_m_list_m2 = [i / 2 for i in cs_m_list_m2]

cs_p_list_m3 = np.add(cs_p1_list_m3, cs_p2_list_m3)
cs_p_list_m3 = [i / 2 for i in cs_p_list_m3]
cs_m_list_m3 = np.add(cs_m1_list_m3, cs_m2_list_m3)
cs_m_list_m3 = [i / 2 for i in cs_m_list_m3]

cs_p_list_m4 = np.add(cs_p1_list_m4, cs_p2_list_m4)
cs_p_list_m4 = [i / 2 for i in cs_p_list_m4]
cs_m_list_m4 = np.add(cs_m1_list_m4, cs_m2_list_m4)
cs_m_list_m4 = [i / 2 for i in cs_m_list_m4]

cs_p_list_m5 = np.add(cs_p1_list_m5, cs_p2_list_m5)
cs_p_list_m5 = [i / 2 for i in cs_p_list_m5]
cs_m_list_m5 = np.add(cs_m1_list_m5, cs_m2_list_m5)
cs_m_list_m5 = [i / 2 for i in cs_m_list_m5]

cs_p_list_m6 = np.add(cs_p1_list_m1, cs_p2_list_m1)
cs_p_list_m6 = [i / 2 for i in cs_p_list_m1]
cs_m_list_m6 = np.add(cs_m1_list_m1, cs_m2_list_m1)
cs_m_list_m6 = [i / 2 for i in cs_m_list_m1]

cs_p_list_m7 = np.add(cs_p1_list_m7, cs_p2_list_m7)
cs_p_list_m7 = [i / 2 for i in cs_p_list_m7]
cs_m_list_m7 = np.add(cs_m1_list_m7, cs_m2_list_m7)
cs_m_list_m7 = [i / 2 for i in cs_m_list_m7]

cs_p_list_m8 = np.add(cs_p1_list_m8, cs_p2_list_m8)
cs_p_list_m8 = [i / 2 for i in cs_p_list_m8]
cs_m_list_m8 = np.add(cs_m1_list_m8, cs_m2_list_m8)
cs_m_list_m8 = [i / 2 for i in cs_m_list_m8]

cs_p_list_m9 = np.add(cs_p1_list_m9, cs_p2_list_m9)
cs_p_list_m9 = [i / 2 for i in cs_p_list_m9]
cs_m_list_m9 = np.add(cs_m1_list_m9, cs_m2_list_m9)
cs_m_list_m9 = [i / 2 for i in cs_m_list_m9]

cs_p_list_m11 = np.add(cs_p1_list_m11, cs_p2_list_m11)
cs_p_list_m11 = [i / 2 for i in cs_p_list_m11]
cs_m_list_m11 = np.add(cs_m1_list_m11, cs_m2_list_m11)
cs_m_list_m11 = [i / 2 for i in cs_m_list_m11]

plt.plot(x_vals, cs_p_list_m1, color='green')
plt.plot(x_vals, cs_m_list_m1, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 1/Processed Data/cs-1c-mouse1.png')

plt.plot(x_vals, cs_p_list_m2, color='green')
plt.plot(x_vals, cs_m_list_m2, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 2/Processed Data/cs-1c-mouse2.png')

plt.plot(x_vals, cs_p_list_m6, color='green')
plt.plot(x_vals, cs_m_list_m6, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 6/Processed Data/cs-1c-mouse6.png')

plt.plot(x_vals, cs_p_list_m7, color='green')
plt.plot(x_vals, cs_m_list_m7, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 7/Processed Data/cs-1c-mouse7.png')

plt.plot(x_vals, cs_p_list_m8, color='green')
plt.plot(x_vals, cs_m_list_m8, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 8/Processed Data/cs-1c-mouse8.png')

plt.plot(x_vals, cs_p_list_m9, color='green')
plt.plot(x_vals, cs_m_list_m9, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 9/Processed Data/cs-1c-mouse9.png')

plt.plot(x_vals, cs_p_list_m11, color='green')
plt.plot(x_vals, cs_m_list_m11, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 11/Processed Data/cs-1c-mouse11.png')

plt.plot(x_vals_3, cs_p_list_m5, color='green')
plt.plot(x_vals_3, cs_m_list_m5, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 5/Processed Data/cs-1c-mouse5.png')

plt.plot(x_vals_2, cs_p_list_m3, color='green')
plt.plot(x_vals_2, cs_m_list_m3, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 3/Processed Data/cs-1c-mouse3.png')

plt.plot(x_vals_2, cs_p_list_m4, color='green')
plt.plot(x_vals_2, cs_m_list_m4, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/mouse 4/Processed Data/cs-1c-mouse4.png')

# For 3 Add color black for control, orange for halo
plt.plot(x_vals, cs_p_list_m1, color= '')
plt.plot(x_vals, cs_p_list_m2, color= '')
plt.plot(x_vals, cs_p_list_m6, color= '')
plt.plot(x_vals, cs_p_list_m7, color= '')
plt.plot(x_vals, cs_p_list_m8, color= '')
plt.plot(x_vals, cs_p_list_m9, color= '')
plt.plot(x_vals, cs_p_list_m11, color= '')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/allmice-csplus-1c.png')

plt.plot(x_vals, cs_m_list_m1, color= '')
plt.plot(x_vals, cs_m_list_m2, color= '')
plt.plot(x_vals, cs_m_list_m6, color= '')
plt.plot(x_vals, cs_m_list_m7, color= '')
plt.plot(x_vals, cs_m_list_m8, color= '')
plt.plot(x_vals, cs_m_list_m9, color= '')
plt.plot(x_vals, cs_m_list_m11, color= '')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/allmice-csminus-1c.png')

# Fig 4 - need to change according to control and halo (like make a cs_p_list_yfp, cs_p_list_halo ...)
cs_p_list_all = np.add(cs_p_list_m1, cs_p_list_m2, cs_p_list_m6, cs_p_list_m7, cs_p_list_m8, cs_p_list_m9, cs_p_list_m11)
cs_p_list_all = [i / 7 for i in cs_p_list_all]
cs_m_list_all = np.add(cs_m_list_m1, cs_m_list_m2, cs_m_list_m6, cs_m_list_m7, cs_m_list_m8, cs_m_list_m9, cs_m_list_m11)
cs_m_list_all = [i / 7 for i in cs_m_list_all]

plt.plot(x_vals, cs_p_list_all, color='green')
plt.plot(x_vals, cs_m_list_all, color='red')
plt.savefig('C:/Users/crist/Dropbox/11-2021_Discrimination/csall-1c-mouse4.png')
