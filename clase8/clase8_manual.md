# 📊 CLASS 8: PLOTLY + STREAMLIT - COMPLETE MANUAL
## From Static Charts to Interactive Web Dashboards in 4 Hours

**Universidad Cooperativa de Colombia - Data Analytics - 7th Semester**

---

## 🎯 TODAY'S OBJECTIVE
By the end of this class, you will have a **fully functional interactive web dashboard** built with your project data.

---

## 📋 TABLE OF CONTENTS

1. [Installation & Setup](#1-installation--setup)
2. [PART 1: Plotly - The 6 Essential Charts](#2-part-1-plotly-quick-start)
3. [PART 2: Plotly - Customization](#3-part-2-customization)
4. [PART 3: Plotly - Advanced Interactivity](#4-part-3-advanced-interactivity)
5. [PART 4: Streamlit - First App](#5-part-4-streamlit-first-app)
6. [PART 5: Streamlit - Complete Dashboard](#6-part-5-complete-dashboard)
7. [PART 6: Apply to Your Project](#7-part-6-your-project)

---

# 1. INSTALLATION & SETUP

## 1.1 Install Required Libraries

**What we're doing:** Installing the three main Python libraries we'll use today.

- **Plotly:** For creating interactive visualizations
- **Pandas:** For data manipulation
- **Streamlit:** For building web dashboards

**IN YOUR TERMINAL (everyone together):**

```bash
pip install plotly pandas streamlit
```

**⏱️ Expected time:** 1-2 minutes (depending on your internet connection)

**💡 Tip:** If you're using a virtual environment, make sure it's activated first!

---

## 1.2 Verify Installation

**What we're doing:** Testing that all libraries were installed correctly before we proceed.

**Step 1:** Create a new file called `test_installation.py`

**Step 2:** Copy and paste this code:

```python
import plotly.express as px
import pandas as pd
import streamlit as st

print("✅ All libraries installed successfully!")
print(f"Plotly version: {px.__version__}")
print(f"Pandas version: {pd.__version__}")
print(f"Streamlit version: {st.__version__}")
```

**Step 3:** Run the file in your terminal:

```bash
python test_installation.py
```

**Expected output:**
```
✅ All libraries installed successfully!
Plotly version: 5.x.x
Pandas version: 2.x.x
Streamlit version: 1.x.x
```

**⚠️ If you get an error:**
- Make sure you're in the correct directory
- Check that pip installation completed without errors
- Try `pip3` instead of `pip` on macOS/Linux
- Raise your hand for help!

---

# 2. PART 1: PLOTLY QUICK START

## 2.1 Your First Interactive Chart (5 minutes)

**What we're doing:** Creating your first interactive Plotly chart with just 3 lines of code! This will show you how easy it is to create professional visualizations.

**Why this matters:** Traditional plotting libraries like Matplotlib create static images. Plotly creates interactive HTML charts that you can zoom, pan, and hover over - perfect for web dashboards.

**Step 1:** Create a new file called `01_first_chart.py`

**Step 2:** Copy this code:

```python
import plotly.express as px
import pandas as pd

# Load sample data from online dataset
# This is the famous Gapminder dataset with country development indicators
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# YOUR FIRST INTERACTIVE CHART - Just 3 lines!
fig = px.scatter(
    df.query("year==2007"),      # Filter: only year 2007
    x='gdpPercap',                # X-axis: GDP per capita
    y='lifeExp',                  # Y-axis: Life expectancy
    size='pop',                   # Bubble size: population
    color='continent',            # Color: by continent
    hover_name='country',         # Show country name on hover
    log_x=True,                   # Logarithmic scale for X-axis
    size_max=60,                  # Maximum bubble size
    title='GDP vs Life Expectancy (2007)'
)

# Display the interactive chart
fig.show()
```

**Step 3:** Run the code:

```bash
python 01_first_chart.py
```

**What you should see:**
- An interactive chart opens in your browser
- You can hover over bubbles to see country details
- Try zooming in/out with your mouse
- Click and drag to pan around
- Double-click to reset the view

**🎯 HANDS-ON ACTIVITY (3 minutes):**
1. Run the code
2. Hover over different bubbles
3. Try the zoom and pan features
4. Notice how professional it looks with minimal code!

**📊 What's happening?**
- `px.scatter()` creates the scatter plot
- Each parameter adds a feature (size, color, hover text)
- `fig.show()` opens it in your browser
- All interactivity comes built-in!

---

## 2.2 The 6 Essential Charts (30 minutes)

**What we're doing:** Learning the 6 chart types that cover 90% of data visualization needs. Each chart type serves a specific purpose.

**Teaching approach:** I'll demonstrate each chart, explain when to use it, then you'll replicate it immediately.

**Step 1:** Create a new file called `02_six_charts.py`

**Step 2:** We'll add charts one by one (follow along!):

```python
import plotly.express as px
import pandas as pd

# Load the data once
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# ========================================
# CHART 1: SCATTER - Relationships between variables
# ========================================
# Use when: You want to see correlation between 2 numeric variables
# Example: Does GDP correlate with life expectancy?

fig1 = px.scatter(
    df.query("year==2007"),    # Filter data for year 2007
    x='gdpPercap',              # X-axis: GDP per capita
    y='lifeExp',                # Y-axis: Life expectancy
    color='continent',          # Color points by continent
    size='pop',                 # Size points by population
    hover_name='country',       # Show country name on hover
    log_x=True,                 # Use log scale for better visualization
    title='GDP vs Life Expectancy (2007)'
)
fig1.show()

# ========================================
# CHART 2: LINE - Time series & trends
# ========================================
# Use when: Showing how something changes over time
# Example: How has Colombia's life expectancy evolved?

colombia = df[df['country']=='Colombia']  # Filter for Colombia only
fig2 = px.line(
    colombia,
    x='year',                   # X-axis: time
    y='lifeExp',                # Y-axis: life expectancy
    markers=True,               # Show points on the line
    title='Life Expectancy Evolution - Colombia'
)
fig2.show()

# ========================================
# CHART 3: BAR - Comparing categories
# ========================================
# Use when: Comparing values across different categories
# Example: Which countries have the largest populations?

top10 = df.query("year==2007").nlargest(10, 'pop')  # Get top 10 countries
fig3 = px.bar(
    top10,
    x='country',                # X-axis: country names
    y='pop',                    # Y-axis: population
    color='continent',          # Color bars by continent
    title='Top 10 Countries by Population (2007)'
)
fig3.show()

# ========================================
# CHART 4: BOX PLOT - Distribution comparison
# ========================================
# Use when: Comparing distributions across groups
# Example: How does life expectancy vary within each continent?

fig4 = px.box(
    df.query("year==2007"),
    x='continent',              # Groups on X-axis
    y='lifeExp',                # Distribution of this variable
    color='continent',          # Color by group
    title='Life Expectancy Distribution by Continent (2007)'
)
fig4.show()

# ========================================
# CHART 5: HISTOGRAM - Single variable distribution
# ========================================
# Use when: Understanding the distribution of one numeric variable
# Example: What's the distribution of life expectancy globally?

fig5 = px.histogram(
    df.query("year==2007"),
    x='lifeExp',                # Variable to analyze
    nbins=20,                   # Number of bins (bars)
    title='Global Life Expectancy Distribution (2007)'
)
fig5.show()

# ========================================
# CHART 6: TREEMAP - Hierarchical proportions
# ========================================
# Use when: Showing hierarchical data and proportions
# Example: How is world population distributed across continents and countries?

fig6 = px.treemap(
    df.query("year==2007"),
    path=[px.Constant("world"), 'continent', 'country'],  # Hierarchy levels
    values='pop',               # Size of rectangles
    title='World Population Distribution (2007)'
)
fig6.show()
```

**🎯 HANDS-ON ACTIVITY (20 minutes):**

**For each chart above:**
1. I demonstrate and explain
2. You copy and run the code
3. Interact with the chart
4. Understand when to use it

**Step 3:** Run the complete file:

```bash
python 02_six_charts.py
```

---

## 2.3 Decision Tree: Which Chart Should I Use?

**Quick reference guide for choosing the right visualization:**

```
What do you want to show?

├─ Relationship between 2 numeric variables → SCATTER
│  Example: Income vs. Education Level
│
├─ Change over time → LINE
│  Example: Sales trends, stock prices
│
├─ Compare categories → BAR
│  Example: Sales by region, scores by team
│
├─ Distribution of 1 variable → HISTOGRAM
│  Example: Age distribution, grade distribution
│
├─ Compare distributions across groups → BOX
│  Example: Salary ranges by department
│
└─ Hierarchical proportions → TREEMAP
   Example: Budget breakdown, market share
```

**💡 Pro Tip:** When in doubt, start with a scatter plot for 2 variables or a bar chart for categories!

---

# 3. PART 2: CUSTOMIZATION

## 3.1 Basic Customization (20 minutes)

**What we're doing:** Transforming basic charts into professional-looking visualizations. The difference between a generic chart and a presentation-ready one is just a few lines of code!

**Why this matters:** Professional charts tell better stories and are more likely to be trusted by stakeholders.

**Step 1:** Create a new file called `03_customization.py`

**Step 2:** Let's compare BEFORE and AFTER

```python
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# ========================================
# BEFORE - Basic chart (minimal code)
# ========================================
fig_basic = px.scatter(
    df.query("year==2007"),
    x='gdpPercap',
    y='lifeExp'
)
fig_basic.show()

# ========================================
# AFTER - Professional chart (with customization)
# ========================================
fig_professional = px.scatter(
    df.query("year==2007"),
    x='gdpPercap',
    y='lifeExp',
    size='pop',                      # Add bubble sizes
    color='continent',               # Add color coding
    hover_name='country',            # Add hover labels
    title='Global Development Analysis',
    labels={                         # Rename axes for clarity
        'gdpPercap': 'GDP per Capita (USD)',
        'lifeExp': 'Life Expectancy (years)',
        'pop': 'Population',
        'continent': 'Continent'
    }
)

# ========================================
# ADVANCED CUSTOMIZATION with update_layout()
# ========================================
# This is where the magic happens!

fig_professional.update_layout(
    # Custom title formatting
    title={
        'text': 'Global Human Development Analysis',
        'x': 0.5,                    # Center the title
        'font': {'size': 20, 'color': '#2c3e50'}
    },

    # Visual theme
    # Options: 'plotly_dark', 'ggplot2', 'seaborn', 'plotly_white'
    template='plotly_white',

    # Chart dimensions
    height=600,
    width=900,

    # Background colors
    paper_bgcolor='#f8f9fa',         # Outer background
    plot_bgcolor='white',            # Chart area background

    # Legend configuration
    legend=dict(
        title='Continent',
        orientation='v',             # Vertical orientation
        x=1.02,                      # Position to the right
        y=1                          # Align to top
    ),

    # Hover interaction mode
    hovermode='closest'              # Snap to nearest point
)

# ========================================
# AXIS CUSTOMIZATION
# ========================================

# X-axis (GDP)
fig_professional.update_xaxes(
    showgrid=True,                   # Show gridlines
    gridwidth=1,
    gridcolor='lightgray',
    type='log'                       # Logarithmic scale for better spread
)

# Y-axis (Life Expectancy)
fig_professional.update_yaxes(
    showgrid=True,
    range=[30, 90]                   # Fixed range for consistency
)

fig_professional.show()
```

**Step 3:** Run and compare:

```bash
python 03_customization.py
```

**What changed?**
- ✅ Descriptive labels instead of variable names
- ✅ Clean, professional color scheme
- ✅ Centered, formatted title
- ✅ Optimized layout and spacing
- ✅ Better gridlines and background

---

## 3.2 Available Templates

**What are templates?** Pre-designed color schemes and styles that you can apply with one line of code.

```python
# See all available templates
import plotly.io as pio
print(pio.templates)

# Most commonly used templates:
templates = [
    'plotly',           # Default Plotly theme
    'plotly_white',     # White background (recommended for presentations)
    'plotly_dark',      # Dark mode (great for screens)
    'ggplot2',          # R/ggplot2 style (academic papers)
    'seaborn',          # Seaborn style (soft colors)
    'simple_white',     # Minimalist
    'presentation'      # Optimized for presentations
]

# To use a template, just add it to update_layout():
fig.update_layout(template='plotly_white')
```

**🎯 HANDS-ON ACTIVITY (10 minutes):**

Customize one of your previous charts:
1. Change the title to something descriptive
2. Try 3 different templates and pick your favorite
3. Adjust the color scheme
4. Add descriptive axis labels

**Challenge:** Make the ugliest chart look professional!

---

## 3.3 Subplots - Multiple Charts in One Figure (25 minutes)

**What we're doing:** Creating dashboard-style layouts with multiple charts in a single figure. This is perfect for comparing related visualizations.

**Why this matters:** Instead of showing 4 separate charts, you can create a professional multi-panel view.

**Step 1:** Create a new file called `04_subplots.py`

**Step 2:** Follow the code below:

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# Crear grid 2x2
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'PIB vs Esperanza de Vida', 
        'Evolución Colombia', 
        'Distribución Esperanza de Vida', 
        'Top 10 Países por Población'
    ),
    specs=[
        [{'type': 'scatter'}, {'type': 'scatter'}],
        [{'type': 'histogram'}, {'type': 'bar'}]
    ]
)

# Preparar datos
df_2007 = df[df['year']==2007]
df_col = df[df['country']=='Colombia']
top10 = df_2007.nlargest(10, 'pop')

# Subplot 1: Scatter (fila 1, columna 1)
fig.add_trace(
    go.Scatter(
        x=df_2007['gdpPercap'], 
        y=df_2007['lifeExp'],
        mode='markers', 
        name='2007',
        marker=dict(size=8, color='blue')
    ),
    row=1, col=1
)

# Subplot 2: Line (fila 1, columna 2)
fig.add_trace(
    go.Scatter(
        x=df_col['year'], 
        y=df_col['lifeExp'],
        mode='lines+markers', 
        name='Colombia',
        line=dict(color='green', width=3)
    ),
    row=1, col=2
)

# Subplot 3: Histogram (fila 2, columna 1)
fig.add_trace(
    go.Histogram(
        x=df_2007['lifeExp'], 
        name='Distribución',
        marker=dict(color='orange')
    ),
    row=2, col=1
)

# Subplot 4: Bar (fila 2, columna 2)
fig.add_trace(
    go.Bar(
        x=top10['country'], 
        y=top10['pop'], 
        name='Top 10',
        marker=dict(color='red')
    ),
    row=2, col=2
)

# Layout general
fig.update_layout(
    height=800,
    showlegend=False,
    title_text='Dashboard Multivista - Gapminder 2007'
)

fig.show()
```

**🎯 ACTIVIDAD (10 min):** 
Crea un subplot 1x2 (horizontal) con 2 gráficos de tu proyecto

---

# 4. PARTE 3: INTERACTIVIDAD AVANZADA

## 4.1 Hover Personalizado (15 minutos)

**Crear archivo: `05_hover_avanzado.py`**

```python
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
df_2007 = df[df['year']==2007]

# HOVER AVANZADO
fig = px.scatter(
    df_2007,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    hover_name='country',  # nombre principal al pasar mouse
    hover_data={
        'gdpPercap': ':,.0f',    # formato con comas, sin decimales
        'lifeExp': ':.1f',       # 1 decimal
        'pop': ':,.0f',          # formato con comas
        'continent': False       # no mostrar (ya está en color)
    },
    title='Hover Personalizado'
)

# Template de hover personalizado
fig.update_traces(
    hovertemplate='<b>%{hovertext}</b><br><br>' +
                  'PIB: $%{x:,.0f}<br>' +
                  'Esperanza Vida: %{y:.1f} años<br>' +
                  'Población: %{marker.size:,.0f}<br>' +
                  '<extra></extra>'  # elimina info extra del lado
)

fig.show()
```

**🎯 ACTIVIDAD (5 min):** Personaliza el hover de uno de tus gráficos

---

## 4.2 Dropdown Interactivo (20 minutos)

**Crear archivo: `06_dropdown.py`**

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
df_2007 = df.query("year==2007 & continent=='Americas'")

fig = go.Figure()

# Agregar múltiples traces (uno por cada métrica)
metricas = ['lifeExp', 'gdpPercap', 'pop']
nombres = ['Esperanza de Vida', 'PIB per Cápita', 'Población']

for i, (metrica, nombre) in enumerate(zip(metricas, nombres)):
    fig.add_trace(go.Bar(
        x=df_2007['country'],
        y=df_2007[metrica],
        name=nombre,
        visible=(i == 0)  # Solo el primero visible
    ))

# Crear dropdown
buttons = []
for i, nombre in enumerate(nombres):
    visible = [False] * len(nombres)
    visible[i] = True
    
    buttons.append(dict(
        label=nombre,
        method="update",
        args=[
            {"visible": visible},
            {"title": f"{nombre} por País - Américas 2007"}
        ]
    ))

fig.update_layout(
    updatemenus=[dict(
        active=0,
        buttons=buttons,
        direction="down",
        showactive=True,
        x=0.1,
        y=1.15
    )],
    title='Esperanza de Vida por País - Américas 2007',
    height=600
)

fig.show()
```

**🎯 ACTIVIDAD (10 min):** Crea dropdown con 2-3 métricas de tu proyecto

---

## 4.3 Animación con Slider (20 minutos)

**Crear archivo: `07_animacion.py`**

```python
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# ANIMACIÓN TEMPORAL
fig = px.scatter(
    df, 
    x='gdpPercap', 
    y='lifeExp', 
    animation_frame='year',      # ← La magia está aquí
    animation_group='country',
    size='pop', 
    color='continent', 
    hover_name='country',
    log_x=True, 
    size_max=55, 
    range_x=[100, 100000], 
    range_y=[25, 90],
    title='Evolución del Desarrollo Global 1952-2007'
)

# Hacer la animación más lenta
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000  # 1 segundo por frame

fig.show()
```

**🎯 ACTIVIDAD (5 min):** Si tus datos tienen columna temporal, crea una animación

---

## 4.4 Subplots Interactivo (15 minutos)

**Crear archivo: `08_subplot_interactivo.py`**

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
df_2007 = df[df['year']==2007]
top10 = df_2007.nlargest(10, 'pop')

fig = make_subplots(
    rows=2, cols=2, 
    subplot_titles=('Scatter', 'Line', 'Bar', 'Box')
)

# Scatter
fig.add_trace(
    go.Scatter(x=df_2007['gdpPercap'], y=df_2007['lifeExp'], mode='markers'), 
    row=1, col=1
)

# Line
colombia = df[df['country']=='Colombia']
fig.add_trace(
    go.Scatter(x=colombia['year'], y=colombia['lifeExp'], mode='lines'), 
    row=1, col=2
)

# Bar
fig.add_trace(
    go.Bar(x=top10['country'], y=top10['pop']), 
    row=2, col=1
)

# Box
fig.add_trace(
    go.Box(x=df_2007['continent'], y=df_2007['lifeExp']), 
    row=2, col=2
)

fig.update_layout(height=600, showlegend=False)
fig.show()
```

---

# 5. PART 4: STREAMLIT - FIRST APP

## 5.1 Basic App in 10 Minutes

**What we're doing:** Transforming your Plotly charts into an interactive web dashboard that anyone can access through a browser - no HTML/CSS/JavaScript knowledge required!

**Why this is amazing:** With just Python, you can create web apps that update in real-time, have interactive filters, and can be shared with anyone.

**The magic:** Streamlit automatically converts Python scripts into web interfaces.

**Step 1:** Create a new file called `app_basic.py`

**Step 2:** Copy this complete basic app:

```python
import streamlit as st
import plotly.express as px
import pandas as pd

# ========================================
# PAGE CONFIGURATION
# ========================================
# THIS MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title='My Dashboard',      # Browser tab title
    page_icon='📊',                  # Browser tab icon
    layout='wide'                    # Use full width of browser
)

# ========================================
# TITLE
# ========================================
st.title('🌍 My First Interactive Dashboard')
st.markdown('---')  # Horizontal line

# ========================================
# LOAD DATA (with caching for performance)
# ========================================
# @st.cache_data makes Streamlit remember the data
# so it doesn't reload every time the app updates
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

df = load_data()

# ========================================
# SIDEBAR - FILTERS
# ========================================
st.sidebar.header('🎛️ Filters')

# Slider for year selection
year = st.sidebar.slider(
    'Year',
    min_value=int(df['year'].min()),  # Earliest year
    max_value=int(df['year'].max()),  # Latest year
    value=2007                         # Default value
)

# Multi-select for continents
continents = st.sidebar.multiselect(
    'Continents',
    options=df['continent'].unique(),    # All available continents
    default=df['continent'].unique()     # Select all by default
)

# ========================================
# FILTER DATA based on user selections
# ========================================
df_filtered = df[(df['year']==year) & (df['continent'].isin(continents))]

# ========================================
# KEY METRICS - Top of dashboard
# ========================================
col1, col2, col3 = st.columns(3)  # Create 3 equal columns

with col1:
    st.metric(
        '🌍 Countries',
        len(df_filtered),
        help='Total countries in selection'
    )

with col2:
    st.metric(
        '👥 Total Population',
        f"{df_filtered['pop'].sum()/1e9:.2f}B"  # Convert to billions
    )

with col3:
    st.metric(
        '❤️ Average Life Expectancy',
        f"{df_filtered['lifeExp'].mean():.1f} years"
    )

st.markdown('---')

# ========================================
# MAIN CHART
# ========================================
st.subheader(f'📊 Global Development - {year}')

# Create Plotly chart
fig = px.scatter(
    df_filtered,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    title=f'GDP vs Life Expectancy ({year})'
)

# Display chart in Streamlit
# use_container_width=True makes it responsive
st.plotly_chart(fig, use_container_width=True)

# ========================================
# DATA TABLE (optional toggle)
# ========================================
if st.checkbox('📋 Show raw data'):
    st.dataframe(df_filtered, use_container_width=True)
```

**Step 3:** Run the app!

```bash
streamlit run app_basic.py
```

**🎉 What happens:**
1. Terminal shows a local URL (usually `http://localhost:8501`)
2. Browser opens automatically with your dashboard
3. Try changing the year slider - the chart updates instantly!
4. Try selecting/deselecting continents - everything updates in real-time!

**🤯 Mind-blowing facts:**
- No HTML/CSS/JavaScript was written
- Updates happen automatically when you interact
- The app is fully responsive
- You can share the URL with anyone on your network

**🎯 HANDS-ON ACTIVITY (10 minutes):**
1. Copy and run the exact code above
2. Move the year slider and watch the chart update
3. Uncheck a continent and see it disappear
4. Toggle the "Show raw data" checkbox
5. Try resizing your browser window - it's responsive!

**💡 How Streamlit works:**
- Streamlit reruns your entire script top-to-bottom when anything changes
- Cached functions (@st.cache_data) only run once
- Interactive widgets automatically trigger reruns
- It's pure Python, but outputs HTML/JavaScript

---

## 5.2 Componentes Esenciales de Streamlit (20 minutos)

**Crear archivo: `componentes_streamlit.py`**

```python
import streamlit as st
import pandas as pd

st.title('📚 Componentes de Streamlit')

# ========================================
# 1. TEXTO Y TÍTULOS
# ========================================
st.header('1. Texto y Títulos')
st.subheader('Esto es un subheader')
st.text('Texto normal')
st.markdown('**Negrita** y *cursiva* y `código`')
st.code('print("Hola Mundo")', language='python')

st.markdown('---')

# ========================================
# 2. INPUTS EN SIDEBAR
# ========================================
st.header('2. Widgets de Input')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Sidebar Inputs')
    
    opcion = st.sidebar.selectbox(
        'Select Box (escoge 1)',
        ['Opción A', 'Opción B', 'Opción C']
    )
    st.write(f'Seleccionaste: {opcion}')
    
    multi = st.sidebar.multiselect(
        'Multi-Select (escoge varios)',
        ['A', 'B', 'C', 'D'],
        default=['A']
    )
    st.write(f'Seleccionaste: {multi}')
    
    numero = st.sidebar.slider(
        'Slider',
        min_value=0,
        max_value=100,
        value=50
    )
    st.write(f'Valor: {numero}')

with col2:
    st.subheader('Más Inputs')
    
    radio = st.sidebar.radio(
        'Radio Buttons',
        ['Opción 1', 'Opción 2', 'Opción 3']
    )
    st.write(f'Radio: {radio}')
    
    check = st.sidebar.checkbox('Checkbox')
    st.write(f'Checked: {check}')
    
    texto = st.sidebar.text_input('Text Input', 'Escribe aquí')
    st.write(f'Texto: {texto}')

st.markdown('---')

# ========================================
# 3. MOSTRAR DATOS
# ========================================
st.header('3. Mostrar Datos')

df = pd.DataFrame({
    'Columna A': [1, 2, 3, 4],
    'Columna B': [10, 20, 30, 40]
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

# Columnas
st.subheader('Columnas')
col1, col2, col3 = st.columns(3)
col1.write('Columna 1')
col2.write('Columna 2')
col3.write('Columna 3')

# Tabs
st.subheader('Tabs')
tab1, tab2, tab3 = st.tabs(['Tab 1', 'Tab 2', 'Tab 3'])
with tab1:
    st.write('Contenido Tab 1')
with tab2:
    st.write('Contenido Tab 2')
with tab3:
    st.write('Contenido Tab 3')

# Expander
st.subheader('Expander')
with st.expander('Click para expandir'):
    st.write('Contenido oculto que se revela al click')

# Contenedor
st.subheader('Container')
container = st.container()
container.write('Esto está en un contenedor')
```

**🎯 ACTIVIDAD (10 min):** Agrega 5 widgets diferentes a `app_basica.py`

---

# 6. PARTE 5: DASHBOARD COMPLETO

**Crear archivo: `dashboard_completo.py`**

```python
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# ========================================
# CONFIGURACIÓN
# ========================================
st.set_page_config(
    page_title='Dashboard Analítica', 
    layout='wide', 
    page_icon='📊'
)

# ========================================
# CARGAR DATOS
# ========================================
@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

df = load_data()

# ========================================
# HEADER
# ========================================
st.title('📊 Dashboard de Análisis Global')
st.markdown('**Análisis de Desarrollo Humano por País y Continente**')
st.markdown('---')

# ========================================
# SIDEBAR
# ========================================
st.sidebar.title('🎛️ Controles')
st.sidebar.markdown('---')

year = st.sidebar.slider(
    '📅 Año', 
    1952, 2007, 2007, 5
)

continents = st.sidebar.multiselect(
    '🌍 Continentes',
    df['continent'].unique(), 
    default=df['continent'].unique()
)

show_data = st.sidebar.checkbox('📋 Mostrar datos crudos')

st.sidebar.markdown('---')
st.sidebar.markdown('**Creado con:**')
st.sidebar.markdown('🐍 Python + Plotly + Streamlit')

# ========================================
# FILTRAR DATOS
# ========================================
df_filtered = df[(df['year']==year) & (df['continent'].isin(continents))]

# ========================================
# MÉTRICAS TOP
# ========================================
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    '🌍 Países',
    len(df_filtered),
    help='Total de países'
)

col2.metric(
    '👥 Población',
    f"{df_filtered['pop'].sum()/1e9:.2f}B"
)

col3.metric(
    '💰 PIB Promedio',
    f"${df_filtered['gdpPercap'].mean():,.0f}"
)

col4.metric(
    '❤️ Esperanza Vida',
    f"{df_filtered['lifeExp'].mean():.1f} años"
)

st.markdown('---')

# ========================================
# TABS PRINCIPALES
# ========================================
tab1, tab2, tab3 = st.tabs(['📈 Análisis General', '🗺️ Por Continente', '📊 Distribuciones'])

# ========================================
# TAB 1: ANÁLISIS GENERAL
# ========================================
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('PIB vs Esperanza de Vida')
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
        st.subheader('Evolución Temporal Promedio')
        df_evolution = df[df['continent'].isin(continents)].groupby('year').agg({
            'lifeExp': 'mean',
            'gdpPercap': 'mean'
        }).reset_index()
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=df_evolution['year'], 
            y=df_evolution['lifeExp'],
            mode='lines+markers', 
            name='Esperanza Vida',
            line=dict(color='green', width=3)
        ))
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, use_container_width=True)

# ========================================
# TAB 2: POR CONTINENTE
# ========================================
with tab2:
    continent_select = st.selectbox(
        'Selecciona Continente',
        continents
    )
    
    df_continent = df_filtered[df_filtered['continent']==continent_select].nlargest(10, 'pop')
    
    fig3 = px.bar(
        df_continent, 
        x='country', 
        y='pop', 
        title=f'Top 10 Países por Población - {continent_select}',
        color='pop',
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig3, use_container_width=True)

# ========================================
# TAB 3: DISTRIBUCIONES
# ========================================
with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Distribución Esperanza de Vida')
        fig4 = px.histogram(
            df_filtered, 
            x='lifeExp', 
            nbins=20,
            color='continent'
        )
        st.plotly_chart(fig4, use_container_width=True)
    
    with col2:
        st.subheader('Distribución PIB por Continente')
        fig5 = px.box(
            df_filtered, 
            x='continent', 
            y='gdpPercap',
            color='continent'
        )
        st.plotly_chart(fig5, use_container_width=True)

# ========================================
# DATOS CRUDOS
# ========================================
if show_data:
    st.markdown('---')
    st.subheader('📋 Datos Crudos')
    st.dataframe(df_filtered, use_container_width=True)
    
    # Botón de descarga
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        '⬇️ Descargar CSV',
        csv,
        'datos_filtrados.csv',
        'text/csv'
    )
```

**🚀 CORRER:**
```bash
streamlit run dashboard_completo.py
```

**🎯 ACTIVIDAD (20 min):** Replicar el dashboard completo

---

# 7. PARTE 6: TU PROYECTO

## 7.1 Template Base para Tu Dashboard

**Crear archivo: `mi_proyecto.py`**

```python
import streamlit as st
import plotly.express as px
import pandas as pd

# ========================================
# CONFIGURACIÓN
# ========================================
st.set_page_config(
    page_title='Mi Proyecto',
    layout='wide',
    page_icon='📊'
)

# ========================================
# CARGAR TUS DATOS
# ========================================
@st.cache_data
def load_data():
    # CAMBIAR AQUÍ POR TU ARCHIVO
    return pd.read_csv('tu_archivo.csv')

df = load_data()

# ========================================
# MOSTRAR PRIMERAS FILAS (para verificar)
# ========================================
st.title('🎯 Mi Proyecto - [Nombre]')
st.markdown('---')

st.subheader('Vista Previa de Datos')
st.dataframe(df.head())

st.write('**Columnas disponibles:**', df.columns.tolist())
st.write('**Shape:**', df.shape)

# ========================================
# SIDEBAR - FILTROS
# ========================================
st.sidebar.header('🎛️ Filtros')

# EJEMPLO: Filtro por columna categórica
# CAMBIAR 'columna_categoria' por tu columna
if 'columna_categoria' in df.columns:
    categoria = st.sidebar.multiselect(
        'Selecciona Categoría',
        df['columna_categoria'].unique()
    )

# EJEMPLO: Filtro por rango numérico
# CAMBIAR 'columna_numerica' por tu columna
if 'columna_numerica' in df.columns:
    min_val = float(df['columna_numerica'].min())
    max_val = float(df['columna_numerica'].max())
    
    rango = st.sidebar.slider(
        'Rango Numérico',
        min_val,
        max_val,
        (min_val, max_val)
    )

# ========================================
# MÉTRICAS
# ========================================
st.markdown('---')
st.subheader('📊 Métricas Principales')

col1, col2, col3, col4 = st.columns(4)

# PERSONALIZAR ESTAS MÉTRICAS SEGÚN TU PROYECTO
col1.metric('Métrica 1', 'Valor 1')
col2.metric('Métrica 2', 'Valor 2')
col3.metric('Métrica 3', 'Valor 3')
col4.metric('Métrica 4', 'Valor 4')

# ========================================
# GRÁFICOS
# ========================================
st.markdown('---')

tab1, tab2, tab3 = st.tabs(['Análisis 1', 'Análisis 2', 'Análisis 3'])

with tab1:
    st.subheader('Gráfico 1')
    # AGREGAR TU GRÁFICO AQUÍ
    # fig1 = px.scatter(df, x='columna_x', y='columna_y')
    # st.plotly_chart(fig1, use_container_width=True)
    st.info('👆 Agrega tu primer gráfico aquí')

with tab2:
    st.subheader('Gráfico 2')
    # AGREGAR TU GRÁFICO AQUÍ
    st.info('👆 Agrega tu segundo gráfico aquí')

with tab3:
    st.subheader('Gráfico 3')
    # AGREGAR TU GRÁFICO AQUÍ
    st.info('👆 Agrega tu tercer gráfico aquí')
```

**🎯 ACTIVIDAD FINAL (45 min):**

1. Copia el template `mi_proyecto.py`
2. Carga TUS datos del proyecto
3. Identifica 3-4 visualizaciones clave
4. Crea 3-5 filtros relevantes
5. Agrega 4 métricas importantes
6. Organiza en tabs lógicos

---

# 8. TIPS Y TRICKS

## 8.1 Caché para Performance

```python
# SIEMPRE usa @st.cache_data para cargar datos
@st.cache_data
def load_data():
    return pd.read_csv('archivo.csv')

# SIEMPRE usa @st.cache_data para cálculos pesados
@st.cache_data
def calcular_estadisticas(df):
    return df.groupby('categoria').mean()
```

## 8.2 Mostrar Spinner Durante Carga

```python
with st.spinner('Cargando datos...'):
    df = load_data()
st.success('✅ Datos cargados!')
```

## 8.3 Mensajes de Estado

```python
st.info('ℹ️ Información importante')
st.success('✅ Operación exitosa')
st.warning('⚠️ Advertencia')
st.error('❌ Error')
```

## 8.4 Progress Bar

```python
import time

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)
st.success('Completado!')
```

---

# 9. HOMEWORK ASSIGNMENT

## 📝 Deliverable for Next Class:

**Build a Streamlit Dashboard with YOUR project data that includes:**

### Minimum Requirements:

✅ **5+ interactive Plotly charts**
   - Choose appropriate chart types for your data
   - Each chart must tell a story
   - All charts must be interactive (zoom, hover, etc.)

✅ **4 metrics/KPIs**
   - Display key statistics prominently
   - Use `st.metric()` with clear labels
   - Consider adding delta (change) indicators

✅ **3+ functional filters**
   - Must actually filter the data
   - Use appropriate widget types (slider, multiselect, etc.)
   - Filters should be intuitive and labeled clearly

✅ **Organized layout**
   - Use tabs or sections logically
   - Group related visualizations together
   - Clear navigation for users

✅ **Coherent theme/colors**
   - Consistent color scheme throughout
   - Professional appearance
   - Good contrast and readability

---

## Grading Rubric:

### **40% - Functionality**
- Dashboard runs without errors
- All filters work correctly
- Data loads properly
- Charts display correctly
- No broken features

### **30% - Appropriate Visualizations**
- Chart types match the data being shown
- Visualizations answer relevant questions
- Data is presented clearly
- Insights are easy to extract

### **20% - User Experience**
- Filters are intuitive and well-labeled
- Layout is logical and easy to navigate
- Interactive elements work smoothly
- Good use of white space

### **10% - Professional Design**
- Clean, professional appearance
- Consistent color scheme
- Proper labels and titles
- No typos or formatting issues

---

## Submission Instructions:

1. **File name:** `your_lastname_dashboard.py`
2. **Include:** A short README.txt with:
   - Your name
   - Brief description of your dataset
   - Instructions to run (if special data file needed)
3. **Submit by:** [Insert deadline]
4. **Format:** Python file + data file (if using local data)

---

## Tips for Success:

🎯 **Start early!** Don't wait until the night before

📊 **Test with real data** - Make sure your filters and charts work with your actual dataset

🎨 **Keep it simple** - A clean, working dashboard beats a complex, broken one

💡 **Ask questions** - If stuck, reach out during office hours

🔄 **Iterate** - Build one feature at a time, test it, then add the next

---

## Common Mistakes to Avoid:

❌ Using inappropriate chart types (e.g., pie chart for time series)
❌ Too many filters that don't add value
❌ Cluttered layout with no clear organization
❌ Missing labels or unclear axis names
❌ Filters that don't actually filter the data
❌ Using different datasets for different charts (keep it cohesive!)
❌ Not testing before submission

---

# 10. ADDITIONAL RESOURCES

## 📚 Official Documentation:

### Plotly
- **Main docs:** https://plotly.com/python/
- **Plotly Express API:** https://plotly.com/python/plotly-express/
- **Figure reference:** https://plotly.com/python/reference/
- **Chart types:** https://plotly.com/python/basic-charts/

### Streamlit
- **Main docs:** https://docs.streamlit.io/
- **API reference:** https://docs.streamlit.io/library/api-reference
- **Cheat sheet:** https://docs.streamlit.io/library/cheatsheet
- **Deployment guide:** https://docs.streamlit.io/streamlit-community-cloud/get-started

### Pandas (for data manipulation)
- **Main docs:** https://pandas.pydata.org/docs/
- **10 minutes to pandas:** https://pandas.pydata.org/docs/user_guide/10min.html

---

## 🎨 Inspiration Galleries:

### Plotly Examples
- **Gallery:** https://plotly.com/python/
- **Chart Studio:** https://chart-studio.plotly.com/feed/#/
- **Community forums:** https://community.plotly.com/

### Streamlit Showcases
- **App gallery:** https://streamlit.io/gallery
- **Community cloud:** https://streamlit.io/cloud
- **30 days of Streamlit:** https://30days.streamlit.app/

---

## 🆘 Troubleshooting Guide:

### Installation Issues
**Problem:** `pip install` fails
- **Solution:** Try `pip install --upgrade pip` first, then retry
- **Alternative:** Use `pip3` instead of `pip` on Mac/Linux
- **Virtual env:** Make sure you're in the correct environment

### Import Errors
**Problem:** `ModuleNotFoundError: No module named 'plotly'`
- **Solution:** Run `pip list` to verify installation
- **Check:** Are you using the right Python interpreter?

### Streamlit Won't Start
**Problem:** `streamlit: command not found`
- **Solution:** Try `python -m streamlit run app.py`
- **Path issue:** Add Streamlit to your PATH

### Data Loading Errors
**Problem:** Can't load CSV file
- **Solution:** Check file path is correct
- **Tip:** Use absolute paths or put file in same directory
- **Debug:** Print `df.head()` to verify data loaded

### Chart Not Displaying
**Problem:** Blank chart or error
- **Solution:** Check column names with `st.write(df.columns)`
- **Verify:** Do the columns exist in your data?
- **Type check:** Are you using numeric data for numeric charts?

### Common Pandas Errors
**Problem:** KeyError for column name
- **Solution:** Column names are case-sensitive!
- **Check:** Use `df.columns.tolist()` to see exact names

---

## 💡 Pro Tips & Best Practices:

### Performance
- ✅ Always use `@st.cache_data` for data loading
- ✅ Filter data before plotting (not after)
- ✅ Use `use_container_width=True` for responsive charts
- ❌ Don't load data inside loops

### Design
- ✅ Use consistent color schemes
- ✅ Label all axes clearly
- ✅ Add helpful titles and descriptions
- ❌ Don't overcrowd charts with too much data

### User Experience
- ✅ Provide sensible default filter values
- ✅ Use expanders for advanced options
- ✅ Add help text to explain metrics
- ❌ Don't require users to select everything manually

---

# 11. QUICK REFERENCE CHEATSHEET

## Plotly Express - The 6 Essential Charts:

```python
# SCATTER - Relationships between 2 variables
px.scatter(df, x='col1', y='col2', color='category', size='value')

# LINE - Trends over time
px.line(df, x='date', y='value', color='category')

# BAR - Compare categories
px.bar(df, x='category', y='value', color='subcategory')

# HISTOGRAM - Distribution of 1 variable
px.histogram(df, x='value', nbins=20)

# BOX - Compare distributions across groups
px.box(df, x='group', y='value', color='group')

# TREEMAP - Hierarchical proportions
px.treemap(df, path=['level1', 'level2'], values='size')
```

## Plotly Customization:

```python
# Update layout
fig.update_layout(
    title='My Title',
    template='plotly_white',
    height=600,
    showlegend=True
)

# Update axes
fig.update_xaxes(title='X Label', showgrid=True)
fig.update_yaxes(title='Y Label', range=[0, 100])
```

## Streamlit - Essential Components:

```python
# Page config (MUST BE FIRST!)
st.set_page_config(page_title='My App', layout='wide')

# Text elements
st.title('Main Title')
st.header('Section Header')
st.subheader('Subsection')
st.text('Plain text')
st.markdown('**Bold** and *italic*')

# Widgets
option = st.selectbox('Choose:', ['A', 'B', 'C'])
value = st.slider('Select value:', 0, 100, 50)
checked = st.checkbox('Check me')
multi = st.multiselect('Pick many:', ['X', 'Y', 'Z'])

# Layout
col1, col2, col3 = st.columns(3)
tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])

# Display data
st.metric('Label', value, delta=change)
st.plotly_chart(fig, use_container_width=True)
st.dataframe(df)

# Caching (for performance!)
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')
```

## Common Patterns:

```python
# Filter pattern
filtered_df = df[
    (df['date'] >= start_date) &
    (df['date'] <= end_date) &
    (df['category'].isin(selected_categories))
]

# Multi-column layout pattern
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Metric 1', value1)
with col2:
    st.metric('Metric 2', value2)
with col3:
    st.metric('Metric 3', value3)

# Tab pattern
tab1, tab2, tab3 = st.tabs(['Overview', 'Details', 'Raw Data'])
with tab1:
    st.plotly_chart(overview_chart)
with tab2:
    st.plotly_chart(detailed_chart)
with tab3:
    st.dataframe(df)
```

---

## 🎉 CONGRATULATIONS!

**You now know how to create interactive dashboards from scratch!**

### What you learned today:
✅ Creating 6 types of interactive charts with Plotly
✅ Customizing visualizations professionally
✅ Building web dashboards with Streamlit
✅ Implementing filters and interactivity
✅ Deploying data apps without web development

### Next class:
**Power BI** - Enterprise Dashboard Development

---

**Remember:** The best way to learn is by doing. Build your project dashboard and experiment!

---

*Manual created for Data Analytics Course - Universidad Cooperativa de Colombia*
*Prof. Julian Eduardo Garzon Giraldo, MsC*
*Translated and enhanced with detailed step-by-step instructions*