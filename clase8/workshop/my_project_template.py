"""
Project Dashboard Template
Class 8: Plotly + Streamlit - Part 6

YOUR HOMEWORK: Adapt this template for YOUR project data

INSTRUCTIONS:
1. Replace 'your_data.csv' with your actual data file
2. Update column names throughout to match your data
3. Add appropriate filters for your dataset
4. Create 5+ relevant charts for your data
5. Add 4 meaningful metrics/KPIs
6. Organize in logical tabs

HOW TO RUN:
streamlit run my_project_template.py
"""

import streamlit as st
import plotly.express as px
import pandas as pd

# ========================================
# CONFIGURATION
# ========================================
st.set_page_config(
    page_title='My Project Dashboard',
    layout='wide',
    page_icon='📊'
)

# ========================================
# LOAD YOUR DATA
# ========================================
@st.cache_data
def load_data():
    # TODO: CHANGE THIS TO YOUR DATA FILE
    # return pd.read_csv('your_data.csv')

    # For now, using example data
    return pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

df = load_data()

# ========================================
# SHOW DATA PREVIEW (for development)
# ========================================
st.title('🎯 My Project Dashboard - [YOUR PROJECT NAME]')
st.markdown('---')

with st.expander('📊 Data Preview (for development - remove later)'):
    st.dataframe(df.head())
    st.write('**Available columns:**', df.columns.tolist())
    st.write('**Dataset shape:**', df.shape)
    st.write('**Data types:**')
    st.write(df.dtypes)

st.markdown('---')

# ========================================
# SIDEBAR - FILTERS
# ========================================
st.sidebar.header('🎛️ Filters')

# TODO: CUSTOMIZE THESE FILTERS FOR YOUR DATA

# Example Filter 1: Categorical column
if 'continent' in df.columns:  # Replace 'continent' with your categorical column
    selected_categories = st.sidebar.multiselect(
        'Select Category',
        df['continent'].unique(),
        default=df['continent'].unique()
    )
    df = df[df['continent'].isin(selected_categories)]

# Example Filter 2: Numeric range
if 'year' in df.columns:  # Replace 'year' with your numeric column
    min_val = int(df['year'].min())
    max_val = int(df['year'].max())

    selected_range = st.sidebar.slider(
        'Numeric Range',
        min_val,
        max_val,
        (min_val, max_val)
    )
    df = df[(df['year'] >= selected_range[0]) & (df['year'] <= selected_range[1])]

# ========================================
# METRICS / KPIs
# ========================================
st.subheader('📊 Key Performance Indicators')

col1, col2, col3, col4 = st.columns(4)

# TODO: REPLACE THESE WITH YOUR ACTUAL METRICS
col1.metric(
    'Metric 1',
    f"{len(df):,}",
    help='Description of metric 1'
)

col2.metric(
    'Metric 2',
    f"{df['pop'].sum()/1e9:.2f}B" if 'pop' in df.columns else 'N/A',
    help='Description of metric 2'
)

col3.metric(
    'Metric 3',
    f"{df['lifeExp'].mean():.1f}" if 'lifeExp' in df.columns else 'N/A',
    help='Description of metric 3'
)

col4.metric(
    'Metric 4',
    'Value',
    delta=10,
    help='Description of metric 4'
)

st.markdown('---')

# ========================================
# MAIN CHARTS - ORGANIZED IN TABS
# ========================================
tab1, tab2, tab3, tab4 = st.tabs(['📈 Analysis 1', '📊 Analysis 2', '🔍 Analysis 3', '📋 Raw Data'])

# ========================================
# TAB 1: First Analysis
# ========================================
with tab1:
    st.subheader('Chart 1: [Title]')

    # TODO: ADD YOUR FIRST CHART HERE
    # Example:
    if 'gdpPercap' in df.columns and 'lifeExp' in df.columns:
        fig1 = px.scatter(
            df,
            x='gdpPercap',
            y='lifeExp',
            color='continent' if 'continent' in df.columns else None,
            title='Example Scatter Plot'
        )
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info('👆 Replace this with your first chart')
        st.code("""
# Example:
fig = px.bar(df, x='category_column', y='value_column')
st.plotly_chart(fig, use_container_width=True)
        """, language='python')

# ========================================
# TAB 2: Second Analysis
# ========================================
with tab2:
    st.subheader('Chart 2: [Title]')

    col1, col2 = st.columns(2)

    with col1:
        st.info('👆 Add your second chart here')
        # TODO: Add chart

    with col2:
        st.info('👆 Add your third chart here')
        # TODO: Add chart

# ========================================
# TAB 3: Third Analysis
# ========================================
with tab3:
    st.subheader('Chart 3: [Title]')

    st.info('👆 Add your fourth and fifth charts here')
    # TODO: Add more charts

# ========================================
# TAB 4: Raw Data
# ========================================
with tab4:
    st.subheader('📋 Filtered Data')
    st.dataframe(df, use_container_width=True)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        '⬇️ Download Filtered Data',
        csv,
        'filtered_data.csv',
        'text/csv'
    )

# ========================================
# FOOTER
# ========================================
st.markdown('---')
st.markdown("""
**TODO Checklist for your project:**
- [ ] Load your actual data file
- [ ] Update all column names
- [ ] Create 5+ relevant charts
- [ ] Add 4 meaningful KPIs
- [ ] Implement 3+ filters
- [ ] Organize tabs logically
- [ ] Add descriptive titles
- [ ] Test all functionality
- [ ] Remove development helpers
- [ ] Add professional styling
""")
