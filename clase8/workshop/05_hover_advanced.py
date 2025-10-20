"""
Advanced Hover Customization
Class 8: Plotly + Streamlit - Part 3

What you'll learn:
- How to customize hover tooltips
- Formatting numbers and text in hover boxes
"""

import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
df_2007 = df[df['year']==2007]

# HOVER CUSTOMIZATION
fig = px.scatter(
    df_2007,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    color='continent',
    hover_name='country',        # Main name shown on hover
    hover_data={
        'gdpPercap': ':,.0f',    # Format with commas, no decimals
        'lifeExp': ':.1f',       # 1 decimal place
        'pop': ':,.0f',          # Format with commas
        'continent': False       # Don't show (already in color)
    },
    title='Custom Hover Information'
)

# Advanced hover template
fig.update_traces(
    hovertemplate='<b>%{hovertext}</b><br><br>' +
                  'GDP: $%{x:,.0f}<br>' +
                  'Life Expectancy: %{y:.1f} years<br>' +
                  'Population: %{marker.size:,.0f}<br>' +
                  '<extra></extra>'  # Remove extra info on the side
)

fig.show()

print("""
💡 Hover Format Codes:
- ':,.0f' = Number with commas, no decimals (1,234,567)
- ':.1f' = Number with 1 decimal (75.5)
- ':.2f' = Number with 2 decimals (75.53)
- '%{x}' = X value
- '%{y}' = Y value
- '%{hovertext}' = Hover name
""")
