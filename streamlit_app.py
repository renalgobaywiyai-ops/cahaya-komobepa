import streamlit as st

st.set_page_config(page_title="Cahya Komobepa")
st.title("Website Cahaya Komobepa")
st.subheader("Selamat datang di website Cahay Komobepa")
menu = st.sidebar.selectbox(
    "Pilih Menuh",
    ["Beranda", Tentang", "Kontak"]
)
if menu == "Beranda":
    st.write("Ini adalah halaman utama website.")

elif menu == "Tentang":
     st.write("Cahaya Komobepa adalah website
informasi dan publikasi.")

elif menu == "Kontak":
    st.write(Email: renalgobaywiyai@gmail.com")
    st.write(WhatsApp: 08xxxxxxxxxx")
st.image(
"https://cahaya-komobepa.io/images/brand/streamilit-log
o-primary-colormark-darktext.png",
   width=200
)
                            
