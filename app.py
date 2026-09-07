import streamlit as st

st.set_page_config(
    page_title="GlobalMove | Global Logistics",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f7f9fc;
}

.block-container {
    padding-top: 1rem;
    max-width: 1250px;
}

.nav {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:12px 0 25px;
}

.logo {
    font-size:26px;
    font-weight:800;
}

.logo span {
    color:#1677ff;
}

.hero {
    padding:75px 20px;
    border-radius:28px;
    background:linear-gradient(135deg,#071a35,#0d3970);
    color:white;
    text-align:center;
    margin-bottom:40px;
}

.hero h1 {
    font-size:58px;
    font-weight:800;
    margin-bottom:15px;
}

.hero p {
    font-size:20px;
    color:#d8e7ff;
    max-width:700px;
    margin:auto;
}

.section {
    margin:55px 0 25px;
}

.section h2 {
    font-size:34px;
    font-weight:800;
}

.card {
    background:white;
    padding:28px;
    border-radius:18px;
    border:1px solid #e5eaf1;
    height:100%;
    box-shadow:0 5px 20px rgba(0,0,0,.04);
}

.card h3 {
    margin-top:10px;
}

.icon {
    font-size:38px;
}

.track {
    background:white;
    padding:35px;
    border-radius:20px;
    border:1px solid #e5eaf1;
    margin-top:20px;
}

.footer {
    margin-top:80px;
    padding:40px 0;
    border-top:1px solid #ddd;
    color:#667085;
    text-align:center;
}

div.stButton > button {
    border-radius:10px;
    font-weight:700;
    min-height:45px;
}

</style>
""", unsafe_allow_html=True)

# NAVBAR
st.markdown("""
<div class="nav">
    <div class="logo">Global<span>Move</span> 🌍</div>
    <div>Ship &nbsp; • &nbsp; Track &nbsp; • &nbsp; Marketplace &nbsp; • &nbsp; Business</div>
</div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <h1>Global delivery.<br>Built for speed.</h1>
    <p>
        Ship packages, track deliveries, shop products and manage
        your business from one global platform.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,1,1])

with c1:
    if st.button("📦 Ship a Package", use_container_width=True):
        st.session_state["page"] = "ship"

with c2:
    if st.button("📍 Track Package", use_container_width=True):
        st.session_state["page"] = "track"

with c3:
    if st.button("🛒 Marketplace", use_container_width=True):
        st.session_state["page"] = "shop"

# SHIPPING
st.markdown('<div class="section"><h2>Ship anywhere</h2></div>',
            unsafe_allow_html=True)

a,b,c = st.columns(3)

with a:
    st.markdown("""
    <div class="card">
    <div class="icon">📦</div>
    <h3>Package Delivery</h3>
    <p>Send packages locally and internationally with reliable delivery options.</p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="card">
    <div class="icon">🌎</div>
    <h3>Global Shipping</h3>
    <p>Connect customers and businesses across countries and continents.</p>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="card">
    <div class="icon">🚚</div>
    <h3>Transportation</h3>
    <p>Build a complete transportation network for moving goods efficiently.</p>
    </div>
    """, unsafe_allow_html=True)

# QUOTE
st.markdown('<div class="section"><h2>Get a shipping estimate</h2></div>',
            unsafe_allow_html=True)

q1,q2 = st.columns(2)

with q1:
    origin = st.text_input("From", placeholder="Lagos, Nigeria")
    destination = st.text_input("To", placeholder="London, UK")

with q2:
    weight = st.number_input("Package weight (kg)", min_value=0.1, value=1.0)
    speed = st.selectbox(
        "Delivery speed",
        ["Standard", "Express", "Priority"]
    )

if st.button("Calculate Estimate", use_container_width=True):
    base = 10 + weight * 4

    if speed == "Express":
        base *= 1.5
    elif speed == "Priority":
        base *= 2

    st.success(
        f"Estimated shipping cost: ${base:,.2f}"
    )

# TRACKING
st.markdown('<div class="section"><h2>Track your package</h2></div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="track">
<h3>📍 Shipment Tracking</h3>
<p>Enter your tracking number to check your shipment status.</p>
</div>
""", unsafe_allow_html=True)

tracking = st.text_input(
    "Tracking number",
    placeholder="GM-123456789"
)

if st.button("Track Shipment", use_container_width=True):

    if tracking:
        st.info("Shipment found.")

        st.progress(0.65)

        t1,t2,t3,t4 = st.columns(4)

        t1.markdown("✅ **Order Created**")
        t2.markdown("✅ **Picked Up**")
        t3.markdown("🚚 **In Transit**")
        t4.markdown("⬜ **Delivered**")
    else:
        st.warning("Enter a tracking number.")

# MARKETPLACE
st.markdown('<div class="section"><h2>Marketplace</h2></div>',
            unsafe_allow_html=True)

products = [
    ("📱", "Smartphone", "$299"),
    ("💻", "Laptop", "$699"),
    ("🎧", "Wireless Headphones", "$79"),
    ("⌚", "Smart Watch", "$129")
]

cols = st.columns(4)

for col, product in zip(cols, products):
    with col:
        st.markdown(f"""
        <div class="card">
        <div class="icon">{product[0]}</div>
        <h3>{product[1]}</h3>
        <h3>{product[2]}</h3>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "View Product",
            key=product[1],
            use_container_width=True
        )

# BUSINESS
st.markdown('<div class="section"><h2>Built for businesses</h2></div>',
            unsafe_allow_html=True)

b1,b2 = st.columns(2)

with b1:
    st.markdown("""
    <div class="card">
    <h2>🏢 Business Services</h2>
    <p>
    Manage shipments, orders, inventory and deliveries
    from one centralized platform.
    </p>
    </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown("""
    <div class="card">
    <h2>📊 Business Dashboard</h2>
    <p>
    Monitor deliveries, sales, customers and logistics
    operations as your business grows.
    </p>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    <h3>GlobalMove 🌍</h3>
    <p>Global transportation, commerce and business services.</p>
    <p>© 2026 GlobalMove. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)