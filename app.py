import streamlit as st

st.set_page_config(
    page_title="Ứng dụng tính thuế TNCN",
    page_icon="💰",
    layout="centered"
)

st.image("Screenshot_2026-06-16-15-36-34-273_com.miui.gallery-edit.jpg")
st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN - Trần Thị Diệu Linh")
st.write(
    "Ứng dụng hỗ trợ tính thuế thu nhập cá nhân "
    "đối với người có thu nhập từ tiền lương, tiền công."
)

st.divider()

st.header("📌 Nhập thông tin")

luong_bhxh = st.number_input(
    "Mức lương đóng BHXH (VNĐ)",
    min_value=0,
    value=10000000,
    step=100000
)

thuong = st.number_input(
    "Tiền thưởng/Phụ cấp khác (VNĐ)",
    min_value=0,
    value=20000000,
    step=100000
)

so_nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc",
    min_value=0,
    value=0,
    step=1
)

tong_thu_nhap = luong_bhxh + thuong

st.info(
    f"💵 Tổng thu nhập tháng: {tong_thu_nhap:,.0f} VNĐ"
)

if st.button("🧮 Tính thuế TNCN"):

    # ======================
    # BẢO HIỂM NGƯỜI LAO ĐỘNG
    # ======================
    bhxh = luong_bhxh * 0.08
    bhyt = luong_bhxh * 0.015
    bhtn = luong_bhxh * 0.01

    tong_bao_hiem = bhxh + bhyt + bhtn

    # ======================
    # GIẢM TRỪ GIA CẢNH
    # ======================
    giam_tru_ban_than = 15_500_000
    giam_tru_phu_thuoc = (
        so_nguoi_phu_thuoc * 6_200_000
    )

    # ======================
    # THU NHẬP TÍNH THUẾ
    # ======================
    thu_nhap_tinh_thue = (
        tong_thu_nhap
        - tong_bao_hiem
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue < 0:
        thu_nhap_tinh_thue = 0

    # ======================
    # THUẾ LŨY TIẾN 5 BẬC
    # ======================
    if thu_nhap_tinh_thue <= 10_000_000:
        thue = thu_nhap_tinh_thue * 0.05

    elif thu_nhap_tinh_thue <= 30_000_000:
        thue = (
            500_000
            + (thu_nhap_tinh_thue - 10_000_000)
            * 0.10
        )

    elif thu_nhap_tinh_thue <= 60_000_000:
        thue = (
            2_500_000
            + (thu_nhap_tinh_thue - 30_000_000)
            * 0.20
        )

    elif thu_nhap_tinh_thue <= 100_000_000:
        thue = (
            8_500_000
            + (thu_nhap_tinh_thue - 60_000_000)
            * 0.30
        )

    else:
        thue = (
            20_500_000
            + (thu_nhap_tinh_thue - 100_000_000)
            * 0.35
        )

    # ======================
    # THU NHẬP THỰC NHẬN
    # ======================
    thu_nhap_thuc_nhan = (
        tong_thu_nhap
        - tong_bao_hiem
        - thue
    )

    st.divider()
    st.header("📊 Kết quả")

    st.write(f"BHXH (8%): {bhxh:,.0f} VNĐ")
    st.write(f"BHYT (1,5%): {bhyt:,.0f} VNĐ")
    st.write(f"BHTN (1%): {bhtn:,.0f} VNĐ")
    st.write(
        f"💰 Tổng bảo hiểm: {tong_bao_hiem:,.0f} VNĐ"
    )

    st.write(
        f"Giảm trừ bản thân: "
        f"{giam_tru_ban_than:,.0f} VNĐ"
    )

    st.write(
        f"Giảm trừ người phụ thuộc: "
        f"{giam_tru_phu_thuoc:,.0f} VNĐ"
    )

    st.write(
        f"Thu nhập tính thuế: "
        f"{thu_nhap_tinh_thue:,.0f} VNĐ"
    )

    st.success(
        f"💸 Thuế TNCN phải nộp: "
        f"{thue:,.0f} VNĐ"
    )

    st.success(
        f"💵 Thu nhập thực nhận: "
        f"{thu_nhap_thuc_nhan:,.0f} VNĐ"
    )

st.divider()
st.caption(
    "Ứng dụng tính thuế TNCN phục vụ mục đích học tập."
        )
