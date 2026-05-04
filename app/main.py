import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import plotly.graph_objects as go

from core.uncertainty import compute_range
from core.explanations import generate_summary, get_learn_more_points

# --- Page setup ---
st.set_page_config(
    page_title="The ± Behind the %",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Sidebar (Presets) ---
st.sidebar.title("Presets")
preset = st.sidebar.selectbox(
    "Choose an example",
    [
        "None",
        "Packaging reduction claim",
        "Transport efficiency claim",
        "Fertiliser reduction claim",
        "Energy efficiency claim",
        "Feed conversion improvement"
    ]
)

if preset == "Packaging reduction claim":
    reported_percent = 20
    uncertainty_level = "High"
elif preset == "Transport efficiency claim":
    reported_percent = 35
    uncertainty_level = "Medium"
elif preset == "Fertiliser reduction claim":
    reported_percent = 50
    uncertainty_level = "High"
elif preset == "Energy efficiency claim":
    reported_percent = 15
    uncertainty_level = "Medium"
elif preset == "Feed conversion improvement":
    reported_percent = 10
    uncertainty_level = "High"
else:
    reported_percent = None
    uncertainty_level = None

# --- Title block ---
st.markdown(
    """
    <div style="text-align: center; margin-bottom: 1rem;">
        <h1 style="margin-bottom: 0.2rem;">The ± Behind the %</h1>
        <p style="color: #555; font-size: 1.05rem;">
            A teaching tool for exploring uncertainty in percentage‑based environmental claims.
        </p>
        <span style="font-size: 0.9rem; color: #888;">ℹ️ Use presets for quick examples, or enter your own values below.</span>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Input section ---
st.subheader("Inputs")

col1, col2 = st.columns(2)

with col1:
    reported_percent = st.number_input(
        "Reported reduction (%)",
        min_value=0,
        max_value=100,
        value=reported_percent if reported_percent is not None else 30
    )

with col2:
    uncertainty_level = st.selectbox(
        "Uncertainty level",
        ["Low", "Medium", "High"],
        index=["Low", "Medium", "High"].index(
            uncertainty_level if uncertainty_level is not None else "Medium"
        ),
        help="These represent wide illustrative uncertainty bands: ±25, ±50, or ±75 percentage points."
    )

mode = st.radio(
    "Display mode",
    ["Relative", "Absolute"],
    horizontal=True
)

st.markdown("---")

# --- Compute plausible range ---
lower, upper = compute_range(reported_percent, uncertainty_level, mode)

# --- Visualisation section ---
st.subheader("Plausible range")

# Elegant range label
st.markdown(
    f"<p style='text-align:center; color:#666;'>Range: <strong>{lower}%</strong> to <strong>{upper}%</strong></p>",
    unsafe_allow_html=True
)

fig = go.Figure()

# Plausible range bar
fig.add_trace(go.Bar(
    x=[upper - lower],
    y=[""],
    base=lower,
    orientation="h",
    marker=dict(color="#88BDE6"),
    hoverinfo="skip",
    showlegend=False
))

# Reported % marker
fig.add_trace(go.Scatter(
    x=[reported_percent],
    y=[""],
    mode="markers",
    marker=dict(size=18, color="#1F78B4", line=dict(width=1, color="black")),
    name="Reported %",
    hovertemplate="Reported: %{x}%<extra></extra>"
))

# Layout
fig.update_layout(
    height=150,
    margin=dict(l=20, r=20, t=10, b=10),
    xaxis=dict(
        range=[0, 100],
        title="Percentage reduction (%)",
        tickmode="linear",
        dtick=10,
        gridcolor="#EEE"
    ),
    yaxis=dict(showticklabels=False),
    transition=dict(duration=300)
)

st.plotly_chart(fig, use_container_width=True)

# --- Explanation section ---
st.subheader("Explanation")
summary = generate_summary(reported_percent, lower, upper)
st.write(summary)

# --- Learn more section ---
with st.expander("Learn more"):
    for point in get_learn_more_points():
        st.write(f"- {point}")

# --- Why uncertainty matters ---
with st.expander("Why uncertainty matters"):
    st.write(
        "Percentage reductions are often interpreted as precise, but they rarely are. "
        "Environmental systems are complex, data sources vary in quality, and modelling "
        "choices can shift results substantially. Understanding uncertainty helps avoid "
        "overconfidence and encourages more informed decision‑making."
    )

# --- About section ---
with st.expander("About this tool"):
    st.write(
        "This tool is designed for teaching purposes. It illustrates how wide uncertainty bands "
        "can be when interpreting percentage-based environmental claims. It does not calculate "
        "statistical confidence intervals or perform life cycle assessment."
    )

# --- Reset button ---
st.markdown("---")
if st.button("Reset"):
    st.rerun()

# --- Footer ---
st.markdown(
    """
    <p style='font-size: 0.8rem; color: #777; text-align: center; margin-top: 2rem;'>
        © 2026 — The ± Behind the %. Built for teaching uncertainty literacy.
    </p>
    """,
    unsafe_allow_html=True
)