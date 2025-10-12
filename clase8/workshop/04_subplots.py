"""
Multiple Charts in One Figure (Subplots)
Class 8: Plotly + Streamlit - Part 2

What you'll learn:
- How to create dashboard-style layouts with multiple charts
- Combining different chart types in one figure
"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# Create 2x2 grid of subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'GDP vs Life Expectancy',
        'Colombia Evolution',
        'Life Expectancy Distribution',
        'Top 10 Countries by Population'
    ),
    specs=[
        [{'type': 'scatter'}, {'type': 'scatter'}],
        [{'type': 'histogram'}, {'type': 'bar'}]
    ]
)

# Prepare data
df_2007 = df[df['year']==2007]
df_col = df[df['country']=='Colombia']
top10 = df_2007.nlargest(10, 'pop')

# Subplot 1: Scatter (row 1, column 1)
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

# Subplot 2: Line (row 1, column 2)
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

# Subplot 3: Histogram (row 2, column 1)
fig.add_trace(
    go.Histogram(
        x=df_2007['lifeExp'],
        name='Distribution',
        marker=dict(color='orange')
    ),
    row=2, col=1
)

# Subplot 4: Bar (row 2, column 2)
fig.add_trace(
    go.Bar(
        x=top10['country'],
        y=top10['pop'],
        name='Top 10',
        marker=dict(color='red')
    ),
    row=2, col=2
)

# Global layout
fig.update_layout(
    height=800,
    showlegend=False,
    title_text='Multi-Chart Dashboard - Gapminder 2007'
)

fig.show()
