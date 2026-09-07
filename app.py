import streamlit as st

st.set_page_config(
    page_title="StoreFront",
    page_icon="🛍️",
    layout="wide"
)

# =========================
# BROWN THEME
# =========================

st.markdown("""
<style>

.stApp {
    background-color: #5A3825;
}

.block-container {
    max-width: 1150px;
    padding-top: 25px;
}

.hero {
    background: linear-gradient(135deg, #2B160D, #7A4A2A);
    padding: 70px 30px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}

.card {
    background: #FFF9F3;
    color: #2B160D;
    padding: 30px;
    border-radius: 20px;
    margin-top: 20px;
    text-align: center;
}

.logo {
    font-size: 28px;
    font-weight: 800;
    color: white;
}

.logo span {
    color: #D9A066;
}

.footer {
    text-align: center;
    color: #E6CCB5;
    margin-top: 70px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION
# =========================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "user" not in st.session_state:
    st.session_state.user = None

# =========================
# NAVBAR
# =========================

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    st.markdown(
        '<div class="logo">Store<span>Front</span> 🛍️</div>',
        unsafe_allow_html=True
    )

with col2:
    if st.button("Login", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()

with col3:
    if st.button("Sign Up", use_container_width=True):
        st.session_state.page = "signup"
        st.rerun()

# =========================
# HOME
# =========================

if st.session_state.page == "home":

    st.markdown('<div class="hero"></div>', unsafe_allow_html=True)

    st.write("")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
            <h2>🛍️ Shop Products</h2>
            <p>Browse and buy products easily.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="card">
            <h2>🚚 Fast Delivery</h2>
            <p>We deliver to your address nationwide.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
            <h2>💳 Secure Payment</h2>
            <p>Pay online with card or transfer.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if st.button("Create Your Account →", use_container_width=True):
        st.session_state.page = "signup"
        st.rerun()

# =========================
# SIGN UP
# =========================

elif st.session_state.page == "signup":

    st.title("Create your account")

    st.write("Join us and start shopping today.")

    col1, col2 = st.columns(2)

    with col1:
        first = st.text_input("First name", placeholder="Your first name")
        email = st.text_input("Email address", placeholder="you@example.com")
        address = st.text_area("Delivery Address", placeholder="12 Market Street, Onitsha")
        country = st.selectbox("Country", ["Nigeria", "Ghana", "Kenya", "South Africa", "USA", "UK"])

    with col2:
        last = st.text_input("Last name", placeholder="Your last name")
        phone = st.text_input("Phone number", placeholder="+234...")
        state = st.text_input("State/City", placeholder="Anambra State")
        password = st.text_input("Password", type="password", placeholder="Create a password")

    confirm = st.text_input("Confirm password", type="password", placeholder="Repeat your password")
    terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")

    if st.button("Create Account", type="primary", use_container_width=True):

        if not first or not last or not email or not password or not address or not state or not phone:
            st.error("Please complete all required fields.")

        elif password != confirm:
            st.error("Passwords do not match.")

        elif len(password) < 6:
            st.error("Password must be at least 6 characters.")

        elif not terms:
            st.error("Please accept the Terms of Service.")

        else:
            st.session_state.user = {
                "first": first,
                "last": last,
                "email": email,
                "phone": phone,
                "address": address,
                "state": state,
                "country": country
            }

            st.session_state.page = "account"
            st.rerun()

    if st.button("← Back"):
        st.session_state.page = "home"
        st.rerun()

# =========================
# ACCOUNT
# =========================

elif st.session_state.page == "account":

    user = st.session_state.user

    st.title(f"Welcome, {user['first']}! 🎉")

    st.success("Your account has been created successfully.")

    st.write("### Account Details")

    st.write(f"**Name:** {user['first']} {user['last']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Phone:** {user['phone']}")
    st.write(f"**Address:** {user['address']}")
    st.write(f"**State:** {user['state']}")
    st.write(f"**Country:** {user['country']}")

    st.write("")

    if st.button("← Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# =========================
# LOGIN
# =========================

elif st.session_state.page == "login":

    st.title("Welcome back")

    st.write("Log in to your account.")

    email = st.text_input("Email address")
    password = st.text_input("Password", type="password")

    if st.button("Log In", type="primary", use_container_width=True):
        if email and password:
            st.success("Login will be connected to Supabase next.")
        else:
            st.error("Enter your email and password.")

    if st.button("Create an account"):
        st.session_state.page = "signup"
        st.rerun()

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

StoreFront 🛍️

<br><br>

Online shopping with fast delivery.

<br><br>

© 2026 StoreFront

</div>
""", unsafe_allow_html=True)