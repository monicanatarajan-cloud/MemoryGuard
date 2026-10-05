import streamlit as st
import pandas as pd
import joblib

# ============================================================
# PAGE SETUP
# ============================================================

st.set_page_config(
    page_title="MemoryGuard",
    page_icon="🧠",
    layout="wide"
)

# ============================================================
# LOAD MODEL
# ============================================================

MODEL_FILE = "memoryguard_9feature_model.pkl"

try:
    model_data = joblib.load(MODEL_FILE)
    model = model_data["model"]
    features = model_data["features"]
    model_loaded = True
except Exception as e:
    model_loaded = False
    model = None
    features = []
    load_error = str(e)

# ============================================================
# HEADER
# ============================================================

st.title("🧠 MemoryGuard")
st.subheader("AI-Powered Early Cognitive Decline Risk Stratification")

st.write(
    "MemoryGuard compares current and previous cognitive assessments "
    "to identify changes over time and provide AI-assisted risk stratification."
)

if model_loaded:
    st.success("🤖 AI model loaded successfully.")
else:
    st.error("AI model could not be loaded.")
    st.code(load_error)
    st.stop()

st.divider()

# ============================================================
# PATIENT INFORMATION
# ============================================================

st.header("👤 Patient Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=None,
        placeholder="Enter age"
    )

with col2:
    sex = st.selectbox(
        "Sex",
        ["Select", "Female", "Male"]
    )

with col3:
    hand = st.selectbox(
        "Handedness",
        ["Select", "Left", "Right"]
    )

# ============================================================
# CURRENT ASSESSMENT
# ============================================================

st.header("🧠 Current Assessment")

col1, col2 = st.columns(2)

with col1:
    st.write("**MMSE**")
    st.caption("Mini-Mental State Examination")

    mmse = st.number_input(
        "Current MMSE",
        min_value=0.0,
        max_value=30.0,
        value=None,
        placeholder="Enter current MMSE",
        step=1.0
    )

with col2:
    st.write("**CDR**")
    st.caption("Clinical Dementia Rating")

    cdr = st.number_input(
        "Current CDR",
        min_value=0.0,
        max_value=3.0,
        value=None,
        placeholder="Enter current CDR",
        step=0.5
    )

# ============================================================
# PREVIOUS ASSESSMENT
# ============================================================

st.header("📅 Previous Assessment")

col1, col2 = st.columns(2)

with col1:
    previous_mmse = st.number_input(
        "Previous MMSE",
        min_value=0.0,
        max_value=30.0,
        value=None,
        placeholder="Enter previous MMSE",
        step=1.0
    )

with col2:
    previous_cdr = st.number_input(
        "Previous CDR",
        min_value=0.0,
        max_value=3.0,
        value=None,
        placeholder="Enter previous CDR",
        step=0.5
    )

# ============================================================
# AUTOMATIC CHANGE CALCULATION
# ============================================================

st.header("📊 Assessment Changes")

if mmse is not None and previous_mmse is not None:
    mmse_change = mmse - previous_mmse
else:
    mmse_change = None

if cdr is not None and previous_cdr is not None:
    cdr_change = cdr - previous_cdr
else:
    cdr_change = None

col1, col2 = st.columns(2)

with col1:
    if mmse_change is not None:
        st.metric(
            "MMSE Change",
            f"{mmse_change:.2f}"
        )
    else:
        st.metric("MMSE Change", "—")

with col2:
    if cdr_change is not None:
        st.metric(
            "CDR Change",
            f"{cdr_change:.2f}"
        )
    else:
        st.metric("CDR Change", "—")

st.caption(
    "Change values are automatically calculated from current and previous assessments."
)

# ============================================================
# ANALYZE BUTTON
# ============================================================

st.divider()

analyze = st.button(
    "🔍 Analyze Risk",
    type="primary",
    use_container_width=True
)

# ============================================================
# ANALYSIS
# ============================================================

if analyze:

    missing = []

    if age is None:
        missing.append("Age")

    if sex == "Select":
        missing.append("Sex")

    if hand == "Select":
        missing.append("Handedness")

    if mmse is None:
        missing.append("Current MMSE")

    if cdr is None:
        missing.append("Current CDR")

    if previous_mmse is None:
        missing.append("Previous MMSE")

    if previous_cdr is None:
        missing.append("Previous CDR")

    if missing:
        st.warning(
            "Please enter: " + ", ".join(missing)
        )
        st.stop()

    # ========================================================
    # ENCODING
    # ========================================================

    sex_encoded = 1 if sex == "Male" else 0
    hand_encoded = 1 if hand == "Right" else 0

    # ========================================================
    # MODEL INPUT
    # ========================================================

    input_data = pd.DataFrame({
        "Age": [age],
        "MMSE": [mmse],
        "CDR": [cdr],
        "Previous_MMSE": [previous_mmse],
        "Previous_CDR": [previous_cdr],
        "MMSE_Change": [mmse_change],
        "CDR_Change": [cdr_change],
        "Sex_Encoded": [sex_encoded],
        "Hand_Encoded": [hand_encoded]
    })

    input_data = input_data[features]

    # ========================================================
    # PREDICTION
    # ========================================================

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    labels = {
        0: "Nondemented",
        1: "Demented",
        2: "Converted"
    }

    prediction_label = labels.get(
        int(prediction),
        str(prediction)
    )

    # ========================================================
    # RESULT
    # ========================================================

    st.divider()

    st.header("🧠 AI Risk Assessment Result")

    result1, result2 = st.columns(2)

    with result1:
        st.subheader("AI Classification")

        st.info(
            f"### {prediction_label}"
        )

        st.write(
            "The model classified the entered assessment "
            f"under the **{prediction_label}** category."
        )

    with result2:
        st.subheader("Model Confidence")

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    # ========================================================
    # SUMMARY
    # ========================================================

    st.header("📋 Assessment Summary")

    summary1, summary2, summary3 = st.columns(3)

    with summary1:
        st.write(f"**Age:** {age}")
        st.write(f"**Sex:** {sex}")
        st.write(f"**Hand:** {hand}")

    with summary2:
        st.write(f"**Current MMSE:** {mmse:.1f}")
        st.write(f"**Previous MMSE:** {previous_mmse:.1f}")
        st.write(f"**MMSE Change:** {mmse_change:.2f}")

    with summary3:
        st.write(f"**Current CDR:** {cdr:.1f}")
        st.write(f"**Previous CDR:** {previous_cdr:.1f}")
        st.write(f"**CDR Change:** {cdr_change:.2f}")

    # ========================================================
    # COGNITIVE TREND
    # ========================================================

    st.divider()

    st.header("📈 Cognitive Trend")

    chart1, chart2 = st.columns(2)

    with chart1:
        st.subheader("MMSE Trend")

        mmse_chart = pd.DataFrame({
            "Assessment": ["Previous", "Current"],
            "MMSE": [previous_mmse, mmse]
        })

        st.line_chart(
            mmse_chart.set_index("Assessment")
        )

        if mmse_change < 0:
            st.warning(
                f"MMSE decreased by {abs(mmse_change):.2f} points."
            )
        elif mmse_change > 0:
            st.success(
                f"MMSE increased by {mmse_change:.2f} points."
            )
        else:
            st.info("MMSE remained stable.")

    with chart2:
        st.subheader("CDR Trend")

        cdr_chart = pd.DataFrame({
            "Assessment": ["Previous", "Current"],
            "CDR": [previous_cdr, cdr]
        })

        st.line_chart(
            cdr_chart.set_index("Assessment")
        )

        if cdr_change > 0:
            st.warning(
                f"CDR increased by {cdr_change:.2f}."
            )
        elif cdr_change < 0:
            st.success(
                f"CDR decreased by {abs(cdr_change):.2f}."
            )
        else:
            st.info("CDR remained stable.")

    # ========================================================
    # PERSONAL COGNITIVE FINGERPRINT
    # ========================================================

    st.divider()

    st.header("🧬 Personal Cognitive Fingerprint")

    st.write(
        "MemoryGuard compares the current assessment with "
        "the patient's previous personal baseline."
    )

    fp1, fp2, fp3, fp4 = st.columns(4)

    with fp1:
        st.metric(
            "Previous MMSE",
            f"{previous_mmse:.1f}"
        )

    with fp2:
        st.metric(
            "Current MMSE",
            f"{mmse:.1f}"
        )

    with fp3:
        st.metric(
            "Previous CDR",
            f"{previous_cdr:.1f}"
        )

    with fp4:
        st.metric(
            "Current CDR",
            f"{cdr:.1f}"
        )

    # ========================================================
    # CONTRIBUTING FACTORS
    # ========================================================

    st.header("🔎 Contributing Factors")

    factors = []

    if mmse_change < 0:
        factors.append(
            f"MMSE decreased by {abs(mmse_change):.2f} points."
        )
    elif mmse_change > 0:
        factors.append(
            f"MMSE increased by {mmse_change:.2f} points."
        )
    else:
        factors.append(
            "MMSE remained stable."
        )

    if cdr_change > 0:
        factors.append(
            f"CDR increased by {cdr_change:.2f}."
        )
    elif cdr_change < 0:
        factors.append(
            f"CDR decreased by {abs(cdr_change):.2f}."
        )
    else:
        factors.append(
            "CDR remained stable."
        )

    factors.append(
        f"Assessment age: {age} years."
    )

    for factor in factors:
        st.write("• " + factor)

    # ========================================================
    # COGNITIVE DIGITAL TIMELINE
    # ========================================================

    st.divider()

    st.header("🕒 Cognitive Digital Timeline")

    timeline = pd.DataFrame({
        "Visit": [
            "Previous Assessment",
            "Current Assessment"
        ],
        "MMSE": [
            previous_mmse,
            mmse
        ],
        "CDR": [
            previous_cdr,
            cdr
        ]
    })

    st.dataframe(
        timeline,
        use_container_width=True,
        hide_index=True
    )

    # ========================================================
    # SUPPORTIVE GUIDANCE
    # ========================================================

    st.header("💡 Supportive Guidance")

    guidance1, guidance2 = st.columns(2)

    with guidance1:
        st.subheader("Lifestyle Support")

        st.write("• Maintain regular physical activity.")
        st.write("• Engage in mentally stimulating activities.")
        st.write("• Maintain regular sleep and daily routines.")
        st.write("• Stay socially engaged.")

    with guidance2:
        st.subheader("Clinical Follow-up")

        if mmse_change < 0 or cdr_change > 0:
            st.warning(
                "A change is present compared with the previous "
                "assessment. Consider discussing the changes with "
                "a qualified healthcare professional."
            )
        else:
            st.info(
                "Continue regular monitoring and discuss concerns "
                "with a qualified healthcare professional."
            )

    # ========================================================
    # MODEL PROBABILITIES
    # ========================================================

    st.divider()

    st.header("📊 Model Prediction Probabilities")

    probability_data = pd.DataFrame({
        "Category": [
            "Nondemented",
            "Demented",
            "Converted"
        ],
        "Probability": [
            probabilities[0] * 100,
            probabilities[1] * 100,
            probabilities[2] * 100
        ]
    })

    probability_data["Probability"] = probability_data[
        "Probability"
    ].round(2)

    st.bar_chart(
        probability_data.set_index("Category")
    )

    # ========================================================
    # DISCLAIMER
    # ========================================================

    st.divider()

    st.warning(
        "⚠️ This result is an AI-assisted classification and "
        "is not a medical diagnosis. MemoryGuard is designed "
        "to support healthcare professionals and should not "
        "replace clinical judgment."
    )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "MemoryGuard | AI-assisted cognitive risk stratification "
    "and longitudinal decision support"
)
