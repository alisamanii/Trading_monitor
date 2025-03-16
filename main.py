import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


@st.cache_data
def get_stock_data():
    timestamps = pd.date_range(start="2024-02-01", periods=100, freq="min")
    prices = np.cumsum(np.random.randn(100) * 0.5 + 0.5) + 100
    return pd.DataFrame({"time": timestamps, "price": prices})


st.set_page_config(page_title="Live Stock Price", layout="wide")

with open("trade/title.html", "r", encoding="utf-8") as file:
    title_html = file.read()
with open("trade/title2.html", "r", encoding="utf-8") as file:
    title_html2 = file.read()

st.html(title_html)
st.html(title_html2)

data = get_stock_data()


fig = go.Figure()
fig.add_trace(go.Candlestick(
    x=data["time"],
    open=data["price"] - np.random.rand(len(data)) * 0.5,
    high=data["price"] + np.random.rand(len(data)) * 0.5,
    low=data["price"] - np.random.rand(len(data)) * 0.5,
    close=data["price"],
    name="price"
))

fig.update_layout(
    title="Trading Monitor",
    xaxis_title="time",
    yaxis_title="price",
    xaxis_rangeslider_visible=False,
    template="plotly_dark",
    height=600,
)


st.plotly_chart(fig, use_container_width=True,key="sdfsd")
url="trade/trade.mp4"
st.video(url,autoplay=True,loop=100)


