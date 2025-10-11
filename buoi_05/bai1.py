from lxml import etree

def excuteXpathQuery():
    # Parse XML từ file
    tree = etree.parse('sv.xml')
    root = tree.getroot()
    
    print("\nTRUY VẤN XPATH VỚI LXML\n")
    
    # 1. Lấy tất cả sinh viên
    print("\n1. Tất cả sinh viên:")
    for student in root.xpath('//student'):
        print(f"{student.xpath('./id/text()')[0]}: {student.xpath('./name/text()')[0]}")
    
    # 2. Liệt kê tên tất cả sinh viên
    print("\n2. Tên tất cả sinh viên:")
    for name in enumerate(root.xpath('//student/name/text()'), 1):
        print(f"- {name}")
    
    # 3. Lấy tất cả id của sinh viên
    print("\n3. Tất cả ID sinh viên:")
    for id in root.xpath('//student/id/text()'):
        print(f"- {id}")
    
    # 4. Lấy ngày sinh của sinh viên có id = "SV01"
    print("\n4. Ngày sinh SV01:")
    date_sv01 = root.xpath("//student[id='SV01']/date/text()")[0]
    print(f"{date_sv01}")
    
    # 5. Lấy các khóa học
    print("\n5. Các khóa học:")
    for course in set(root.xpath('//enrollment/course/text()')):
        print(f"- {course}")
    
    # 6. Lấy toàn bộ thông tin của sinh viên đầu tiên
    print("\n6. Thông tin sinh viên đầu tiên:")
    first = root.xpath('//student[1]')[0]
    print(f"ID: {first.xpath('./id/text()')[0]}")
    print(f"Tên: {first.xpath('./name/text()')[0]}")
    print(f"Ngày sinh: {first.xpath('./date/text()')[0]}")
    
    # 7. Lấy mã sinh viên đăng ký khóa học "Vatly203"
    print("\n7. Mã SV đăng ký Vatly203:")
    for ref in root.xpath("//enrollment[course='Vatly203']/studentRef/text()"):
        print(f"- {ref}")
    
    # 8. Lấy tên sinh viên học môn "Toan101"
    print("\n8. Tên SV học Toan101:")
    for student_id in root.xpath("//enrollment[course='Toan101']/studentRef/text()"):
        name = root.xpath(f"//student[id='{student_id}']/name/text()")[0]
        print(f"- {name} ({student_id})")
    
    # 9. Lấy tên sinh viên học môn "Vatly203"
    print("\n9. Tên SV học Vatly203:")
    for student_id in root.xpath("//enrollment[course='Vatly203']/studentRef/text()"):
        name = root.xpath(f"//student[id='{student_id}']/name/text()")[0]
        print(f"- {name} ({student_id})")
    
    # 10. Lấy ngày sinh của sinh viên có id="SV01"
    print("\n10. Ngày sinh SV01:")
    sv01_date = root.xpath("//student[id='SV01']/date/text()")[0]
    print(f"{sv01_date}")
    
    # 11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997
    print("\n11. SV sinh năm 1997:")
    for student in root.xpath("//student[contains(date, '1997')]"):
        name = student.xpath('./name/text()')[0]
        date = student.xpath('./date/text()')[0]
        print(f"- {name}: {date}")
    
    # 12. Lấy tên của các sinh viên có ngày sinh trước năm 1998
    print("\n12. SV sinh trước 1998:")
    for student in root.xpath('//student[number(substring(date, 1, 4)) < 1998]'):
        name = student.xpath('./name/text()')[0]
        date = student.xpath('./date/text()')[0]
        print(f"- {name}: {date}")
    
    # 13. Đếm tổng số sinh viên
    print("\n13. Tổng số sinh viên:")
    count = root.xpath('count(//student)')
    print(f"{int(count)} sinh viên")
    
    # 14. Lấy sinh viên chưa đăng ký môn nào
    print("\n14. SV chưa đăng ký môn nào:")
    unregistered = root.xpath('//student[not(id = //enrollment/studentRef)]')
    for student in unregistered:
        print(f"- {student.xpath('./name/text()')[0]} ({student.xpath('./id/text()')[0]})")
    
    # 15. Lấy phần tử <date> anh em ngay sau <name> của SV01
    print("\n15. Date sau name của SV01:")
    date = root.xpath("//student[id='SV01']/name/following-sibling::date[1]/text()")
    print(f"{date[0]}" if date else "   Không tìm thấy")
    
    # 16. Lấy phần tử <id> anh em ngay trước <name> của SV02
    print("\n16. ID trước name của SV02:")
    id = root.xpath("//student[id='SV02']/name/preceding-sibling::id[1]/text()")
    print(f"{id[0]}" if id else "   Không tìm thấy")
    
    # 17. Lấy node <course> trong cùng enrollment với studentRef='SV03'
    print("\n17. Course của SV03:")
    for course in root.xpath("//enrollment[studentRef='SV03']/course/text()"):
        print(f"- {course}")
    
    # 18. Lấy sinh viên có họ là "Trần"
    print("\n18. SV họ Trần:")
    for student in root.xpath("//student[starts-with(name, 'Trần')]"):
        print(f"- {student.xpath('./name/text()')[0]} ({student.xpath('./id/text()')[0]})")
    
    # 19. Lấy năm sinh của sinh viên SV01
    print("\n19. Năm sinh SV01:")
    year = root.xpath("substring(//student[id='SV01']/date, 1, 4)")
    print(f"{year}")

if __name__ == "__main__":
    excuteXpathQuery()