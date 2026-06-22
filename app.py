import streamlit as st

st.set_page_config(
    page_title="Ứng dụng tính thuế TNCN",
    page_icon="💰",
    layout="centered"
)

st.image("Screenshot_2026-06-16-15-36-34-273_com.miui.gallery-edit.jpg")
st.title("💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN - Trần Thị Diệu Linh")
st.write(
    "Hỗ trợ tính thuế thu nhập cá nhân và các khoản bảo hiểm "
    "cho người lao động và người sử dụng lao động."
)

st.divider()

doi_tuong = st.radio(
    "👤 Chọn đối tượng",
    ["Người lao động", "Người sử dụng lao động"]
)

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

if st.button("🧮 Tính toán"):

    st.divider()

    # =========================
    # NGƯỜI LAO ĐỘNG
    # =========================
    if doi_tuong == "Người lao động":

        bhxh = luong_bhxh * 0.08
        bhyt = luong_bhxh * 0.015
        bhtn = luong_bhxh * 0.01

        tong_bao_hiem = bhxh + bhyt + bhtn

        giam_tru_ban_than = 15_500_000
        giam_tru_phu_thuoc = (
            so_nguoi_phu_thuoc * 6_200_000
        )

        thu_nhap_tinh_thue = (
            tong_thu_nhap
            - tong_bao_hiem
            - giam_tru_ban_than
            - giam_tru_phu_thuoc
        )

        if thu_nhap_tinh_thue < 0:
            thu_nhap_tinh_thue = 0

        # Thuế lũy tiến 5 bậc
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

        thu_nhap_thuc_nhan = (
            tong_thu_nhap
            - tong_bao_hiem
            - thue
        )

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

    # =========================
    # NGƯỜI SỬ DỤNG LAO ĐỘNG
    # =========================
    else:

        huu_tri = luong_bhxh * 0.14
        om_dau = luong_bhxh * 0.03
        tai_nan = luong_bhxh * 0.005
        bhtn = luong_bhxh * 0.01
        bhyt = luong_bhxh * 0.03

        tong_dong = (
            huu_tri
            + om_dau
            + tai_nan
            + bhtn
            + bhyt
        )

        tong_chi_phi = (
            tong_thu_nhap
            + tong_dong
        )

        st.header("📊 Kết quả")

        st.write(
            f"Hưu trí, tử tuất (14%): "
            f"{huu_tri:,.0f} VNĐ"
        )

        st.write(
            f"Ốm đau, thai sản (3%): "
            f"{om_dau:,.0f} VNĐ"
        )

        st.write(
            f"Tai nạn lao động (0,5%): "
            f"{tai_nan:,.0f} VNĐ"
        )

        st.write(
            f"BHTN (1%): {bhtn:,.0f} VNĐ"
        )

        st.write(
            f"BHYT (3%): {bhyt:,.0f} VNĐ"
        )

        st.success(
            f"🏢 Tổng doanh nghiệp phải đóng: "
            f"{tong_dong:,.0f} VNĐ"
        )

        st.success(
            f"💰 Tổng chi phí lao động: "
            f"{tong_chi_phi:,.0f} VNĐ"
        )

st.divider()
st.caption(
    "Ứng dụng phục vụ mục đích học tập."
)
