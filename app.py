import streamlit as st
import pandas as pd
from servicenow import get_validations
from notifier import send_email
from pdf_report import create_report

st.set_page_config(page_title='Validation Copilot',layout='wide')
st.title('ServiceNow Validation Copilot')

menu=st.sidebar.selectbox('Menu',['Dashboard','Validations','Reminders','Reports','AI Assistant'])

data=get_validations()
df=pd.DataFrame(data) if data else pd.DataFrame()

if menu=='Dashboard':
    c1,c2,c3=st.columns(3)
    c1.metric('Total',len(df))
    c2.metric('Open',len(df))
    c3.metric('Critical',0)
    st.dataframe(df)

elif menu=='Validations':
    st.dataframe(df)

elif menu=='Reminders':
    email=st.text_input('Email/DL')
    if st.button('Send Reminder'):
        send_email(email,'Validation Reminder','Please review pending validations')
        st.success('Reminder sent')

elif menu=='Reports':
    if st.button('Generate PDF'):
        create_report('validation_report.pdf','Validation Summary Report')
        st.success('PDF generated')

else:
    q=st.text_input('Ask about validations')
    if q:
        st.write('AI integration placeholder: connect Azure OpenAI here')
