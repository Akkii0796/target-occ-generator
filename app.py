import streamlit as st

# Function to extract TCIN from Target URL
def extract_tcin(url):
    if "preselect=" in url:
        return url.split("preselect=")[1].split("&")[0].split("#")[0]
    elif "/A-" in url:
        return url.split("/A-")[1].split("?")[0].split("#")[0]
    else:
        return None

# App title
st.title("🎯 Target OCC Link Generator")

# Ask user how many products they want to create ads for
num_products = st.number_input("How many products do you want to show ads for?", min_value=1, step=1)

# Collect product URL and quantity for each product
product_data = []
for i in range(num_products):
    url = st.text_input(f"Enter URL for product {i + 1}", key=f"url_{i}")
    quantity = st.number_input(f"Quantity for product {i + 1}", min_value=1, step=1, key=f"qty_{i}")
    product_data.append((url, quantity))

# Ask for the Affiliate ID
afid = st.text_input("Enter your AFID")

# Generate OCC link when the button is clicked
if st.button("Generate OCC Link"):
    pl_items = []
    for url, qty in product_data:
        tcin = extract_tcin(url.strip())
        if tcin:
            pl_items.append(f"{tcin}:{qty}")
        else:
            st.error(f"❌ Could not extract TCIN from: {url}")
    
    if pl_items:
        pl_param = ",".join(pl_items)
        occ_link = f"https://www.target.com/occ?pl={pl_param}&afid={afid.strip()}"
        st.success("✅ OCC Link generated successfully:")
        st.code(occ_link, language="text")
    else:
        st.warning("⚠️ No valid TCINs extracted. Please check your URLs.")
