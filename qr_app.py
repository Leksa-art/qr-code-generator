import streamlit as st
import qrcode
from io import BytesIO

st.title("สร้าง QR Code นามบัตร (vCard)")

fields = ["name", "phone", "email", "line_id", "website", "org", "title"]

def clear_form():
    for field in fields:
        st.session_state[field] = ""

with st.form("vcard_form"):
    name = st.text_input("ชื่อ-นามสกุล", key="name")
    phone = st.text_input("เบอร์โทร", key="phone")
    email = st.text_input("อีเมล", key="email")
    line_id = st.text_input("Line ID", key="line_id")
    website = st.text_input("เว็บไซต์ (ถ้ามี)", key="website")
    org = st.text_input("ชื่อองค์กร", key="org")
    title = st.text_input("ตำแหน่ง", key="title")

    submitted = st.form_submit_button("✨ สร้าง QR Code")
    clear_clicked = st.form_submit_button("🧹 ล้างฟอร์ม", on_click=clear_form)

if submitted:
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{st.session_state.name}
N:{st.session_state.name}
ORG:{st.session_state.org}
TITLE:{st.session_state.title}
TEL;TYPE=CELL:{st.session_state.phone}
EMAIL:{st.session_state.email}
NOTE:Line ID: {st.session_state.line_id}
URL:{st.session_state.website}
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

