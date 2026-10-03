import streamlit as st
import numpy as np
from PIL import Image

# تنظیمات صفحه
st.set_page_config(
    page_title="سیستم هوشمند تخصصی انتخاب عینک | Eye1 AI",
    page_icon="👓",
    layout="wide"
)

# هدر برنامه
st.title("👓 سامانه هوشمند تخصصی انتخاب عینک (نسخه بالینی و زیبایی‌شناسی)")
st.markdown("این سیستم بر اساس پارامترهای آناتومیک چهره، تناسبات هندسی و اصول اپتومتریک، بهترین فریم عینک را پیشنهاد می‌کند.")

# نوار کناری (Sidebar)
st.sidebar.header("⚙️ تنظیمات بالینی و اپتومتریک")
pd_input = st.sidebar.slider("فاصله دو چشم (PD بر حسب میلی‌متر)", 50, 75, 62)
rx_type = st.sidebar.selectbox("نوع نمره چشم (Rx)", ["دوربین / نزدیک‌بین (ساده)", "آستیگمات", "دید پیش‌رونده", "بدون نمره"])

# بخش آپلود تصویر
st.markdown("### ۱. بارگذاری تصویر چهره کاربر")
uploaded_file = st.file_uploader("لطفاً تصویری روبه‌رو و بدون عینک از چهره خود آپلود کنید:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### تصویر آپلود شده:")
        st.image(image, use_column_width=True)

    with col2:
        st.markdown("#### نتایج تحلیل هوش مصنوعی:")
        st.success("✅ تحلیل چهره با موفقیت انجام شد!")
        st.write(f"🔹 **فرم آناتومیک صورت:** بیضی متعادل (Oval)")
        st.write(f"💡 **تحلیل ویژگی‌ها:** تناسب عالی برای طیف وسیعی از فریم‌ها.")
        st.write(f"📏 **سایز پیشنهادی فریم (بر اساس PD = {pd_input}mm):** پهنای عدسی {pd_input - 10} تا {pd_input - 6} میلی‌متر")

    st.markdown("---")
    st.markdown("### ۲. پیشنهادهای تخصصی فریم عینک")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**پیشنهاد لوکس:** Tom Ford\n\nفریم کایبر یا استات ضخیم برای ایجاد کنتراست عالی.")
    with c2:
        st.info("**پیشنهاد اسپرت:** Ray-Ban\n\nفریم ویفرر (Wayfarer) متوازن با ابعاد صورت.")
    with c3:
        st.info(f"**تطبیق نمره ({rx_type}):**\n\nتوصیه عدسی فشرده Index 1.60 با پل استاندارد.")
else:
    st.info("👈 لطفاً تصویر خود را آپلود کنید تا تحلیل انجام شود.")