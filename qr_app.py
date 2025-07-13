import streamlit as st
import qrcode
from io import BytesIO

st.title("สร้าง QR Code นามบัตร (vCard)")

fields = ["name", "phone", "email", "line_id", "website", "org", "title", "address"]
for field in fields:
    if field not in st.session_state:
        st.session_state[field] = ""

with st.form("vcard_form"):
    name = st.text_input("ชื่อ-นามสกุล", value=st.session_state.name, key="name")
    phone = st.text_input("เบอร์โทร", value=st.session_state.phone, key="phone")
    email = st.text_input("อีเมล", value=st.session_state.email, key="email")
    line_id = st.text_input("Line ID", value=st.session_state.line_id, key="line_id")
    website = st.text_input("เว็บไซต์ (ถ้ามี)", value=st.session_state.website, key="website")
    org = st.text_input("ชื่อองค์กร", value=st.session_state.org, key="org")
    title = st.text_input("ตำแหน่ง", value=st.session_state.title, key="title")
    address = st.text_area("ที่อยู่", value=st.session_state.address, key="address")

    submitted = st.form_submit_button("✨ สร้าง QR Code")

if st.button("🧹 ล้างฟอร์ม"):
    for field in fields:
        st.session_state[field] = ""

if submitted:
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
N:{name}
ORG:{org}
TITLE:{title}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
ADR;TYPE=home:;;{address};;;;  # ที่อยู่จะถูกแสดงตรงนี้
NOTE:Line ID: {line_id}
URL:{website}
END:VCARD"""

    qr_img = qrcode.make(vcard)
    buf = BytesIO()
    qr_img.save(buf, format="PNG")
    qr_image_bytes = buf.getvalue()

    st.image(qr_image_bytes, caption="QR Code นามบัตร", use_container_width=True)
    st.download_button(
        "📥 ดาวน์โหลด QR Code",
        data=qr_image_bytes,
        file_name="vcard_qrcode.png",
        mime="image/png"
    )

