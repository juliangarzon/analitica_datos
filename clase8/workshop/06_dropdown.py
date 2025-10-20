"""
Interactive Dropdown Menu
Class 8: Plotly + Streamlit - Part 3

What you'll learn:
- How to add dropdown menus to switch between metrics
- Creating interactive controls in Plotly
"""

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')
df_2007 = df.query("year==2007 & continent=='Americas'")

fig = go.Figure()

# Add multiple traces (one per metric)
metrics = ['lifeExp', 'gdpPercap', 'pop']
names = ['Life Expectancy', 'GDP per Capita', 'Population']

for i, (metric, name) in enumerate(zip(metrics, names)):
    fig.add_trace(go.Bar(
        x=df_2007['country'],
        y=df_2007[metric],
        name=name,
        visible=(i == 0)  # Only first one visible by default
    ))

# Create dropdown buttons
buttons = []
for i, name in enumerate(names):
    visible = [False] * len(names)
    visible[i] = True

    buttons.append(dict(
        label=name,
        method="update",
        args=[
            {"visible": visible},
            {"title": f"{name} by Country - Americas 2007"}
        ]
    ))

# Add dropdown menu
fig.update_layout(
    updatemenus=[dict(
        active=0,
        buttons=buttons,
        direction="down",
        showactive=True,
        x=0.1,
        y=1.15
    )],
    title='Life Expectancy by Country - Americas 2007',
    height=600
)

fig.show()

print("✅ Click the dropdown menu at the top to switch between metrics!")
