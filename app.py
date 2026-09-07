import streamlit as st

st.set_page_config(
    page_title="GlobalMove",
    page_icon="🌍",
    layout="wide"
)

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: #f7f9fc;
}

.block-container {
    max-width: 1100px;
    padding-top: 25px;
}

.logo {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 35px;
}

.logo span {
    color: #1677ff;
}

.hero {
    background: linear-gradient(135deg,#061a35,#0d3970);
    padding: 70px 30px;
    border-radius: 25px;
    color: white;
    text-align: center;
}

.hero h1 {
    font-size: 55px;
    font-weight: 800;
}

.hero p {
    font-size: 19px;
    color: #d9e7ff;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #e5eaf1;
    margin-top: 25px;
}

.signup-box {
    max-width: 550px;
    margin: 30px auto;
    background: white;
    padding: 35px;
    border-radius: 20px;
    border: 1px solid #e5eaf1;
}

.center {
    text-align: center;
}

.footer {
    margin-top: 70px;
    padding: 35px;
    text-align: center;
    color: #667085;
}
</style>
""", unsafe_allow_html=True)


# ---------- SESSION ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "account_created" not in st.session_state:
    st.session_state.account_created = False


# ---------- NAVBAR ----------
c1, c2 = st.columns([2, 1])

with c1:
    st.markdown(
        '<div class="logo">Global<span>Move</span> 🌍</div>',
        unsafe_allow_html=True
    )

with c2:
    x, y = st.columns(2)

    with x:
        if st.button("Login", use_container_width=True):
            st.session_state.page = "login"

    with y:
        if st.button("Sign Up", use_container_width=True):
            st.session_state.page = "signup"


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <h1>Global delivery.<br>Built for speed.</h1>
        <p>
        Ship packages, track deliveries, shop products
        and manage your business from one platform.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    a, b, c = st.columns(3)

    with a:
        st.markdown("""
        <div class="card">
        <h2>📦</h2>
        <h3>Package Delivery</h3>
        <p>Fast and reliable package delivery.</p>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown("""
        <div class="card">
        <h2>🌎</h2>
        <h3>Global Shipping</h3>
        <p>Move products across countries and continents.</p>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="card">
        <h2>🏢</h2>
        <h3>Business Services</h3>
        <p>Tools for businesses to manage logistics.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("Create Your Account →", use_container_width=True):
        st.session_state.page = "signup"


# =========================================================
# SIGN UP
# =========================================================

elif st.session_state.page == "signup":

    st.markdown("""
    <div class="signup-box">
    <div class="center">
    <h1>Create your account</h1>
    <p>Join GlobalMove and start moving.</p>
    </div>
    """, unsafe_allow_html=True)

    first = st.text_input("First name", placeholder="Your first name")

    last = st.text_input("Last name", placeholder="Your last name")

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
            st.session_state.account_created = True
            st.session_state.page = "account"

            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()


# =========================================================
# ACCOUNT CREATED
# =========================================================

elif st.session_state.page == "account":

    st.markdown("""
    <div class="signup-box center">

    <h1>🎉 Welcome to GlobalMove!</h1>

    <p>Your account has been created successfully.</p>

    <p>
    Your account dashboard will be available here.
    </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Continue to GlobalMove →",
        type="primary",
        use_container_width=True
    ):
        st.session_state.page = "home"
        st.rerun()


# =========================================================
# LOGIN
# =========================================================

elif st.session_state.page == "login":

    st.markdown("""
    <div class="signup-box">

    <div class="center">
    <h1>Welcome back</h1>
    <p>Log in to your GlobalMove account.</p>
    </div>

    """, unsafe_allow_html=True)

    email = st.text_input(
        "Email address",
        placeholder="you@example.com"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Your password"
    )

    if st.button(
        "Log In",
        type="primary",
        use_container_width=True
    ):

        if email and password:
            st.success("Login interface is ready.")
        else:
            st.error("Enter your email and password.")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Create a new account"):
        st.session_state.page = "signup"
        st.rerun()


# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <h3>GlobalMove 🌍</h3>
    <p>
    Global transportation, commerce and business services.
    </p>
    <p>© 2026 GlobalMove</p>
</div>
""", unsafe_allow_html=True)