from typing import List
import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
import matplotlib.pyplot as plt

DATA_URL = ("vgsales.csv")

st.title("Dashboard for Video Game Data")
st.sidebar.title("Control Panel")
st.markdown("This application is a Streamlit dashboard used "
            "to understand video games sales data")
st.sidebar.markdown("This application is a Streamlit dashboard used "
            "to understand video games sales data")

@st.cache(persist=True)

def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()
data = data.fillna(method='ffill')

st.sidebar.subheader("Game Sales Data")

name = st.sidebar.text_input('Enter Name')
ng = data[data['Name']==str(name)]

ptfm = ng.Platform.values
ptms = st.sidebar.selectbox('Select Platform',ptfm)

vg = data[(data['Name']==name) & (data['Platform']==str(ptms))]

roi = st.sidebar.selectbox('Select Region',['North America','Europe','Japan','Other','Global'])
reg_dict = {'North America':'NA_Sales','Europe':'EU_Sales','Japan':'JP_Sales','Other':'Other_Sales','Global':'Global_Sales'}
region = reg_dict[roi]

pt = vg[region].values
sales=vg.iloc[:,5:]
glob = vg.iloc[:,9:]


# plot_type =  st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'],key='2')
if not st.sidebar.checkbox("Close", True, key='2'):
    data_choice=st.sidebar.selectbox("Data", ['Show Raw Data','Show Overall Data'])
    if data_choice == 'Show Raw Data':
        st.subheader('The Total Sales of {} (in Millions) in {} Region are'.format(name,roi))
        st.write(pt)
    else:
        st.subheader('Overall Data for selected Game')
        st.write(vg)
#     if plot_type == 'Bar Plot':
#         st.write('True')
#         st.subheader("Total No of Sales")
#         fig = px.bar(vg,x=100,y=100,height=500)
#         st.plotly_chart(fig)
#     else:
#         fig = px.pie(vg, values=glob, names='Global_Sales')
#         st.plotly_chart(fig)

st.sidebar.subheader('Games by Publisher')
publishers = data.Publisher.unique()
pub = st.sidebar.selectbox('Select Publisher',publishers)
ptmf2 = data.Platform.unique()
ptms2 = st.sidebar.selectbox('Select Platform',ptmf2)

glist= data[(data['Publisher']==pub) & (data['Platform']==ptms2)]
vg2=glist.iloc[:,1:2]
if st.sidebar.button("Search",key=1):
    st.write(vg2)

st.sidebar.subheader('Games by Genre')
genres = data.Genre.unique()
gen = st.sidebar.selectbox('Select Genre',genres)
ptmf3 = data.Platform.unique()
ptms3 = st.sidebar.selectbox('Select Platform',ptmf3,key='2')

glist2= data[(data['Genre']==gen) & (data['Platform']==ptms3)]
vg3=glist2.iloc[:,1:2]
if st.sidebar.button("Search",key=2):
    st.write(vg3)

st.sidebar.subheader("Games by Year of Release")
year = st.sidebar.slider("Year", 1980, 2017)
ptmf4 = data.Platform.unique()
ptms4 = st.sidebar.selectbox('Select Platform',ptmf4,key='3')

glist3 = data[(data['Year']==year) & (data['Platform']==ptms4)]
vg4 = glist3.iloc[:,1:6]
if st.sidebar.button("Find"):
    st.write(vg4)

st.sidebar.subheader("Top Selling Games of All Time")
top = st.sidebar.number_input("Enter Number of Games")
top = int(top)

glist4 = data[data['Rank']<=top]
vg5 = glist4.iloc[:,0:6]

if st.sidebar.button("Get Results"):
    st.write(vg5)

st.sidebar.subheader("Get Rank of a Specific Game")
rank = st.sidebar.text_input('Enter Name',key='2')

glist5 = data[data['Name']==rank]
vg6 = glist5.iloc[:,0:3]

if st.sidebar.button("Get Rank"):
    st.write(vg6)