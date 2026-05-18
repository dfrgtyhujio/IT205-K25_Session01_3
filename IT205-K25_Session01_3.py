print("=== HỆ THỐNG TIẾP NHẬN BỆNH ÁN ĐIỆN TỬ ===")
    
fullname = input("Nhập họ và tên bệnh nhân       : ")
medical_id = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám chỉ định  : ")

phieu_kham = f"Bệnh nhân: {fullname} - Mã BA: {medical_id} - Chuyển tới: {department}"
    
print(phieu_kham)