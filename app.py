import streamlit as st

# 1. Cấu hình tab trình duyệt
st.set_page_config(page_title="Tính thuế TNCN · Streamlit", page_icon="💰")

# 2. Hiển thị ảnh đại diện hình tròn (Giống ảnh đầu tiên)
# Bạn hãy thay link ảnh này bằng đường link ảnh cá nhân của bạn nếu muốn nhé
avatar_url = "https://unsplash.com" 
st.markdown(
    f"""
    <div style="display: flex; justify-content: left; margin-bottom: 20px;">
        <img src="{avatar_url}" style="width: 150px; height: 150px; border-radius: 10px; object-fit: cover;">
    </div>
    """,
    unsafe_allow_index=True
)

# 3. Tiêu đề lớn hiển thị đậm kèm TÊN CỦA BẠN (Bạn sửa chữ NGUYỄN VĂN A thành tên bạn)
st.markdown(
    """
    <h1 style="font-size: 38px; font-weight: 800; line-height: 1.3; color: #111111; margin-bottom: 5px;">
        💰 ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN_Trần Thị Diệu Linh 
    </h1>
    """, 
    unsafe_allow_index=True
)

# 4. Dòng chữ nhỏ mô tả dưới tiêu đề
st.write("thue luy tien tung phan.")
st.markdown("---")

# 5. Tiêu đề mục nhập thông tin cá nhân kèm Ghim đỏ
st.markdown(
    """
    <h2 style="font-size: 28px; font-weight: 700; margin-top: 10px; margin-bottom: 20px;">
        📌 Nhập thông tin cá nhân
    </h2>
    """, 
    unsafe_allow_index=True
)

# 6. Ô nhập Thu nhập chịu thuế (Mặc định 30 triệu giống ảnh 2)
thu_nhap = st.number_input(
    "Thu nhập chịu thuế/tháng (VNĐ)", 
    min_value=0, 
    value=30000000, 
    step=1000000,
    format="%d"
)

# 7. Ô nhập Khoản bảo hiểm bắt buộc (Mặc định 3.15 triệu giống ảnh 2)
bao_hiem = st.number_input(
    "Các khoản bảo hiểm bắt buộc (VNĐ)", 
    min_value=0, 
    value=3150000, 
    step=50000,
    format="%d"
)

# 8. Ô nhập Số người phụ thuộc
nguoi_phu_thuoc = st.number_input(
    "Số người phụ thuộc", 
    min_value=0, 
    value=0, 
    step=1,
    format="%d"
)

# 9. Nút bấm tính thuế
nut_tinh_thue = st.button("🗮 Tính thuế TNCN")

st.markdown("---")
# Dòng ghi chú dưới chân trang
st.write("*Ứng dụng tính thuế TNCN phục vụ mục đích học tập.*")

# --- KHỐI XỬ LÝ LOGIC TÍNH TOÁN ---
# Định mức giảm trừ năm 2026: Bản thân 15.5tr, Người phụ thuộc 6.2tr
GIAM_TRU_BAN_THAN = 15500000
GIAM_TRU_PHU_THUOC = nguoi_phu_thuoc * 6200000

# Thu nhập tính thuế = Thu nhập chịu thuế - Bảo hiểm - Các khoản giảm trừ
thu_nhap_tinh_thue = thu_nhap - bao_hiem - GIAM_TRU_BAN_THAN - GIAM_TRU_PHU_THUOC

if thu_nhap_tinh_thue < 0:
    thu_nhap_tinh_thue = 0

# Biểu thuế lũy tiến từng phần rút gọn năm 2026
def tinh_thue_tncn_2026(tntt):
    if tntt <= 10000000:
        return tntt * 0.05
    elif tntt <= 30000000:
        return tntt * 0.1 - 500000
    elif tntt <= 60000000:
        return tntt * 0.2 - 3500000
    elif tntt <= 100000000:
        return tntt * 0.3 - 9500000
    else:
        return tntt * 0.35 - 14500000

thue_phai_nop = tinh_thue_tncn_2026(thu_nhap_tinh_thue)

# 10. Hành động hiển thị kết quả khi bấm nút
if nut_tinh_thue:
    st.success(f"### 📊 Số thuế TNCN phải nộp: {thue_phai_nop:,.0f} VNĐ")
    with st.expander("Xem chi tiết các bước tính"):
        st.write(f"- Giảm trừ gia cảnh bản thân: {GIAM_TRU_BAN_THAN:,.0f} VNĐ")
        st.write(f"- Giảm trừ người phụ thuộc: {GIAM_TRU_PHU_THUOC:,.0f} VNĐ")
        st.write(f"- Bảo hiểm bắt buộc đã khấu trừ: {bao_hiem:,.0f} VNĐ")
        st.write(f"👉 **Thu nhập làm căn cứ tính thuế:** {thu_nhap_tinh_thue:,.0f} VNĐ")
        
