import streamlit as st
import pandas as pd
import plotly.express as px
import plost

st.set_page_config(layout="wide")
df = pd.read_csv('D:\diabetes1.csv')

def displaytable():
    st.title('Data Table')
    st.write(df)

def scatter_plot():
    st.title('Scatter Plot')
    col1, col2 = st.columns(2)
    
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    plot = px.scatter(df, x="Age", y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)


def Bar_Graph():  
    st.title('Bar Graph') 
    col1, col2 = st.columns(2)
    
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)
    
    plost.hist(
    df, 
    x='Age',
    y=y_axis_val,
    aggregate='mean'
)


# #Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Data Table','Scatter Plot','Bar_Graph'])


# Navigation options

if options == 'Data Table':
    displaytable()
elif options == 'Scatter Plot':
    scatter_plot()
elif options == 'Bar_Graph':
    Bar_Graph()

