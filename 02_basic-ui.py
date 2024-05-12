import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

button=st.button('click button')

if button:
    st.write(':blue[버튼]이 눌렸습니다 :sparkles:')


#file donwload
dataframe=pd.DataFrame(
    {'first column': [1,2,3,4],
     'second column':[10,20,30,40]}
)

st.download_button(
    label='csv로다운로드',
    data=dataframe.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)

#check box
agree=st.checkbox('동의하십니까?')
if agree:
    st.write('동의해줘서 감사')

#radio button
mbti=st.radio(
    '당신의 mbti는 무엇입니까',
    ('ISTJ','ENFP','선택지없음')
)

if mbti=='ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti=='ENFP':
   st.write('당신은 :green[활동가] 이시네요') 
else:
    st.write('당신에 대해 :red[알고싶어요]:grey_exclamation:')


#drop down
mbti=st.selectbox(
    '당신의 mbti는 무엇입니까',
    ('ISTJ','ENFP','선택지없음')
)

if mbti=='ISTJ':
    st.write('당신은 :blue[현실주의자] 이시네요')
elif mbti=='ENFP':
   st.write('당신은 :green[활동가] 이시네요') 
else:
    st.write('당신에 대해 :red[알고싶어요]:grey_exclamation:')





