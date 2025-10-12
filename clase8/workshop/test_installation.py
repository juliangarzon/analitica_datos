"""
Test Installation Script
Class 8: Plotly + Streamlit
Universidad Cooperativa de Colombia

Purpose: Verify that all required libraries are installed correctly
Run this FIRST before starting the workshop
"""

import plotly.express as px
import pandas as pd
import streamlit as st

print("✅ All libraries installed successfully!")
print(f"Plotly version: {px.version}")
print(f"Pandas version: {pd.version}")
print(f"Streamlit version: {st.version}")
print("\n🎉 You're ready to start the workshop!")
