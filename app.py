import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales & Revenue Dashboard", layout="wide")

st.title("📊 Sales & Revenue Performance Dashboard")

# Load data
df = pd.read_csv('superstore_clean.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Sidebar filters
st.sidebar.header("Filters")
region_filter = st.sidebar.multiselect("Region", options=df['Region'].unique(), default=df['Region'].unique())
category_filter = st.sidebar.multiselect("Category", options=df['Category'].unique(), default=df['Category'].unique())

filtered_df = df[(df['Region'].isin(region_filter)) & (df['Category'].isin(category_filter))]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{filtered_df['Order ID'].nunique():,}")

# Monthly trend chart
monthly = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M').astype(str))['Sales'].sum().reset_index()
monthly.columns = ['Month', 'Sales']
fig1 = px.line(monthly, x='Month', y='Sales', title='Monthly Sales Trend', markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Category profit chart
cat_profit = filtered_df.groupby('Sub-Category')['Profit'].sum().sort_values().reset_index()
fig2 = px.bar(cat_profit, x='Profit', y='Sub-Category', orientation='h', title='Profit by Sub-Category',
              color='Profit', color_continuous_scale=['red', 'green'])
st.plotly_chart(fig2, use_container_width=True)

# Region breakdown
region_summary = filtered_df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
fig3 = px.bar(region_summary, x='Region', y=['Sales', 'Profit'], barmode='group', title='Sales & Profit by Region')
st.plotly_chart(fig3, use_container_width=True)