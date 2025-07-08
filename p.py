import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="🌲 Forest Energy Calculator",
    page_icon="🌿",
    layout="wide"
)

# ========== LOAD CSS ==========
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ========== LOTTIE ANIMATION ==========
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_forest = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")

lottie_bird = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_UJNc2t.json")
st_lottie(lottie_bird, height=120, speed=0.7, key="bird", loop=True)


# ========== HEADER ==========
st.markdown("<h1 class='custom-title'>⚡ Energy Metrics Analyzer ⚡</h1>", unsafe_allow_html=True)
# ========== MAIN UI ==========
col1, col2 = st.columns([1, 2])

with col1:
    st_lottie(lottie_forest, height=300, key="forest")

with col2:
    st.subheader("🌳 Enter your forest data below:")
    energy_input = st.slider("Tree density (per sq km)", 0, 1000, 250)
    carbon_input = st.slider("Carbon Sequestration Rate (kg/tree/year)", 0, 100, 20)
    area_input = st.number_input("Forest Area (sq km)", min_value=0.0, step=0.1)

    # ========== CALCULATION ==========
    if st.button("🌿 Calculate Energy"):
        total_trees = energy_input * area_input
        total_carbon = total_trees * carbon_input

        st.success(f"🌲 Total Trees: **{int(total_trees)}**")
        st.success(f"💨 Total Carbon Sequestration: **{total_carbon:.2f} kg/year**")

# ========== EXPANDERS ==========
with st.expander("🔍 About This App"):
    st.write("""
        This Forest Energy Calculator estimates carbon sequestration based on tree density and area.
        Developed with ❤️ using Streamlit, styled for nature lovers 🌿
    """)

with st.expander("📊 Future Features"):
    st.write("- Satellite image integration\n- Real-time CO2 data\n- Forecasting tools")

with st.container():
    st.markdown("<div style='animation: fadeIn 1s ease; font-size: 20px;'>", unsafe_allow_html=True)
    st.success(f"🌲 Total Trees: **{int(total_trees)}**")
    st.success(f"💨 Total Carbon Sequestration: **{total_carbon:.2f} kg/year**")
    st.markdown("</div>", unsafe_allow_html=True)

