# 🎓 CLASS 8 WORKSHOP FILES

Welcome to the hands-on workshop for Plotly + Streamlit!

This folder contains all the code files you'll create during the 4-hour class.

---

## 📁 Files Overview

### ✅ Setup & Testing
- **`test_installation.py`** - Verify all libraries are installed
  - Run this FIRST before starting!
  - Command: `python test_installation.py`

---

### 📊 Part 1: Plotly Basics (Files 01-02)

**`01_first_chart.py`** - Your first interactive chart
- Learn: Creating a scatter plot in 3 lines of code
- Time: 5 minutes
- Run: `python 01_first_chart.py`

**`02_six_charts.py`** - The 6 essential chart types
- Learn: Scatter, Line, Bar, Box, Histogram, Treemap
- Time: 30 minutes
- Run: `python 02_six_charts.py`

---

### 🎨 Part 2: Customization (Files 03-04)

**`03_customization.py`** - Professional styling
- Learn: Before/After comparison, themes, layouts
- Time: 20 minutes
- Run: `python 03_customization.py`

**`04_subplots.py`** - Multiple charts in one figure
- Learn: Creating dashboard-style multi-panel views
- Time: 25 minutes
- Run: `python 04_subplots.py`

---

### ⚡ Part 3: Advanced Interactivity (Files 05-07)

**`05_hover_advanced.py`** - Custom hover tooltips
- Learn: Formatting hover information
- Time: 15 minutes
- Run: `python 05_hover_advanced.py`

**`06_dropdown.py`** - Interactive dropdown menus
- Learn: Adding controls to switch between views
- Time: 20 minutes
- Run: `python 06_dropdown.py`

**`07_animation.py`** - Animated charts with time slider
- Learn: Creating animated visualizations
- Time: 20 minutes
- Run: `python 07_animation.py`

---

### 🌐 Part 4-5: Streamlit Dashboards (Files 08-10)

**`app_basic.py`** - Your first web dashboard ⭐
- Learn: Converting charts to web apps
- Time: 10 minutes
- Run: `streamlit run app_basic.py`
- Opens in browser automatically!

**`streamlit_components.py`** - Component reference
- Learn: All Streamlit widgets and layouts
- Time: 20 minutes
- Run: `streamlit run streamlit_components.py`

**`dashboard_complete.py`** - Full-featured dashboard ⭐⭐
- Learn: Building production-ready dashboards
- Time: 30 minutes
- Run: `streamlit run dashboard_complete.py`

---

### 🎯 Part 6: Your Project

**`my_project_template.py`** - Template for your homework 📝
- Your assignment: Adapt this for YOUR data
- Includes: TODOs and checklist
- Run: `streamlit run my_project_template.py`

---

## 🚀 Quick Start Guide

### Step 1: Verify Installation
```bash
python test_installation.py
```

### Step 2: Try Your First Chart
```bash
python 01_first_chart.py
```

### Step 3: Create Your First Web App
```bash
streamlit run app_basic.py
```

---

## 📚 Learning Path

### Beginner Path (2 hours)
1. `test_installation.py`
2. `01_first_chart.py`
3. `02_six_charts.py`
4. `app_basic.py`
5. `my_project_template.py`

### Complete Path (4 hours - Full Class)
Follow all files in order 01 → 10

### Quick Reference Path
- Need a chart? → `02_six_charts.py`
- Need styling? → `03_customization.py`
- Need Streamlit widgets? → `streamlit_components.py`

---

## 💡 Tips for Workshop

### For Each File:
1. **Read the docstring** at the top (explains what you'll learn)
2. **Run the code** to see it in action
3. **Modify something** to experiment
4. **Try with your data** if applicable

### When You Get Stuck:
1. Read the error message completely
2. Check column names with `df.columns`
3. Verify data types with `df.dtypes`
4. Ask for help!

### Common Commands:
```bash
# Run Python scripts
python filename.py

# Run Streamlit apps
streamlit run filename.py

# Stop Streamlit app
Ctrl + C (in terminal)

# Check installed packages
pip list

# Reinstall if needed
pip install plotly pandas streamlit
```

---

## 📊 Homework Assignment

**Due:** [Next class date]

**File to modify:** `my_project_template.py`

**Requirements:**
- ✅ 5+ interactive Plotly charts
- ✅ 4 metrics/KPIs
- ✅ 3+ functional filters
- ✅ Organized in tabs
- ✅ Uses YOUR project data

**Submission:**
- Rename to: `yourlastname_dashboard.py`
- Include your data file (if local)
- Add a brief README.txt

---

## 🎯 Learning Objectives Checklist

By the end of this workshop, you should be able to:

### Plotly Skills
- [ ] Create 6 types of interactive charts
- [ ] Customize colors, titles, and layouts
- [ ] Add hover tooltips
- [ ] Create subplots (multi-chart figures)
- [ ] Add animations and dropdowns

### Streamlit Skills
- [ ] Build a basic web dashboard
- [ ] Add interactive filters (slider, multiselect)
- [ ] Display metrics and KPIs
- [ ] Organize content with tabs and columns
- [ ] Cache data for performance
- [ ] Deploy Plotly charts in Streamlit

### Project Skills
- [ ] Choose appropriate chart types for data
- [ ] Design user-friendly interfaces
- [ ] Apply these skills to your own project

---

## 📖 Additional Resources

### Documentation
- **Plotly:** https://plotly.com/python/
- **Streamlit:** https://docs.streamlit.io/
- **Pandas:** https://pandas.pydata.org/docs/

### Galleries
- **Plotly Examples:** https://plotly.com/python/
- **Streamlit Gallery:** https://streamlit.io/gallery

### Help
- Refer to `clase8_manual.md` for detailed step-by-step instructions
- Check the cheatsheet at the end of the manual
- Ask questions during office hours

---

## 🗂️ File Organization

```
workshop/
├── README.md                      ← You are here!
│
├── test_installation.py           ← Start here
│
├── 01_first_chart.py             ← Part 1: Plotly basics
├── 02_six_charts.py              │
│
├── 03_customization.py           ← Part 2: Styling
├── 04_subplots.py                │
│
├── 05_hover_advanced.py          ← Part 3: Interactivity
├── 06_dropdown.py                │
├── 07_animation.py               │
│
├── app_basic.py                  ← Part 4-5: Streamlit
├── streamlit_components.py       │
├── dashboard_complete.py         │
│
└── my_project_template.py        ← Part 6: Your homework
```

---

## ⚡ Quick Reference

### Chart Selection
- **Relationships?** → Scatter
- **Time series?** → Line
- **Compare categories?** → Bar
- **Distribution?** → Histogram or Box
- **Hierarchy?** → Treemap

### Streamlit Widgets
- **Choose one:** `st.selectbox()` or `st.radio()`
- **Choose many:** `st.multiselect()`
- **Number range:** `st.slider()`
- **Yes/No:** `st.checkbox()`
- **Text:** `st.text_input()`

### Common Patterns
```python
# Cache data loading
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

# Create columns
col1, col2, col3 = st.columns(3)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
```

---

## 🎉 Ready to Start?

1. Run `python test_installation.py`
2. Open `01_first_chart.py`
3. Follow along with the class!

**Good luck and have fun building awesome dashboards! 🚀**

---

*Workshop materials for Class 8: Plotly + Streamlit*
*Universidad Cooperativa de Colombia - Data Analytics*
*Prof. Julian Eduardo Garzon Giraldo, MsC*
