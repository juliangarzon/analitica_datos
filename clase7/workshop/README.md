# Workshop: Effective Data Visualization

## Objective
Apply the concepts learned in class about data visualization to create clear and effective presentations of a dataset of your choice.

## Instructions

### 1. Dataset Selection (15 minutes)
Find a small dataset (maximum 100 records) that interests you. You can use:
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- Public data from your country or city

**Selection criteria:**
- Between 50-100 records
- At least 5 variables (columns)
- Mix of numerical and categorical variables
- Topic that interests you

### 2. Initial Exploration (20 minutes)
Perform a basic exploratory analysis:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('your_dataset.csv')

# Basic exploration
print(df.head())
print(df.info())
print(df.describe())

# Identify:
# - Variable types
# - Missing values
# - Distributions
# - Potential relationships
```

### 3. Story Definition (15 minutes)
Answer the following questions:
- What is the main message I want to communicate?
- Who is my audience?
- What questions do I want to answer with the data?
- What insights are most relevant?

Write a paragraph with the story you want to tell.

### 4. Visualization Design (30 minutes)
Create 3-5 visualizations that tell your story:

#### Visualization 1: Distribution
Show the distribution of a key variable
```python
# Example: Histogram or boxplot
plt.figure(figsize=(10, 6))
# Your code here
```

#### Visualization 2: Relationship
Explore the relationship between two variables
```python
# Example: Scatter plot or trend line
plt.figure(figsize=(10, 6))
# Your code here
```

#### Visualization 3: Comparison
Compare categories or groups
```python
# Example: Bar plot or violin plot
plt.figure(figsize=(10, 6))
# Your code here
```

#### Visualization 4: Composition
Show parts of a whole
```python
# Example: Pie chart or stacked bar
plt.figure(figsize=(10, 6))
# Your code here
```

### 5. Visual Enhancement (20 minutes)
Apply effective design principles:

- **Simplicity**: Remove unnecessary elements
- **Clarity**: Descriptive titles and clear labels
- **Color**: Use coherent and accessible palette
- **Hierarchy**: Highlight what's most important

```python
# Example of enhanced visualization
fig, ax = plt.subplots(figsize=(12, 7))

# Your visualization here

# Design improvements
ax.set_title('Clear and Descriptive Title', fontsize=16, fontweight='bold')
ax.set_xlabel('X Variable', fontsize=12)
ax.set_ylabel('Y Variable', fontsize=12)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
```

### 6. Final Dashboard (20 minutes)
Create a dashboard that combines the visualizations:

```python
fig = plt.figure(figsize=(15, 10))

# Subplot 1
ax1 = plt.subplot(2, 2, 1)
# Visualization 1

# Subplot 2
ax2 = plt.subplot(2, 2, 2)
# Visualization 2

# Subplot 3
ax3 = plt.subplot(2, 2, 3)
# Visualization 3

# Subplot 4
ax4 = plt.subplot(2, 2, 4)
# Visualization 4

plt.suptitle('Your Main Title', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

## Deliverables

1. **Jupyter Notebook** with:
   - Data loading and exploration code
   - All visualizations with their code
   - Comments explaining design decisions

2. **Presentation** (3 slides):
   - Slide 1: Dataset context and main question
   - Slide 2: Key visualizations (2-3)
   - Slide 3: Insights and conclusions

3. **Written reflection** (1 paragraph):
   - What visualization principles did you apply?
   - What design decisions did you make and why?
   - What did you learn from the process?

## Evaluation Criteria

- **Message clarity** (30%): Do the visualizations communicate effectively?
- **Visual design** (30%): Did you apply effective design principles?
- **Code** (20%): Is the code clean and reproducible?
- **Storytelling** (20%): Is there a coherent narrative?

## Additional Tips

✅ **DO's:**
- Keep consistency in colors and styles
- Use descriptive titles
- Include units on axes
- Consider color accessibility
- Try different chart types

❌ **DON'Ts:**
- Don't use 3D charts unnecessarily
- Don't overload with information
- Don't use too many colors
- Don't forget labels
- Don't distort scales

## Useful Resources

- [Data to Viz](https://www.data-to-viz.com/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Color Palettes](https://colorbrewer2.org/)
- [Data Viz Catalogue](https://datavizcatalogue.com/)

## Total Estimated Time: 2 hours

Good luck with your visualization!