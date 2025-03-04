import streamlit as st
from streamlit_cookies_controller import CookieController
import numpy as np
import pandas as pd

# set initial page configuration
st.set_page_config(page_title='OBMedia Analysis Streamlit', # page title in browser tab
                   page_icon=':bar_chart:', # icon in browser tab
                   layout='wide', # page layout setting
                   initial_sidebar_state='collapsed', # collapse left sidebar by default
                   menu_items={'Report a bug': 'https://admarket.slack.com/archives/C04434ZKMQB'})

# create cookie controller
cookie_controller = CookieController()

# define layout elements
header = st.container(height=100, border=True)
sidebar, content = st.columns([0.2, 0.8], border=False)
footer = st.container(height=150, border=True)

# header
with header:
    st.markdown("""
                #### We can put a header up here!
                
                Appearance leaves something to be desired, but we can use our own CSS.
                """)

# test the built-in sidebar (uses same sidebar as page nav)
with st.sidebar:
    st.write('Built-in sidebar test')

# test using columns to make my own sidebar

# define the sidebar content
with sidebar:
    with st.form('Sidebar form'):
        st.write('Hello, sidebar!')
        st.write('This is a form. A reload is only triggered when the form is submitted.')
        
        # checkboxes
        st.checkbox(label='Checkbox 1')
        st.checkbox(label='Checkbox 2')
        st.checkbox(label='Checkbox 3')
        
        # pills
        st.pills('Pill selection',
                 options=['Option 1', 'Option 2', 'Option 3', 'Option 4'])
        
        # multiselects
        st.multiselect(label='Multiselect',
                       options=['Option 1', 'Option 2', 'Option 3'])
        
        # slider
        st.slider(label='Slider',
                  min_value=0,
                  max_value=10,
                  step=1)
        
        # button to submit sidebar form
        st.form_submit_button('Apply Selection')
    with st.container(border=True):
        st.write('The sidebar can have elements outside of the form.')
        st.write('Interacting with these elements immediately triggers a reload.')
        st.button('Button 1')
        st.button('Button 2')

# page content
with content:
    st.markdown("""
                # Hello, world!
                Content goes here.
                """)
                
    # test cookie controller
    st.write('Setting a cookie')
    cookie_controller.set('cookie_name', 'testing')
    st.write(st.session_state)
    # all cookies
    st.write('All cookies:')
    cookies = cookie_controller.getAll()
    st.write(cookies)
    # the cookie I set
    st.write('The content of the cookie we just set, fetched by name:')
    cookie = cookie_controller.get('cookie_name')
    st.write(cookie)

    # show some sample content        
    st.markdown('## Example content: table')    
    st.dataframe(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
    st.markdown("""
                ## More content
                Here are a couple of other dataframes, which are used to illustrate the behavior of the
                footer and sidebar when more content is shown.
                """)
    st.dataframe(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
    st.dataframe(pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD')))
    
# footer
with footer:
    st.markdown("""
                ##### We can put a footer here!
                
                Sure is ugly. But, look: input fields!
                """)
    
    footer_columns = st.columns(8)
    for i, col in enumerate(footer_columns):
        with footer_columns[i]:
            st.checkbox(label=f'Checkbox {i+1}')
