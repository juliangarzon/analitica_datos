"""
Animated Chart with Time Slider
Class 8: Plotly + Streamlit - Part 3

What you'll learn:
- How to create animated visualizations
- Adding time-based animations with a slider
"""

import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.csv')

# ANIMATED SCATTER PLOT
fig = px.scatter(
    df,
    x='gdpPercap',
    y='lifeExp',
    animation_frame='year',      # ← The magic is here!
    animation_group='country',
    size='pop',
    color='continent',
    hover_name='country',
    log_x=True,
    size_max=55,
    range_x=[100, 100000],       # Fixed ranges for consistent animation
    range_y=[25, 90],
    title='Evolution of Global Development 1952-2007'
)

# Make animation slower (1 second per frame)
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000

fig.show()

print("""
🎬 Try these controls:
- Click PLAY to watch the animation
- Use the slider to jump to specific years
- Pause and explore any year in detail
- Watch how countries move over time!
""")
