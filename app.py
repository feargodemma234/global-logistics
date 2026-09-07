import streamlit as st
from supabase import create_client, Client

st.set_page_config(page_title="StoreFront", page_icon="🛍️", layout="wide")

# =========================
# SUPABASE CONNECTION
# =========================
SUPABASE_URL = "PASTE_YOUR_URL_HERE" # from supabase
SUPABASE_KEY = "PASTE_YOUR_ANON_KEY_HERE" # from supabase

@st.cache_resource
def init_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

supabase: Client = init_supabase()

# =========================
# THEME
# =========================
st.markdown("""
<style>
.stApp {background-color: #5A3825;}
.block-container {max-width: 1150px; padding-top: 25px;}
.hero {background: linear-gradient(135deg, #2B160D, #7A4A2A); padding: 70px 30px; border-radius: 25px; text-align: center; color: white; margin-bottom: 20px;}
.card {background: #FFF9F3; color: #2B160D; padding: 30px; border-radius: 20px; margin-top: 20px; text-align: center;}
.logo {font-size: 28px; font-weight: 800; color: white;}
.logo span {color: #D9A066;}
.footer {text-align: center; color: #E6CCB5; margin-top: 70px;}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION
# =========================
if "page" not in st.session_state: st.session_state.page = "home"
if "user" not in st.session_state: st.session_state.user = None

# =========================
# NAVBAR
# =========================
col1, col2, col3 = st.columns([3, 1, 1])
with col1: st.markdown('<div class="logo">Store<span>Front</span> 🛍️</div>', unsafe_allow_html=True)
with col2:
    if st.session_state.user is None:
        if st.button("Login", use_container_width=True): st.session_state.page = "login"; st.rerun()
    else:
        if st.button("Logout", use_container_width=True): st.session_state.user = None; st.session_state.page = "home"; st.rerun()
with col3:
    if st.session_state.user is None:
        if st.button("Sign Up", use_container_width=True): st.session_state.page = "signup"; st.rerun()

# =========================
# HOME
# =========================
if st.session_state.page == "home":
    st.markdown('<div class="hero"></div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a: st.markdown('<div class="card"><h2>🛍️ Shop Products</h2><p>Browse and buy products easily.</p></div>', unsafe_allow_html=True)
    with b: st.markdown('<div class="card"><h2>🚚 Fast Delivery</h2><p>We deliver to your address nationwide.</p></div>', unsafe_allow_html=True)
    with c: st.markdown('<div class="card"><h2>💳 Secure Payment</h2><p>Pay online with card or transfer.</p></div>', unsafe_allow_html=True)
    if st.button("Create Your Account →", use_container_width=True): st.session_state.page = "signup"; st.rerun()

# =========================
# SIGN UP - NOW SAVES TO SUPABASE
# =========================
elif st.session_state.page == "signup":
    st.title("Create your account")
    col1, col2 = st.columns(2)
    with col1:
        first = st.text_input("First name")
        email = st.text_input("Email address")
        address = st.text_area("Delivery Address")
        country = st.selectbox("Country", ["Nigeria", "Ghana", "Kenya", "South Africa", "USA", "UK"])
    with col2:
        last = st.text_input("Last name")
        phone = st.text_input("Phone number")
        state = st.text_input("State/City")
        password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm password", type="password")
    terms = st.checkbox("I agree to Terms")

    if st.button("Create Account", type="primary", use_container_width=True):
        if not all([first, last, email, password, address, state, phone]):
            st.error("Please complete all required fields.")
        elif password!= confirm: st.error("Passwords do not match.")
        elif len(password) < 6: st.error("Password must be at least 6 characters.")
        elif not terms: st.error("Please accept Terms.")
        else:
            try:
                data = {
                    "first_name": first, "last_name": last, "email": email,
                    "phone": phone, "address": address, "state": state,
                    "country": country, "password": password # NOTE: In production use Supabase Auth + hashing
                }
                supabase.table("users").insert(data).execute()
                st.success("Account created! Please login.")
                st.session_state.page = "login"
                st.rerun()
            except Exception as e:
                st.error(f"Email already exists or error: {e}")

    if st.button("← Back"): st.session_state.page = "home"; st.rerun()

# =========================
# ACCOUNT
# =========================
elif st.session_state.page == "account":
    user = st.session_state.user
    st.title(f"Welcome, {user['first_name']}! 🎉")
    st.success("You are logged in.")
    st.write("### Account Details")
    st.write(f"**Name:** {user['first_name']} {user['last_name']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Phone:** {user['phone']}")
    st.write(f"**Address:** {user['address']}, {user['state']}, {user['country']}")
    if st.button("← Home", use_container_width=True): st.session_state.page = "home"; st.rerun()

# =========================
# LOGIN - NOW CHECKS SUPABASE
# =========================
elif st.session_state.page == "login":
    st.title("Welcome back")
    email = st.text_input("Email address")
    password = st.text_input("Password", type="password")

    if st.button("Log In", type="primary", use_container_width=True):
        if email and password:
            res = supabase.table("users").select("*").eq("email", email).eq("password", password).execute()
            if len(res.data) > 0:
                st.session_state.user = res.data[0]
                st.session_state.page = "account"
                st.rerun()
            else:
                st.error("Invalid email or password.")
        else:
            st.error("Enter your email and password.")

    if st.button("Create an account"): st.session_state.page = "signup"; st.rerun()

# =========================
# FOOTER
# =========================
st.markdown('<div class="footer">StoreFront 🛍️ <br><br> Online shopping with fast delivery. <br><br> © 2026 StoreFront </div>', unsafe_allow_html=True)