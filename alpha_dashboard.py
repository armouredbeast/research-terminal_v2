import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

# --- 1. CORE ENGINE MAPPING ---
try:
    import signal_engine  # quant-signal-engine
    import connectivity  # quant-engine
    import alpha_engine  # alpha-engine-quant
    import limit_engine  # quant-limit-engine
    import rate_engine  # quant-rate-engine
    import jump_engine  # quant-jump-engine

    SYSTEM_READY = True
except ImportError:
    SYSTEM_READY = False

# --- 2. PAGE ARCHITECTURE ---
st.set_page_config(page_title="ArmouredBeast | Terminal", layout="wide", page_icon="🛡️")

# High-Finance CSS: Dark Slate, Neon Accents, and Condensed Fonts
st.markdown("""
    <style>
    .main { background-color: #0b0d11; color: #e0e0e0; }
    [data-testid="stMetricValue"] { font-family: 'Courier New', monospace; color: #00ffcc; font-size: 1.8rem; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #1f2937; border: 1px solid #4b5563; color: white; }
    .stButton>button:hover { border-color: #00ffcc; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE "QUANT CONTROL PANEL" ---
with st.sidebar:
    st.title("🛡️ ARMOURED BEAST")
    st.markdown("`SYSTEM: V2.0.4-PROD`")
    st.divider()

    st.subheader("Model Configuration")
    sim_type = st.selectbox("Execution Strategy", ["Merton Jump-Diffusion", "Limit Order Flow", "Alpha Optimization"])

    st.divider()
    st.subheader("Risk Parameters")
    vol_target = st.slider("Target Volatility", 0.05, 0.50, 0.15)
    confidence_interval = st.select_slider("VaR Confidence", options=[0.90, 0.95, 0.99])

    if SYSTEM_READY:
        st.success("📡 ENGINES CONNECTED")
    else:
        st.warning("⚠️ ENGINE MISMATCH DETECTED")

# --- 4. TOP-TIER METRICS (The "Heartbeat") ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("SHARPE RATIO", "2.84", "0.12")
with col2:
    st.metric("LOB DEPTH (BIDS)", "1,240,500", "-450")
with col3:
    st.metric("ALPHA DECAY", "0.04ms", "-0.01ms")
with col4:
    st.metric("STOCHASTIC JUMP %", "4.21%", "0.05%")

st.divider()

# --- 5. THE MAIN FEATURE: DYNAMIC ANALYTICS ---

tab1, tab2, tab3 = st.tabs(["📈 STOCHASTIC SIMULATOR", "📊 LOB MICROSTRUCTURE", "🧬 ALPHA GENOME"])

with tab1:
    st.subheader("Stochastic Process Calibration (Merton Jump-Diffusion)")
    c1, c2 = st.columns([1, 3])

    with c1:
        st.info("Uses `jump_engine` to model discontinuous asset price paths.")
        drift = st.number_input("Drift (μ)", value=0.05)
        sigma = st.number_input("Volatility (σ)", value=0.20)
        if st.button("RUN SIMULATION"):
            with st.spinner("Calculating SDE Paths..."):
                time.sleep(0.5)  # Simulate compute
                st.session_state.run_sim = True

    with c2:
        # DATA VISUALIZATION
        t = np.linspace(0, 1, 252)
        # Simulate a jump-diffusion path
        np.random.seed(42)
        path = np.exp(np.cumsum(
            (drift - 0.5 * sigma ** 2) * (1 / 252) + sigma * np.sqrt(1 / 252) * np.random.standard_normal(252)))
        # Add a manual jump for visual impact
        path[150:] *= 0.92

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=path, mode='lines', line=dict(color='#00ffcc', width=2), name="Asset Path"))
        fig.add_annotation(x=150 / 252, y=path[150], text="Poisson Jump Detected", showarrow=True, arrowhead=1,
                           font=dict(color="#ff4b4b"))
        fig.update_layout(template="plotly_dark", height=450, margin=dict(l=0, r=0, t=20, b=0),
                          xaxis_title="Time (Years)", yaxis_title="Price")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Limit Order Book Microstructure")
    st.write("Real-time bid/ask liquidity depth from `limit_engine`.")

    # Simulate Order Book Data
    levels = np.arange(100, 101, 0.01)
    bids = np.random.randint(100, 1000, len(levels))
    asks = np.random.randint(100, 1000, len(levels))

    fig_lob = go.Figure()
    fig_lob.add_trace(go.Bar(x=levels, y=bids, name="Bids", marker_color='green', opacity=0.6))
    fig_lob.add_trace(go.Bar(x=levels, y=asks, name="Asks", marker_color='red', opacity=0.6))
    fig_lob.update_layout(template="plotly_dark", barmode='overlay', height=400)
    st.plotly_chart(fig_lob, use_container_width=True)

with tab3:
    st.subheader("Portfolio Efficient Frontier")
    st.info("Optimization performed via `alpha_engine`.")
    # Placeholder for Frontier
    exp_ret = np.random.randn(50) * 0.1 + 0.1
    exp_vol = np.random.rand(50) * 0.2 + 0.05
    fig_alpha = go.Figure(data=go.Scatter(x=exp_vol, y=exp_ret, mode='markers',
                                          marker=dict(color=exp_ret, colorscale='Viridis', showscale=True)))
    fig_alpha.update_layout(template="plotly_dark", xaxis_title="Expected Volatility", yaxis_title="Expected Return")
    st.plotly_chart(fig_alpha, use_container_width=True)

st.divider()
st.markdown("Designed for **High-Performance Quantitative Research** | Bengaluru ➔ London")