import json

def generate(quantities_data, project_info):
    prompt = f"""
Dựa trên dữ liệu khối lượng đã tính toán:
{json.dumps(quantities_data, ensure_ascii=False, indent=2)}

Hãy tạo bảng bóc tách khối lượng theo chuẩn Việt Nam với định dạng Markdown:
- Chia theo hạng mục công việc (phần thô, hoàn thiện, MEP)
- Cột: STT | Tên công việc | Đơn vị | Số lượng | Ghi chú
- Ghi rõ giả định và hệ số hao hụt áp dụng
- Tham chiếu định mức theo TCVN/Thông tư 12/2021/TT-BXD

Dự án: {project_info}
"""