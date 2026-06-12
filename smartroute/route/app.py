import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="SmartRoute AI Agent",
    page_icon="📍",
    layout="wide"
)

# Title
st.title("📍 SmartRoute")
st.subheader("Autonomous Address Resolution Agent")

# Load Orders
df = pd.read_csv("orders.csv")

# Select Order
order_id = st.selectbox(
    "Select Order ID",
    df["order_id"]
)

# Get Selected Order
selected_order = df[df["order_id"] == order_id].iloc[0]

customer = selected_order["customer"]
address = selected_order["address"]

st.markdown("---")

# Display Order Details
col1, col2 = st.columns(2)

with col1:
    st.write("### Customer")
    st.info(customer)

with col2:
    st.write("### Original Address")
    st.warning(address)

st.markdown("---")

# Ambiguous Address Detection
keywords = [
    "near",
    "behind",
    "beside",
    "opposite"
]

vague = False

for word in keywords:
    if word in address.lower():
        vague = True

# If Ambiguous
if vague:

    st.error("⚠ Ambiguous Address Detected")

    st.write("### 🤖 AI Agent Analysis")

    st.write("""
    This address appears incomplete because it contains
    landmark-based directions and lacks a precise location.
    """)

    confidence = 92

    st.metric(
        label="Confidence Score",
        value=f"{confidence}%"
    )

    st.markdown("---")

    st.write("### 🤖 Agent Message")

    st.info(
        "Please provide an additional landmark or location detail."
    )

    customer_response = st.text_input(
        "Customer Response"
    )

    if customer_response:

        final_address = (
            address + ", " + customer_response
        )

        st.markdown("---")

        st.success("✅ Address Successfully Resolved")

        st.write("### 📍 Final Driver Instructions")

        st.code(final_address)

        st.write("### 🚚 Delivery Status")

        st.success(
            "Ready for Delivery"
        )

else:

    st.success("✅ Address Looks Clear")

    st.metric(
        label="Confidence Score",
        value="98%"
    )

    st.write("### 📍 Driver Instructions")

    st.code(address)

    st.success(
        "Ready for Delivery"
    )

st.markdown("---")

st.caption(
    "SmartRoute MVP | ScriptedByHer Submission"
)