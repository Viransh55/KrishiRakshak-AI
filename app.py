import streamlit as st
import joblib

# -----------------------------
# PAGE SETTINGS
# -----------------------------

st.set_page_config(
    page_title="KrishiRakshak AI",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.block-container{
    padding-top: 0.5rem;
    padding-bottom: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

img{
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# BANNER
# -----------------------------

st.image(
    "banner.png",
    use_container_width=True
)

# -----------------------------
# LOAD MODELS
# -----------------------------

crop_model = joblib.load("crop_model.pkl")
irrigation_model = joblib.load("irrigation_model.pkl")

st.divider()

# -----------------------------
# INPUTS
# -----------------------------

st.subheader("🌱 Field Parameters")
st.caption("Enter real-time sensor values collected from the field")

col1, col2, col3 = st.columns(3)

with col1:
    moisture = st.number_input(
        "Soil Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

with col2:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=0.0,
        step=1.0
    )

with col3:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

# -----------------------------
# ANALYZE BUTTON
# -----------------------------

if st.button("🔍 Analyze Field", use_container_width=True):

    crop = crop_model.predict(
        [[moisture, temperature, humidity]]
    )[0]

    irrigation = irrigation_model.predict(
        [[moisture, temperature, humidity]]
    )[0]

    # Dryness Risk

    if moisture < 25:
        dryness = "HIGH 🔴"
    elif moisture < 40:
        dryness = "MEDIUM 🟡"
    else:
        dryness = "LOW 🟢"

    # Field Condition

    if moisture < 25:
        condition = "Poor ❌"
    elif moisture < 50:
        condition = "Moderate ⚠️"
    else:
        condition = "Healthy ✅"

    st.divider()

    st.subheader("📊 Analysis Results")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"🌱 Recommended Crop: {crop}"
        )

        if irrigation == 1:
            st.warning(
                "💧 Irrigation Required"
            )
        else:
            st.success(
                "✅ Irrigation Not Required"
            )

    with col2:

        st.info(
            f"🌾 Dryness Risk: {dryness}"
        )

        st.info(
            f"🌿 Field Condition: {condition}"
        )

    st.divider()

    st.subheader("🤖 AI Suggestions")

    if moisture < 25:

        st.error(
            "Immediate irrigation is recommended because soil moisture is critically low."
        )

    elif moisture < 40:

        st.warning(
            "Monitor the field regularly. Irrigation may be required soon."
        )

    else:

        st.success(
            "Soil moisture is healthy. Continue normal monitoring."
        )

    if temperature > 35:

        st.warning(
            "High temperature detected. Crops may require additional watering."
        )

    if humidity < 40:

        st.warning(
            "Low humidity detected. Risk of soil drying is increased."
        )

st.divider()

st.caption(
    "🚜 KrishiRakshak AI | Smart Agriculture Assistant"
)