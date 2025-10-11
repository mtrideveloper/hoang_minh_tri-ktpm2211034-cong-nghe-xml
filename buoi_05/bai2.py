# vào thư mục buoi_05 chạy python bai2.py

from lxml import etree
import os

def get_namespace_from_xml(xml_path):
    """Lấy namespace trực tiếp từ file XML"""
    tree = etree.parse(xml_path)
    root = tree.getroot()
    
    # Lấy namespace từ root element
    namespace = root.nsmap[None] if None in root.nsmap else None
    
    return namespace, root, tree

current_dir = os.path.dirname(__file__)
xml_path = os.path.join(current_dir, '..', 'buoi_04', 'quanlybanan.xml')

namespace_uri, root, tree = get_namespace_from_xml(xml_path)
print(f"\nNamespace: {namespace_uri}")

# Tạo ns dict tự động
ns = {'ns': namespace_uri} if namespace_uri else None

# 1. Lấy tất cả bàn
print("\n1. Tất cả bàn:")
bans = root.xpath('//ns:BAN', namespaces=ns)
for ban in bans:
    soban = ban.xpath('./ns:SOBAN/text()', namespaces=ns)[0]
    tenban = ban.xpath('./ns:TENBAN/text()', namespaces=ns)[0]
    print(f"- Bàn {soban}: {tenban}")

# 2. Lấy tất cả nhân viên
print("\n2. Tất cả nhân viên:")
nhanviens = root.xpath('//ns:NHANVIEN', namespaces=ns)
for nv in nhanviens:
    manv = nv.xpath('./ns:MANV/text()', namespaces=ns)[0]
    tennv = nv.xpath('./ns:TENNV/text()', namespaces=ns)[0]
    print(f"- {manv}: {tennv}")

# 3. Lấy tất cả tên món
print("\n3. Tất cả tên món:")
tenmons = root.xpath('//ns:MON/ns:TENMON/text()', namespaces=ns)
for i, tenmon in enumerate(tenmons, 1):
    print(f"{i}. {tenmon}")

# 4. Lấy tên nhân viên có mã NV02
print("\n4. Tên nhân viên có mã NV02:")
ten_nv02 = root.xpath('//ns:NHANVIEN[ns:MANV="NV02"]/ns:TENNV/text()', namespaces=ns)
if ten_nv02:
    print(f"- {ten_nv02[0]}")

# 5. Lấy tên và số điện thoại của nhân viên NV03
print("\n5. Tên và số điện thoại của nhân viên NV03:")
nv03_info = root.xpath('//ns:NHANVIEN[ns:MANV="NV03"]', namespaces=ns)
if nv03_info:
    ten_nv03 = nv03_info[0].xpath('./ns:TENNV/text()', namespaces=ns)[0]
    sdt_nv03 = nv03_info[0].xpath('./ns:SDT/text()', namespaces=ns)[0]
    print(f"- Tên: {ten_nv03}")
    print(f"- SĐT: {sdt_nv03}")

# 6. Lấy tên món có giá > 50,000
print("\n6. Tên món có giá > 50,000:")
mon_gia_cao = root.xpath('//ns:MON[ns:GIA > 50000]/ns:TENMON/text()', namespaces=ns)
if mon_gia_cao:
    for mon in mon_gia_cao:
        print(f"- {mon}")
else:
    print("   - Không có món nào có giá > 50,000")

# 7. Lấy số bàn của hóa đơn HD03
print("\n7. Số bàn của hóa đơn HD03:")
soban_hd03 = root.xpath('//ns:HOADON[ns:SOHD="HD03"]/ns:SOBAN_THUOC/text()', namespaces=ns)
if soban_hd03:
    print(f"- Bàn số {soban_hd03[0]}")

# 8. Lấy tên món có mã M02
print("\n8. Tên món có mã M02:")
ten_mon_m02 = root.xpath('//ns:MON[ns:MAMON="M02"]/ns:TENMON/text()', namespaces=ns)
if ten_mon_m02:
    print(f"- {ten_mon_m02[0]}")

# 9. Lấy ngày lập của hóa đơn HD03
print("\n9. Ngày lập của hóa đơn HD03:")
ngaylap_hd03 = root.xpath('//ns:HOADON[ns:SOHD="HD03"]/ns:NGAYLAP/text()', namespaces=ns)
if ngaylap_hd03:
    print(f"- {ngaylap_hd03[0]}")

# 10. Lấy tất cả mã món trong hóa đơn HD01
print("\n10. Tất cả mã món trong hóa đơn HD01:")
mamons_hd01 = root.xpath('//ns:SOLUONG[ns:SOHD_THUOC="HD01"]/ns:MAMON_THUOC/text()', namespaces=ns)
if mamons_hd01:
    for mamon in mamons_hd01:
        print(f"- {mamon}")

# 11. Lấy tên món trong hóa đơn HD01
print("\n11. Tên món trong hóa đơn HD01:")
mamons_hd01 = root.xpath('//ns:SOLUONG[ns:SOHD_THUOC="HD01"]/ns:MAMON_THUOC/text()', namespaces=ns)
for mamon in mamons_hd01:
    tenmon = root.xpath(f'//ns:MON[ns:MAMON="{mamon}"]/ns:TENMON/text()', namespaces=ns)
    if tenmon:
        print(f"- {tenmon[0]}")

# 12. Lấy tên nhân viên lập hóa đơn HD02
print("\n12. Tên nhân viên lập hóa đơn HD02:")
manv_hd02 = root.xpath('//ns:HOADON[ns:SOHD="HD02"]/ns:MANV_LAP/text()', namespaces=ns)
if manv_hd02:
    tennv = root.xpath(f'//ns:NHANVIEN[ns:MANV="{manv_hd02[0]}"]/ns:TENNV/text()', namespaces=ns)
    if tennv:
        print(f"- {tennv[0]}")

# 13. Đếm số bàn
print("\n13. Đếm số bàn:")
count_ban = root.xpath('count(//ns:BAN)', namespaces=ns)
print(f"- {int(count_ban)} bàn")

# 14. Đếm số hóa đơn lập bởi NV01
print("\n14. Số hóa đơn lập bởi NV01:")
count_hd_nv01 = root.xpath('count(//ns:HOADON[ns:MANV_LAP="NV01"])', namespaces=ns)
print(f"- {int(count_hd_nv01)} hóa đơn")

# 15. Lấy tên tất cả món có trong hóa đơn của bàn số 2
print("\n15. Tên món có trong hóa đơn của bàn số 2:")
sohds_ban2 = root.xpath('//ns:HOADON[ns:SOBAN_THUOC="2"]/ns:SOHD/text()', namespaces=ns)
mamons_ban2 = set()
for sohd in sohds_ban2:
    mamons = root.xpath(f'//ns:SOLUONG[ns:SOHD_THUOC="{sohd}"]/ns:MAMON_THUOC/text()', namespaces=ns)
    mamons_ban2.update(mamons)

for mamon in mamons_ban2:
    tenmon = root.xpath(f'//ns:MON[ns:MAMON="{mamon}"]/ns:TENMON/text()', namespaces=ns)
    if tenmon:
        print(f"- {tenmon[0]}")

# 16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3
print("\n16. Nhân viên từng lập hóa đơn cho bàn số 3:")
manvs_ban3 = root.xpath('//ns:HOADON[ns:SOBAN_THUOC="3"]/ns:MANV_LAP/text()', namespaces=ns)
unique_manvs = set(manvs_ban3)
for manv in unique_manvs:
    tennv = root.xpath(f'//ns:NHANVIEN[ns:MANV="{manv}"]/ns:TENNV/text()', namespaces=ns)
    if tennv:
        print(f"- {tennv[0]}")

# 17. Lấy tất cả hóa đơn mà nhân viên nữ lập
print("\n17. Hóa đơn nhân viên nữ lập:")
manvs_nu = root.xpath('//ns:NHANVIEN[ns:GIOITINH="Nữ"]/ns:MANV/text()', namespaces=ns)
sohds_nu = []
for manv in manvs_nu:
    sohds = root.xpath(f'//ns:HOADON[ns:MANV_LAP="{manv}"]/ns:SOHD/text()', namespaces=ns)
    sohds_nu.extend(sohds)

for sohd in sohds_nu:
    print(f"- {sohd}")

# 18. Lấy tất cả nhân viên từng phục vụ bàn số 1
print("\n18. Nhân viên từng phục vụ bàn số 1:")
manvs_ban1 = root.xpath('//ns:HOADON[ns:SOBAN_THUOC="1"]/ns:MANV_LAP/text()', namespaces=ns)
unique_manvs_ban1 = set(manvs_ban1)
for manv in unique_manvs_ban1:
    tennv = root.xpath(f'//ns:NHANVIEN[ns:MANV="{manv}"]/ns:TENNV/text()', namespaces=ns)
    if tennv:
        print(f"- {tennv[0]}")

# 19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn
print("\n19. Món được gọi nhiều hơn 1 lần:")
mamons_nhieu = root.xpath('//ns:SOLUONG[ns:SOLUONG > 1]/ns:MAMON_THUOC/text()', namespaces=ns)
unique_mamons_nhieu = set(mamons_nhieu)
for mamon in unique_mamons_nhieu:
    tenmon = root.xpath(f'//ns:MON[ns:MAMON="{mamon}"]/ns:TENMON/text()', namespaces=ns)
    if tenmon:
        print(f"- {tenmon[0]}")

# 20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'
print("\n20. Tên bàn và ngày lập hóa đơn HD02:")
soban_hd02 = root.xpath('//ns:HOADON[ns:SOHD="HD02"]/ns:SOBAN_THUOC/text()', namespaces=ns)
ngaylap_hd02 = root.xpath('//ns:HOADON[ns:SOHD="HD02"]/ns:NGAYLAP/text()', namespaces=ns)

if soban_hd02 and ngaylap_hd02:
    tenban = root.xpath(f'//ns:BAN[ns:SOBAN="{soban_hd02[0]}"]/ns:TENBAN/text()', namespaces=ns)
    if tenban:
        print(f"- Tên bàn: {tenban[0]}")
        print(f"- Ngày lập: {ngaylap_hd02[0]}")