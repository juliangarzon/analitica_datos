#!/usr/bin/env python3
"""
Script to export charts from Jupyter notebook as images for HTML presentation
Run this after executing the Jupyter notebook to generate the charts
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set high DPI for crisp images
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0.1

# Load and prepare data (same as notebook)
df = pd.read_csv('Casos_de_maltrato_infantil_Palmira_2022_20250921.csv')
df.columns = df.columns.str.replace('\n', ' ', regex=False)

# Clean data
def clean_text_column(df, column):
    if column in df.columns:
        df[column] = df[column].astype(str).str.lower().str.strip()
        df[column] = df[column].replace(['no aplica', 'no registro', 'no', 'ninguno', 'nan'], 'no')
        df[column] = df[column].replace(['si', 'sí'], 'si')
    return df

abuse_columns = ['FISICA', 'VERBAL', 'ECONOMICA', 'PSICOLOGICA', 'SEXUAL']
for col in abuse_columns:
    df = clean_text_column(df, col)

df['GENERO M/F VICTIMA'] = df['GENERO M/F VICTIMA'].astype(str).str.lower().str.strip()
df['PARENTESCO FRENTE A LA VICTIMA'] = df['PARENTESCO FRENTE A LA VICTIMA'].astype(str).str.lower().str.strip()

def extract_age(age_str):
    try:
        age_str = str(age_str)
        import re
        numbers = re.findall(r'\d+', age_str)
        if numbers:
            age = int(numbers[0])
            if 0 <= age <= 100:
                return age
    except:
        pass
    return None

edad_victima_col = [col for col in df.columns if 'EDAD' in col and 'VICTIMA' in col][0]
df['EDAD_VICTIMA_NUM'] = df[edad_victima_col].apply(extract_age)

df['TOTAL_ABUSE_TYPES'] = 0
for col in abuse_columns:
    df['TOTAL_ABUSE_TYPES'] += (df[col] == 'si').astype(int)

# Define colors
colors = {
    'primary': '#1f77b4',
    'danger': '#d62728',
    'warning': '#ff7f0e',
    'success': '#2ca02c',
    'info': '#17becf',
    'dark': '#2F4F4F'
}

gender_colors = {
    'masculino': '#3498db',
    'femenino': '#e74c3c'
}

print("📊 Generating charts for HTML presentation...")

# CHART 1: Intrafamilial Nature (for Slide 3)
print("1. Creating intrafamilial chart...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Donut chart
relationships = df['PARENTESCO FRENTE A LA VICTIMA'].value_counts()
parent_total = relationships.get('madre', 0) + relationships.get('padre', 0)
non_parent_total = len(df) - parent_total

data = [parent_total, non_parent_total]
labels = ['Parents\n(Madre + Padre)', 'Others']
colors_pie = [colors['danger'], colors['warning']]

wedges, texts, autotexts = ax1.pie(data, labels=labels, autopct='%1.1f%%',
                                   colors=colors_pie, startangle=90,
                                   textprops={'fontsize': 12, 'fontweight': 'bold'})

# Create donut hole
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax1.add_artist(centre_circle)
ax1.set_title('Parents vs Others as Aggressors', fontsize=14, fontweight='bold', pad=20)

# Bar chart detail
top_relationships = relationships.head(5)
top_relationships = top_relationships[~top_relationships.index.isin(['no aplica', 'no'])]
colors_bar = [colors['danger'] if rel in ['madre', 'padre'] else colors['warning']
              for rel in top_relationships.index]

bars = ax2.bar(range(len(top_relationships)), top_relationships.values, color=colors_bar)
ax2.set_xticks(range(len(top_relationships)))
ax2.set_xticklabels([rel.title() for rel in top_relationships.index], rotation=45, ha='right')
ax2.set_title('Detailed Breakdown', fontsize=14, fontweight='bold', pad=20)
ax2.set_ylabel('Number of Cases')

for bar, val in zip(bars, top_relationships.values):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
            str(val), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('chart_intrafamilial.png', dpi=300, bbox_inches='tight')
plt.close()

# CHART 2: Multidimensional Abuse (for Slide 4) - IMPROVED VERSION
print("2. Creating improved multidimensional chart...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Left: Pie chart - Single vs Multiple (same as before)
abuse_distribution = df['TOTAL_ABUSE_TYPES'].value_counts().sort_index()
single_abuse = abuse_distribution[abuse_distribution.index <= 1].sum()
multiple_abuse = abuse_distribution[abuse_distribution.index > 1].sum()

pie_data = [single_abuse, multiple_abuse]
pie_labels = ['Tipo Único', 'Múltiples Tipos']
pie_colors = [colors['success'], colors['danger']]

wedges, texts, autotexts = ax1.pie(pie_data, labels=pie_labels, autopct='%1.1f%%',
                                   colors=pie_colors, startangle=90, explode=(0, 0.1),
                                   textprops={'fontsize': 12, 'fontweight': 'bold'})
ax1.set_title('Tipo Único vs Múltiples Tipos\n91.4% Sufren Múltiples Tipos', fontsize=14, fontweight='bold', pad=20)

# Right: IMPROVED - Most common specific combinations
def get_abuse_combination(row):
    types = []
    for col in abuse_columns:
        if row[col] == 'si':
            types.append(col)
    return ' + '.join(sorted(types)) if types else 'None'

df['ABUSE_COMBINATION'] = df.apply(get_abuse_combination, axis=1)

# Get top 7 most common combinations
top_combinations = df['ABUSE_COMBINATION'].value_counts().head(7)
top_combinations = top_combinations[top_combinations.index != 'None']

# Create better labels with Spanish names
abuse_names_es = {
    'FISICA': 'Fís.',
    'VERBAL': 'Verb.',
    'ECONOMICA': 'Econ.',
    'PSICOLOGICA': 'Psic.',
    'SEXUAL': 'Sex.'
}

combination_labels = []
for combo in top_combinations.index:
    if ' + ' in combo:
        types = combo.split(' + ')
        spanish_types = [abuse_names_es.get(t, t) for t in types]
        combination_labels.append(' + '.join(spanish_types))
    else:
        combination_labels.append(abuse_names_es.get(combo, combo))

# Color based on number of types in combination
colors_combo = []
for combo in top_combinations.index:
    num_types = len(combo.split(' + ')) if ' + ' in combo else 1
    if num_types >= 4:
        colors_combo.append(colors['danger'])
    elif num_types == 3:
        colors_combo.append(colors['warning'])
    else:
        colors_combo.append(colors['primary'])

bars = ax2.barh(range(len(top_combinations)), top_combinations.values,
                color=colors_combo, edgecolor='white', linewidth=1)

ax2.set_yticks(range(len(top_combinations)))
ax2.set_yticklabels(combination_labels, fontsize=11)
ax2.set_title('Combinaciones Específicas Más Comunes\nQué Tipos Ocurren Juntos',
             fontweight='bold', fontsize=14, pad=20)
ax2.set_xlabel('Número de Casos', fontweight='bold')

# Add value and percentage labels
for bar, val in zip(bars, top_combinations.values):
    percentage = val / len(df) * 100
    ax2.text(val + 3, bar.get_y() + bar.get_height()/2,
            f'{val}\n({percentage:.1f}%)', va='center', fontweight='bold', fontsize=10)

ax2.grid(True, alpha=0.3, axis='x')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('chart_multidimensional.png', dpi=300, bbox_inches='tight')
plt.close()

# CHART 3: Psychological Universality (for Slide 5)
print("3. Creating psychological universality chart...")
fig, ax = plt.subplots(figsize=(12, 8))

# Create better labels with Spanish names and definitions
abuse_data = []
abuse_labels_spanish = {
    'FISICA': '🤛 Físico\n(Golpes, lesiones)',
    'VERBAL': '🗣️ Verbal\n(Gritos, insultos)',
    'ECONOMICA': '💰 Económico\n(Control recursos)',
    'PSICOLOGICA': '🧠 Psicológico\n(Daño emocional)',
    'SEXUAL': '⚠️ Sexual\n(Contacto inapropiado)'
}

for col in abuse_columns:
    count = (df[col] == 'si').sum()
    percentage = (count / len(df)) * 100
    label = abuse_labels_spanish.get(col, col.title())
    abuse_data.append({'Type': label, 'Count': count, 'Percentage': percentage})

abuse_df = pd.DataFrame(abuse_data).sort_values('Percentage', ascending=True)

colors_prev = [colors['danger'] if p > 80 else
               colors['warning'] if p > 50 else
               colors['primary'] for p in abuse_df['Percentage']]

bars = ax.barh(abuse_df['Type'], abuse_df['Percentage'], color=colors_prev, height=0.6)

for i, (bar, val, count) in enumerate(zip(bars, abuse_df['Percentage'], abuse_df['Count'])):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2,
            f'{val:.1f}%\n({count} casos)', va='center', fontweight='bold', fontsize=11)

ax.set_xlabel('Porcentaje de Casos', fontweight='bold', fontsize=12)
ax.set_title('Prevalencia por Tipo de Maltrato\nDaño Psicológico Prácticamente Universal',
             fontweight='bold', fontsize=16, pad=20)
ax.set_xlim(0, max(abuse_df['Percentage']) * 1.2)

# Highlight psychological abuse
for i, bar in enumerate(bars):
    if '🧠' in abuse_df.iloc[i]['Type']:
        bar.set_edgecolor('black')
        bar.set_linewidth(3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('chart_psychological.png', dpi=300, bbox_inches='tight')
plt.close()

# CHART 4: Demographics (for Slide 6)
print("4. Creating demographics chart...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Gender pie chart
gender_counts = df['GENERO M/F VICTIMA'].value_counts()
valid_genders = gender_counts[gender_counts.index.isin(['masculino', 'femenino'])]
colors_gender = [gender_colors.get(g, '#95a5a6') for g in valid_genders.index]

wedges, texts, autotexts = ax1.pie(valid_genders.values,
                                   labels=[g.title() for g in valid_genders.index],
                                   autopct='%1.1f%%',
                                   colors=colors_gender,
                                   startangle=90,
                                   textprops={'fontsize': 12, 'fontweight': 'bold'})
ax1.set_title('Victim Gender Distribution', fontweight='bold', fontsize=14, pad=20)

# Age histogram
age_data = df['EDAD_VICTIMA_NUM'].dropna()
age_data = age_data[age_data <= 18]

ax2.hist(age_data, bins=18, range=(0, 18),
         color=colors['info'], edgecolor='white', linewidth=1, alpha=0.8)
ax2.set_xlabel('Age (years)', fontweight='bold')
ax2.set_ylabel('Number of Cases', fontweight='bold')
ax2.set_title('Victim Age Distribution', fontweight='bold', fontsize=14, pad=20)

mean_age = age_data.mean()
ax2.axvline(mean_age, color='red', linestyle='--', linewidth=2,
           label=f'Mean: {mean_age:.1f} years')
ax2.legend()

plt.tight_layout()
plt.savefig('chart_demographics.png', dpi=300, bbox_inches='tight')
plt.close()

# CHART 5: Executive Dashboard (for Slide 7)
print("5. Creating executive dashboard...")
fig = plt.figure(figsize=(16, 10))

# Calculate metrics
parent_cases = df[df['PARENTESCO FRENTE A LA VICTIMA'].isin(['madre', 'padre'])]
intrafamilial_rate = len(parent_cases) / len(df) * 100
multiple_abuse_cases = df[df['TOTAL_ABUSE_TYPES'] > 1]
multidimensional_index = len(multiple_abuse_cases) / len(df) * 100
psychological_cases = df[df['PSICOLOGICA'] == 'si']
psychological_universality = len(psychological_cases) / len(df) * 100
average_complexity = df['TOTAL_ABUSE_TYPES'].mean()

# 1. Abuse Types (Top Left)
ax1 = plt.subplot(2, 3, 1)
abuse_counts = [(df[col] == 'si').sum() for col in abuse_columns]
abuse_names = [col.title()[:4] for col in abuse_columns]

bars1 = ax1.bar(abuse_names, abuse_counts,
                color=[colors['danger'] if c > 300 else colors['warning'] if c > 100 else colors['primary']
                       for c in abuse_counts])
ax1.set_title('Types of Abuse', fontweight='bold')
ax1.set_ylabel('Cases')
for bar, val in zip(bars1, abuse_counts):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
            str(val), ha='center', fontweight='bold')

# 2. Gender Distribution (Top Middle)
ax2 = plt.subplot(2, 3, 2)
wedges, texts, autotexts = ax2.pie(valid_genders.values,
                                   labels=[g.title() for g in valid_genders.index],
                                   autopct='%1.1f%%',
                                   colors=colors_gender,
                                   startangle=90)
ax2.set_title('Victim Gender', fontweight='bold')

# 3. Age Distribution (Top Right)
ax3 = plt.subplot(2, 3, 3)
ax3.hist(age_data, bins=15, color=colors['info'], alpha=0.8, edgecolor='white')
ax3.set_title('Victim Age Distribution', fontweight='bold')
ax3.set_xlabel('Age')
ax3.axvline(age_data.mean(), color='red', linestyle='--', linewidth=2)

# 4. Top Aggressors (Bottom Left)
ax4 = plt.subplot(2, 3, 4)
top_aggressors = df['PARENTESCO FRENTE A LA VICTIMA'].value_counts()
top_aggressors = top_aggressors[~top_aggressors.index.isin(['no aplica', 'no'])].head(5)
bars4 = ax4.barh([a.title()[:10] for a in top_aggressors.index], top_aggressors.values,
                 color=[colors['danger'] if 'madre' in a or 'padre' in a else colors['warning']
                        for a in top_aggressors.index])
ax4.set_title('Top Aggressor Relations', fontweight='bold')
ax4.set_xlabel('Cases')

# 5. Multiple Abuse (Bottom Middle)
ax5 = plt.subplot(2, 3, 5)
bars5 = ax5.bar(abuse_distribution.index, abuse_distribution.values,
               color=[colors['success'] if x == 0 else
                      colors['warning'] if x <= 2 else
                      colors['danger'] for x in abuse_distribution.index])
ax5.set_title('Co-occurring Abuse Types', fontweight='bold')
ax5.set_xlabel('Number of Types')
ax5.set_ylabel('Cases')

# 6. Key Statistics (Bottom Right)
ax6 = plt.subplot(2, 3, 6)
ax6.axis('off')

stats_text = f"""KEY STATISTICS

📊 Total Cases: {len(df)}

🏠 Intrafamilial Rate:
   {intrafamilial_rate:.1f}%

🔄 Multiple Abuse:
   {multidimensional_index:.1f}%

🧠 Psychological Damage:
   {psychological_universality:.1f}%

📈 Avg Complexity:
   {average_complexity:.2f} types
"""

ax6.text(0.1, 0.5, stats_text, fontsize=11, va='center',
         bbox=dict(boxstyle='round', facecolor='lightgray', alpha=0.8),
         family='monospace', fontweight='bold')

plt.suptitle('Child Abuse in Palmira 2022: Executive Dashboard',
             fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig('chart_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ All charts generated successfully!")
print("\n📁 Generated files:")
print("   - chart_intrafamilial.png")
print("   - chart_multidimensional.png")
print("   - chart_psychological.png")
print("   - chart_demographics.png")
print("   - chart_dashboard.png")
print("\n🔧 Next steps:")
print("   1. Open presentacion_maltrato_palmira.html in browser")
print("   2. Replace [CHART PLACEHOLDER] sections with these images")
print("   3. Use browser dev tools or edit HTML directly")
print("   4. Presentation ready for use!")