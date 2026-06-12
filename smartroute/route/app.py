import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SmartRoute",
    page_icon="📍"
)

st.title("📍 SmartRoute")
st.subheader("Autonomous Address Resolution Agent")

# Sample Data (No CSV Required)
df = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer": ["Ramesh", "Sita", "Ravi", "Anjali", "Kiran"],
    "address": [
        "Behind old water tank near Hanuman temple",
        "H.No 2-45 Main Road Vizag",
        "Blue gate beside ration shop",
        "Door No 5-12 Gandhi Road Visakhapatnam",
        "Near bus stand opposite school"
    ]
})

order_id = st.selectbox(
    "Select Order ID",
    df["order_id"]
)

selected = df[df["order_id"] == order_id].iloc[0]

customer = selected["customer"]
address = selected["address"]

st.write("### Customer")
st.info(customer)

st.write("### Original Address")
st.warning(address)

keywords = ["near", "behind", "beside", "opposite"]

vague = any(word in address.lower() for word in keywords)

if vague:

    st.error("⚠ Ambiguous Address Detected")

    st.info(
        "Please provide an additional landmark."
    )

    response = st.text_input(
        "Customer Response"
    )

    if response:

        final_address = (
            address + ", " + response
        )

        st.success(
            "Address Successfully Resolved"
        )

        st.write(
            "### Driver Instructions"
        )

        st.code(final_address)

else:

    st.success(
        "Address Looks Clear"
    )

    st.code(address)
