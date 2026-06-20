import streamlit as st

st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN - Trần Thị Diệu Linh")
st.image("Screenshot_2026-06-16-15-36-34-273_com.miui.gallery-edit.jpg")
thu_nhap = st.number_input(
    "Thu nhập chịu thuế/tháng (VNĐ)",
    min_value=0,
    value=30000000
)

bao_hiem = st.number_input(
    "Các khoản bảo hiểm bắt buộc (VNĐ)",
    min_value=0,
    value=3150000
)

nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0
)

if st.button("🧮 Tính thuế TNCN"):

    # Giảm trừ bản thân
    giam_tru_ban_than = 11000000

    # Giảm trừ người phụ thuộc
    giam_tru_phu_thuoc = nguoi_phu_thuoc * 4400000

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap
        - bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue <= 0:
        thue = 0
    elif thu_nhap_tinh_thue <= 5000000:
        thue = thu_nhap_tinh_thue * 0.05
    elif thu_nhap_tinh_thue <= 10000000:
        thue = 250000 + (thu_nhap_tinh_thue - 5000000) * 0.1
    elif thu_nhap_tinh_thue <= 18000000:
        thue = 750000 + (thu_nhap_tinh_thue - 10000000) * 0.15
    elif thu_nhap_tinh_thue <= 32000000:
        thue = 1950000 + (thu_nhap_tinh_thue - 18000000) * 0.2
    elif thu_nhap_tinh_thue <= 52000000:
        thue = 4750000 + (thu_nhap_tinh_thue - 32000000) * 0.25
    elif thu_nhap_tinh_thue <= 80000000:
        thue = 9750000 + (thu_nhap_tinh_thue - 52000000) * 0.3
    else:
        thue = 18150000 + (thu_nhap_tinh_thue - 80000000) * 0.35

    st.success(f"Thu nhập tính thuế: {thu_nhap_tinh_thue:,.0f} VNĐ")
    st.success(f"Thuế TNCN phải nộp: {thue:,.0f} VNĐ")
    st.success(f"Thu nhập sau thuế: {thu_nhap - bao_hiem - thue:,.0f} VNĐ")
