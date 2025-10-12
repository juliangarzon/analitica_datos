"""
Complete Interactive Dashboard
Class 8: Plotly + Streamlit - Part 5

What you'll learn:
- Building a full-featured dashboard
- Using tabs for organization
- Multiple charts with coordinated filtering

HOW TO RUN:
streamlit run dashboard_complete.py
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ========================================
# CONFIGURATION
# ========================================
st.set_page_config(
    page_title='Analytics Dashboard',
    layout='wide',
    page_icon='📊'
)

# ========================================
# LOAD DATA
# ========================================
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

df = load_data()

# ========================================
# HEADER
# ========================================
st.title('📊 Global Development Analytics Dashboard')
st.markdown('**Human Development Analysis by Country and Continent**')
st.markdown('---')

# ========================================
# SIDEBAR
# ========================================
st.sidebar.title('🎛️ Controls')
st.sidebar.markdown('---')

year = st.sidebar.slider(
    '📅 Year',
    1952, 2007, 2007, 5
)

continents = st.sidebar.multiselect(
    '🌍 Continents',
    df['continent'].unique(),
    default=df['continent'].unique()
)

show_data = st.sidebar.checkbox('📋 Show raw data')

st.sidebar.markdown('---')
st.sidebar.markdown('**Built with:**')
st.sidebar.markdown('🐍 Python + Plotly + Streamlit')

# ========================================
# FILTER DATA
# ========================================
df_filtered = df[(df['year']==year) & (df['continent'].isin(continents))]

# ========================================
# TOP METRICS
# ========================================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    '🌍 Countries',
    len(df_filtered),
    help='Total countries'
)

col2.metric(
    '👥 Population',
    f"{df_filtered['pop'].sum()/1e9:.2f}B"
)

col3.metric(
    '💰 Avg GDP',
    f"${df_filtered['gdpPercap'].mean():,.0f}"
)

col4.metric(
    '❤️ Avg Life Expectancy',
    f"{df_filtered['lifeExp'].mean():.1f} years"
)

st.markdown('---')

# ========================================
# MAIN TABS
# ========================================
tab1, tab2, tab3 = st.tabs(['📈 General Analysis', '🗺️ By Continent', '📊 Distributions'])

# ========================================
# TAB 1: GENERAL ANALYSIS
# ========================================
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('GDP vs Life Expectancy')
        fig1 = px.scatter(
            df_filtered,
            x='gdpPercap',
            y='lifeExp',
            size='pop',
            color='continent',
            hover_name='country',
            log_x=True
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader('Average Evolution Over Time')
        df_evolution = df[df['continent'].isin(continents)].groupby('year').agg({
            'lifeExp': 'mean',
            'gdpPercap': 'mean'
        }).reset_index()

        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=df_evolution['year'],
            y=df_evolution['lifeExp'],
            mode='lines+markers',
            name='Life Expectancy',
            line=dict(color='green', width=3)
        ))
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)

# ========================================
# TAB 2: BY CONTINENT
# ========================================
with tab2:
    continent_select = st.selectbox(
        'Select Continent',
        continents
    )

    df_continent = df_filtered[df_filtered['continent']==continent_select].nlargest(10, 'pop')

    fig3 = px.bar(
        df_continent,
        x='country',
        y='pop',
        title=f'Top 10 Countries by Population - {continent_select}',
        color='pop',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig3, use_container_width=True)

# ========================================
# TAB 3: DISTRIBUTIONS
# ========================================
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Life Expectancy Distribution')
        fig4 = px.histogram(
            df_filtered,
            x='lifeExp',
            nbins=20,
            color='continent'
        )
        st.plotly_chart(fig4, use_container_width=True)

    with col2:
        st.subheader('GDP Distribution by Continent')
        fig5 = px.box(
            df_filtered,
            x='continent',
            y='gdpPercap',
            color='continent'
        )
        st.plotly_chart(fig5, use_container_width=True)

# ========================================
# RAW DATA
# ========================================
if show_data:
    st.markdown('---')
    st.subheader('📋 Raw Data')
    st.dataframe(df_filtered, use_container_width=True)

    # Download button
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        '⬇️ Download CSV',
        csv,
        'filtered_data.csv',
        'text/csv'
    )
