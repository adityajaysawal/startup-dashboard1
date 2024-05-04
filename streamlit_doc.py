import streamlit as st
import pandas as pd
import  time
st.title('Startup Dashboard')
st.header('I am learning streamlit')
st.subheader('Aditya')
st.write('This is a normal text')
st.markdown("""
## My favourite movies
- Iron man
- spider man
""")
st.code("""
def foo(input):
    return foo**2
x=foo(2)    
""")

st.latex('x^2 + y^2 + 2 = 0')
df = pd.DataFrame({
    'name':['Nitish','Ankit','Anupam'],
    'marks':[50,60,70],
    'package':[10,12,14]
})
#df1=pd.read_csv('C:\Users\HP\OneDrive\Desktop\Sales Data.csv',x=0)
st.dataframe(df)
#st.dataframe(df1.head(5))

st.metric('Revenue','RS 3L','-3')

st.json({
    'name': ['Nitish', 'Ankit', 'Anupam'],
    'marks': [50, 60, 70],
    'package': [10, 12, 14]
})

st.image('Screenshot (42).png')
# st.video()
# st.audio()
# Creating layouts
st.sidebar.title('Sidebar Tittle')
col1, col2, col3 =st.columns(3)
with col2:
    st.image('Screenshot (42).png')
with col1:
    st.image('Screenshot (42).png')
with col3:
    st.image('Screenshot (42).png')
# Showing Status
# Error and Success Message
st.error('login failed')
st.success('login succesful')

# Progress Bar
bar= st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

# Taking user input
email = st.text_input('Enter Email')
number =st.number_input('Enter Age')
st.date_input('Enter Registration date')

email=st.text_input('Enter email')
password=st.text_input('Enter password')
gender = st.selectbox('Select gender',['male','female','others'])
# if the button is clicked
btn = st.button('Do login')
if btn:
    if email=='aditya@gmail.com' and password=='1234':
        st.success('login successful')
        st.balloons()
        st.write(gender)
    else:
        st.error('login failed')
# file uploader
file=st.file_uploader('Upload a csv flie')
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.head())
    st.dataframe(df.describe())