# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 13:58:26 2025

@author: hperr

real-world scenario differences
- needs hosting: do not want dashboard to be public
- needs API to pull data 
- need data storage


"""

# marketing_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="Marketing Dashboard", layout="wide")

# --- Title ---
st.title("📊 Marketing Performance Dashboard")

#%% import data
## --- Load CSV from GitHub ---
#csv_url = "https://github.com/nailson/ifood-data-business-analyst-test/blob/master/ifood_df.csv"
#@st.cache_data
#def load_data(url):
#    return pd.read_csv(url, delimiter=",", error_bad_lines=False, engine="python")

#df = load_data(csv_url)

#%% generate fake data
# Generate 30 days of data
np.random.seed(42)
dates = pd.date_range(end=pd.Timestamp.today(), periods=90)
campaigns = ["Spring Launch", "Retargeting Blast", "Brand Awareness", "Promo Boost"]

data = []
for date in dates:
    for campaign in campaigns:
        impressions = np.random.randint(5000, 20000)
        clicks = np.random.randint(100, 800)
        spend = round(np.random.uniform(100, 500), 2)
        ctr = round(clicks / impressions, 4)
        conversions = np.random.randint(5, 50)
        cpc = round(spend / clicks, 2)

        data.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Campaign Name": campaign,
            "Ad Spend": spend,
            "Impressions": impressions,
            "Clicks": clicks,
            "CTR": ctr,
            "Conversions": conversions,
            "CPC": cpc
        })

facebook = pd.DataFrame(data)

#%% chart 1

# --- Basic KPIs ---
total_spend = facebook["Ad Spend"].sum()
total_clicks = facebook["Clicks"].sum()
avg_ctr = facebook["CTR"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Ad Spend", f"${total_spend:,.2f}")
col2.metric("Total Clicks", f"{total_clicks:,}")
col3.metric("Avg. CTR", f"{avg_ctr:.2%}")

# --- Line Chart: CTR over Time ---
if "Date" in facebook.columns:
    facebook["Date"] = pd.to_datetime(facebook["Date"])
    fig = px.line(facebook, x="Date", y="CTR", title="Click-Through Rate Over Time")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("No 'Date' column found in the dataset.")

#%% add table view
    
# --- Optional: Table View ---
with st.expander("🔍 View Raw Data"):
    st.dataframe(df)