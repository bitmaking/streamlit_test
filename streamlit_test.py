import streamlit as st
#st.image("image.jpg", caption="this is my image", width=600)
#st.audio('audio.mp3')
#st.video('video.mp4')

def change():
    print(st.session_state.checker)
state=st.checkbox("checkbox", value=True,on_change=change, key='checker')

if state:
    st.write('hi')
else:
    pass


radio_btn=st.radio("in which country do you live?", options=('us','uk','canada'))
print(radio_btn)

def btn_click():
    print('buttion clicked')
btn=st.button('click me!', on_click=btn_click)


select=st.selectbox('what is your favorite car', options=("Audi","BMW","Ferrari"))

print(select)


multi_select=st.multiselect('what is your favorite tech grand',options=('ms','apple','samsung','oracle'))
st.write(multi_select)


#######9

st.markdown("---")
st.write('## image upload')
image=st.file_uploader('please upload an image', type=["png",'jpg'])

if image is not None:
    st.image(image)

st.markdown('---')
images=st.file_uploader('please upload multiple image', type=["png",'jpg'], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)


#####10
st.markdown('---')
st.write('## slider')

val=st.slider('this is a slider', min_value=150, value=70)
print(val)

st.write('## text input')
val2=st.text_input('Enter your Course title',max_chars=60)
print(val2)

val3=st.text_area('course description')
print(val3)

val4=st.date_input('enter your registereration date')
print(val4)

val5=st.time_input('set timer')
print(val5)

#11

st.write('## timer2')
import time as ts
from datetime import time  

def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60*int(s)*int(mm)/1000
    return t_s

val=st.time_input('set timer',value=time(0,0,0))
if str(val) == '00:00:00':
    st.write('please sent timer')
else: 
    sec= converter(str(val))
    bar=st.progress(0)
    per=sec/100
    for i in range(100):
        bar.progress(i+1)
        ts.sleep(per)

#12
st.write('## #12')
st.markdown('<h1>user registration</h1>', unsafe_allow_html=True)
form=st.form('form 1')
form.text_input('first name')
form.form_submit_button('submit')

with st.form('form 2', clear_on_submit=True):
    col1,col2 = st.columns(2)
    f_name=col1.text_input('first name')
    l_name=col2.text_input('last name')
    st.text_input('email address')
    st.text_input('password')
    st.text_input('confirm password')
    day,month,year=st.columns(3)
    day.text_input('Day')
    month.text_input('Month')
    year.text_input('Year')
    s_state=st.form_submit_button('submit')
    if s_state:
        if f_name=="" and l_name=="":
            st.warning('please fill above fields')
        else:
            st.success('submitted successfully')

#14
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])
opt=st.sidebar.radio('select my graph', options=('line','bar','h-bar'))

if opt=='line':
    st.markdown('line chart')
    fig=plt.figure()
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    st.write(fig)
elif opt=='bar':
    st.markdown('bar chart')
    fig=plt.figure()
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    st.markdown('h-bar chart')
    fig=plt.figure()
    plt.barh(bar_x*10,bar_x)
    st.write(fig)



