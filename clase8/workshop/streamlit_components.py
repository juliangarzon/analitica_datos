"""
Streamlit Components Reference
Class 8: Plotly + Streamlit - Part 4

What you'll learn:
- All essential Streamlit components
- How to use different widgets and layouts

HOW TO RUN:
streamlit run streamlit_components.py
"""

import streamlit as st
import pandas as pd

st.title('📚 Streamlit Components Reference')

# ========================================
# 1. TEXT AND TITLES
# ========================================
st.header('1. Text and Titles')
st.subheader('This is a subheader')
st.text('Normal text')
st.markdown('**Bold** and *italic* and `code`')
st.code('print("Hello World")', language='python')

st.markdown('---')

# ========================================
# 2. INPUT WIDGETS IN SIDEBAR
# ========================================
st.header('2. Input Widgets')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Sidebar Inputs')

    # Select box (choose one)
    option = st.sidebar.selectbox(
        'Select Box (choose 1)',
        ['Option A', 'Option B', 'Option C']
    )
    st.write(f'Selected: {option}')

    # Multi-select (choose many)
    multi = st.sidebar.multiselect(
        'Multi-Select (choose many)',
        ['A', 'B', 'C', 'D'],
        default=['A']
    )
    st.write(f'Selected: {multi}')

    # Slider
    number = st.sidebar.slider(
        'Slider',
        min_value=0,
        max_value=100,
        value=50
    )
    st.write(f'Value: {number}')

with col2:
    st.subheader('More Inputs')

    # Radio buttons
    radio = st.sidebar.radio(
        'Radio Buttons',
        ['Option 1', 'Option 2', 'Option 3']
    )
    st.write(f'Radio: {radio}')

    # Checkbox
    check = st.sidebar.checkbox('Checkbox')
    st.write(f'Checked: {check}')

    # Text input
    text = st.sidebar.text_input('Text Input', 'Type here')
    st.write(f'Text: {text}')

st.markdown('---')

# ========================================
# 3. DISPLAYING DATA
# ========================================
st.header('3. Displaying Data')

df = pd.DataFrame({
    'Column A': [1, 2, 3, 4],
    'Column B': [10, 20, 30, 40]
})

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('DataFrame')
    st.dataframe(df)

with col2:
    st.subheader('Table')
    st.table(df)

with col3:
    st.subheader('Metric')
    st.metric('Total', 100, delta=10)

st.markdown('---')

# ========================================
# 4. LAYOUTS
# ========================================
st.header('4. Layouts')

# Columns
st.subheader('Columns')
col1, col2, col3 = st.columns(3)
col1.write('Column 1')
col2.write('Column 2')
col3.write('Column 3')

# Tabs
st.subheader('Tabs')
tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])
with tab1:
    st.write('Content in Tab 1')
with tab2:
    st.write('Content in Tab 2')
with tab3:
    st.write('Content in Tab 3')

# Expander
st.subheader('Expander')
with st.expander('Click to expand'):
    st.write('Hidden content revealed on click')

# Container
st.subheader('Container')
container = st.container()
container.write('This is in a container')

st.markdown('---')

# ========================================
# 5. STATUS MESSAGES
# ========================================
st.header('5. Status Messages')

col1, col2 = st.columns(2)

with col1:
    st.info('ℹ️ Information message')
    st.success('✅ Success message')

with col2:
    st.warning('⚠️ Warning message')
    st.error('❌ Error message')

st.markdown('---')

# ========================================
# 6. PROGRESS & SPINNER
# ========================================
st.header('6. Progress & Spinner')

if st.button('Show progress'):
    import time
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    st.success('Completed!')

st.markdown('---')
st.info('💡 Explore the sidebar to see all the input widgets in action!')
