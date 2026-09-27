import streamlit as st

st.set_page_config(
    page_title="Candle AI Assistant",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Candle AI Assistant")
st.write("Demo Trading Analysis Tool")

st.divider()

st.subheader("Market")

pair = st.selectbox(
    "Select Pair",
    ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD"]
)

timeframe = st.selectbox(
    "Timeframe",
    ["1 Minute", "5 Minutes", "15 Minutes"]
)

st.divider()

st.subheader("AI Signal")

if st.button("🔍 Analyze 4 Candles", use_container_width=True):

    st.success("Analysis completed")

    st.metric(
        "Signal",
        "WAIT"
    )

    st.metric(
        "Confidence",
        "50%"
    )

    st.info(
        "Demo mode: candle analysis will be connected in the next step."
    )

st.divider()

st.caption("⚠️ Demo/research tool — not a guaranteed trading signal.")
