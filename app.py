import streamlit as st

st.set_page_config(
    page_title="GlobalMove",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: #5A3825;
}

.block-container {
    max-width: 1150px;
    padding-top: 25px;
}

/* LOGO */

.logo {
    font-size: 29px;
    font-weight: 800;
    color: #FFF9F3;
    margin-bottom: 35px;
}

.logo span {
    color: #D9A066;
}

/* HERO */

.hero {
    background: linear-gradient(135deg, #2B160D, #7A4A2A);
    padding: 80px 30px;
    border-radius: 28px;
    text-align: center;
    color: white;
    box-shadow: 0 15px 40px rgba(0,0,0,.25);
}

.hero h1 {
    font-size: 58px;
    font-weight: 800;
    line-height: 1.05;
    margin-bottom: 20px;
}

.hero h1 span {
    color: #D9A066;
}

.hero p {
    font-size: 19px;
    color: #F2DFCC;
    max-width: 700px;
    margin: auto;
}

/* CARDS */

.card {
    background: #FFF9F3;
    color: #2B160D;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #D9B99A;
    margin-top: 25px;
    min-height: 190px;
    box-shadow: 0 8px 25px rgba(0,0,0,.15);
}

.card h2 {
    margin: 0;
}

.card h3 {
    color: #4A2818;
}

.card p {
    color: #73513B;
}

/* SIGNUP BOX */

.signup-box {
    max-width: 560px;
    margin: 35px auto;
    padding: 38px;
    background: #FFF9F3;
    color: #2B160D;
    border-radius: 22px;
    border: 1px solid #D9B99A;
    box-shadow: 0 15px 40px rgba(0,0,0,.2);
}

.signup-box h1 {
    color: #2B160D;
}

.signup-box p {
    color: #73513B;
}

/* INPUTS */

.stTextInput label,
.stNumberInput label,
.stSelectbox label {
    color: #FFF9F3 !important;
    font-weight: 600;
}

.signup-box input {
    background: white !important;
    color: #2B160D !important;
}

/* BUTTONS */

div.stButton > button {
    border-radius: 12px;
    min-height: 46px;
    font-weight: 700;
}

/* FOOTER */

.footer {
    margin-top: 80px;
    padding: 40px;
    text-align: center;
    color: #E6CCB5;
    border-top: 1px solid #81583C;
}

.center {
    text-align: center;
}

/* MOBILE */

@media (max-width: 700px) {

    .hero {
        padding: 55px 20px;
    }

    .hero h1 {
        font-size: 40px;
    }

    .hero p {
        font-size: 16px;
    }

    .signup-box {
        padding: 25px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================
# SESSION STATE
# =========================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "account_created" not in st.session_state:
    st.session_state.account_created = False


# =========================
# NAVIGATION
# =========================

left, right = st.columns([2, 1])

with left:

    st.markdown(
        '<div class="logo">Global<span>Move</span> 🌍</div>',
        unsafe_allow_html=True
    )

with right:

    login_col, signup_col = st.columns(2)

    with login_col:

        if st.button(
            "Login",
            use_container_width=True
        ):

            st.session_state.page = "login"
            st.rerun()

    with signup_col:

        if st.button(
            "Sign Up",
            use_container_width=True
        ):

            st.session_state.page = "signup"
            st.rerun()


# ==========================================================
# HOME
# ==========================================================

if st.session_state.page == "home":

    # HERO
    st.markdown("""
    <div class="hero">

        <h1>
            Global delivery.<br>
            <span>Built for speed.</span>
        </h1>

        <p>
            Ship packages, track deliveries, shop products
            and manage your business from one global platform.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # MAIN BUTTONS

    b1, b2, b3 = st.columns(3)

    with b1:

        if st.button(
            "📦 Ship a Package",
            use_container_width=True
        ):

            st.info(
                "Shipping services will be available soon."
            )

    with b2:

        if st.button(
            "📍 Track Package",
            use_container_width=True
        ):

            st.info(
                "Package tracking will be available soon."
            )

    with b3:

        if st.button(
            "🛒 Marketplace",
            use_container_width=True
        ):

            st.info(
                "Marketplace coming soon."
            )

    # SERVICES

    st.write("")
    st.write("")

    st.markdown(
        "<h2 style='color:#FFF9F3;'>Everything that moves.</h2>",
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:

        st.markdown("""
        <div class="card">

            <h2>📦</h2>

            <h3>
                Package Delivery
            </h3>

            <p>
                Fast and reliable delivery for packages
                of different sizes.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with b:

        st.markdown("""
        <div class="card">

            <h2>🌎</h2>

            <h3>
                Global Shipping
            </h3>

            <p>
                Move products between cities,
                countries and continents.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with c:

        st.markdown("""
        <div class="card">

            <h2>🏢</h2>

            <h3>
                Business Services
            </h3>

            <p>
                Logistics tools designed to help
                businesses grow.
            </p>

        </div>
        """, unsafe_allow_html=True)

    # ACCOUNT CTA

    st.write("")
    st.write("")

    st.markdown("""
    <div class="card">

        <div class="center">

            <h2>
                Start moving with GlobalMove.
            </h2>

            <p>
                Create your account and get access
                to our transportation and commerce platform.
            </p>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "Create Your Account →",
        use_container_width=True
    ):

        st.session_state.page = "signup"
        st.rerun()


# ==========================================================
# SIGN UP
# ==========================================================

elif st.session_state.page == "signup":

    st.markdown("""
    <div class="signup-box">

        <div class="center">

            <h1>
                Create your account
            </h1>

            <p>
                Join GlobalMove and start moving.
            </p>

        </div>

    </div>
    """, unsafe_allow_html=True)

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

    st.write("")

    if st.button(
        "Create Account",
        type="primary",
        use_container_width=True
    ):

        if not first:

            st.error(
                "Please enter your first name."
            )

        elif not last:

            st.error(
                "Please enter your last name."
            )

        elif not email:

            st.error(
                "Please enter your email address."
            )

        elif not password:

            st.error(
                "Please create a password."
            )

        elif password != confirm:

            st.error(
                "Passwords do not match."
            )

        elif len(password) < 6:

            st.error(
                "Password must be at least 6 characters."
            )

        elif not terms:

            st.error(
                "Please accept the Terms of Service."
            )

        else:

            st.session_state.account_created = True

            st.session_state.user = {
                "first_name": first,
                "last_name": last,
                "email": email,
                "phone": phone
            }

            st.session_state.page = "account"

            st.rerun()

    st.write("")

    if st.button("← Back to Home"):

        st.session_state.page = "home"
        st.rerun()


# ==========================================================
# ACCOUNT
# ==========================================================

elif st.session_state.page == "account":

    user = st.session_state.get(
        "user",
        {}
    )

    first_name = user.get(
        "first_name",
        "there"
    )

    st.markdown(f"""
    <div class="signup-box">

        <div class="center">

            <h1>
                🎉 Welcome, {first_name}!
            </h1>

            <p>
                Your GlobalMove account has been created.
            </p>

            <br>

            <h3>
                Your account dashboard
            </h3>

            <p>
                Shipping, tracking, marketplace and
                business services will appear here.
            </p>

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📦 Ship a Package",
            use_container_width=True
        ):

            st.info(
                "Shipping is coming soon."
            )

    with col2:

        if st.button(
            "📍 Track Package",
            use_container_width=True
        ):

            st.info(
                "Tracking is coming soon."
            )

    st.write("")

    if st.button(
        "← Return to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()


# ==========================================================
# LOGIN
# ==========================================================

elif st.session_state.page == "login":

    st.markdown("""
    <div class="signup-box">

        <div class="center">

            <h1>
                Welcome back
            </h1>

            <p>
                Log in to your GlobalMove account.
            </p>

        </div>

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

    st.write("")

    if st.button(
        "Log In",
        type="primary",
        use_container_width=True
    ):

        if not email or not password:

            st.error(
                "Please enter your email and password."
            )

        else:

            st.success(
                "Login system is ready."
            )

    st.write("")

    if st.button(
        "Create a new account",
        use_container_width=True
    ):

        st.session_state.page = "signup"
        st.rerun()


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("""
<div class="footer">

    <h3>
        GlobalMove 🌍
    </h3>

    <p>
        Global transportation, commerce and business services.
    </p>

    <p>
        © 2026 GlobalMove
    </p>

</div>
""", unsafe_allow_html=True)