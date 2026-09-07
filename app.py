import streamlit as st

st.set_page_config(
    page_title="GlobalMove",
    page_icon="🌍",
    layout="wide"
)

# =========================
# BROWN THEME
# =========================
st.markdown('<div class="hero"><div class="hero-title">Global delivery.<br>Built for speed.</div><div class="hero-text">Ship packages, track deliveries, shop products and manage your business from one global platform.</div></div>', unsafe_allow_html=True)

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
        '<div class="logo">Global<span>Move</span> 🌍</div>',
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

    st.markdown("""
    <div class="hero">

        <div class="hero-title">
            Global delivery.<br>
            Built for speed.
        </div>

        <div class="hero-text">
            Ship packages, track deliveries, shop products
            and manage your business from one global platform.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
            <h2>📦 Package Delivery</h2>
            <p>Fast and reliable delivery for packages.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="card">
            <h2>🌎 Global Shipping</h2>
            <p>Move products across cities and countries.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
            <h2>🏢 Business Services</h2>
            <p>Logistics tools for growing businesses.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "Create Your Account →",
        use_container_width=True
    ):
        st.session_state.page = "signup"
        st.rerun()


# =========================
# SIGN UP
# =========================

elif st.session_state.page == "signup":

    st.title("Create your account")

    st.write(
        "Join GlobalMove and start moving."
    )

    first = st.text_input(
        "First name",
        placeholder="Your first name"
    )

    last = st.text_input(
        "Last name",
        placeholder="Your last name"
    )

    email = st.text_input(
        "Email address",
        placeholder="you@example.com"
    )

    phone = st.text_input(
        "Phone number",
        placeholder="+234..."
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Create a password"
    )

    confirm = st.text_input(
        "Confirm password",
        type="password",
        placeholder="Repeat your password"
    )

    terms = st.checkbox(
        "I agree to the Terms of Service and Privacy Policy"
    )

    if st.button(
        "Create Account",
        type="primary",
        use_container_width=True
    ):

        if not first or not last or not email or not password:
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
                "phone": phone
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

    st.title(
        f"Welcome, {user['first']}! 🎉"
    )

    st.success(
        "Your account has been created successfully."
    )

    st.write("### Account")

    st.write(
        f"**Name:** {user['first']} {user['last']}"
    )

    st.write(
        f"**Email:** {user['email']}"
    )

    if user["phone"]:
        st.write(
            f"**Phone:** {user['phone']}"
        )

    st.write("")

    if st.button(
        "← Home",
        use_container_width=True
    ):
        st.session_state.page = "home"
        st.rerun()


# =========================
# LOGIN
# =========================

elif st.session_state.page == "login":

    st.title("Welcome back")

    st.write(
        "Log in to your GlobalMove account."
    )

    email = st.text_input(
        "Email address"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Log In",
        type="primary",
        use_container_width=True
    ):

        if email and password:
            st.success(
                "Login will be connected to Supabase next."
            )
        else:
            st.error(
                "Enter your email and password."
            )

    if st.button("Create an account"):
        st.session_state.page = "signup"
        st.rerun()


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

GlobalMove 🌍

<br><br>

Global transportation, commerce and business services.

<br><br>

© 2026 GlobalMove

</div>
""", unsafe_allow_html=True)