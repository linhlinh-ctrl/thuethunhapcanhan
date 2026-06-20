import streamlit as st

st.set_page_config(
    page_title="Ứng dụng tính thuế TNCN",
    page_icon="💰",
    layout="centered"
)

st.image("Screenshot_2026-06-16-15-36-34-273_com.miui.gallery-edit.jpg")
st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN - Trần Thị Diệu Linh")
st.write(
    "Tính thuế thu nhập cá nhân từ tiền lương, tiền công theo biểu thuế lũy tiến từng phần."
)

st.divider()

st.header("📌 Nhập thông tin cá nhân")

luong = st.number_input(
    "Thu nhập tháng (VNĐ)",
    min_value=0,
    value=30000000,
    step=100000
)

so_nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

if st.button("🧮 Tính thuế TNCN"):

    # TÍNH BẢO HIỂM
    bhxh = luong * 0.08
    bhyt = luong * 0.015
    bhtn = luong * 0.01

    tong_bao_hiem = bhxh + bhyt + bhtn

    # GIẢM TRỪ GIA CẢNH
    giam_tru_ban_than = 15_500_000
    giam_tru_nguoi_phu_thuoc = so_nguoi_phu_thuoc * 6_200_000

    # THU NHẬP TÍNH THUẾ
    thu_nhap_tinh_thue = (
        luong
        - tong_bao_hiem
        - giam_tru_ban_than
        - giam_tru_nguoi_phu_thuoc
    )

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # TÍNH THUẾ LŨY TIẾN 5 BẬC
    thue = 0

    if thu_nhap_tinh_thue <= 10_000_000:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30_000_000:
        thue = (
            10_000_000 * 0.05
            + (thu_nhap_tinh_thue - 10_000_000) * 0.10
        )

    elif thu_nhap_tinh_thue <= 60_000_000:
        thue = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + (thu_nhap_tinh_thue - 30_000_000) * 0.20
        )

    elif thu_nhap_tinh_thue <= 100_000_000:
        thue = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + 30_000_000 * 0.20
            + (thu_nhap_tinh_thue - 60_000_000) * 0.30
        )

    else:
        thue = (
            10_000_000 * 0.05
            + 20_000_000 * 0.10
            + 30_000_000 * 0.20
            + 40_000_000 * 0.30
            + (thu_nhap_tinh_thue - 100_000_000) * 0.35
        )

    thu_nhap_sau_thue = luong - tong_bao_hiem - thue

    st.divider()
    st.header("📊 Kết quả")

    st.write(f"**BHXH (8%)**: {bhxh:,.0f} VNĐ")
    st.write(f"**BHYT (1,5%)**: {bhyt:,.0f} VNĐ")
    st.write(f"**BHTN (1%)**: {bhtn:,.0f} VNĐ")
    st.write(f"**Tổng bảo hiểm (10,5%)**: {tong_bao_hiem:,.0f} VNĐ")

    st.write(
        f"**Giảm trừ bản thân**: {giam_tru_ban_than:,.0f} VNĐ"
    )

    st.write(
        f"**Giảm trừ người phụ thuộc**: {giam_tru_nguoi_phu_thuoc:,.0f} VNĐ"
    )

    st.write(
        f"**Thu nhập tính thuế**: {thu_nhap_tinh_thue:,.0f} VNĐ"
    )

    st.success(
        f"💸 Thuế TNCN phải nộp: {thue:,.0f} VNĐ"
    )

    st.success(
        f"💵 Thu nhập sau thuế: {thu_nhap_sau_thue:,.0f} VNĐ"
    )

st.divider()
st.caption("Ứng dụng tính thuế TNCN phục vụ mục đích học tập.")
