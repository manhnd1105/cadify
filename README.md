# Summary

Công cụ bóc tách khối lượng từ bản vẽ AutoCAD dùng trong ngành AEC (architecture, Engineering and Construction).

Các bước phân tích sơ bộ:
1. Đầu vào: bản vẽ AutoCAD (dwg) đặt trong mục `./dataset`
2. Chuyển đổi file thành định dạng DXF
3. Chuyển đổi và trích xuất dữ liệu (layer, entity, block). Xuất ra json có cấu trúc và ảnh PNG
4. Dùng Vision LLM phân tích hình ảnh bản vẽ. Phân loại: tường, cột, dầm, sàn, cửa, cầu thang...
5. Tính toán khối lượng. Đọc toạ độ, scale từ bản vẽ, tính ra diện tích, thể tích. Áp dụng hao hụt, định mức vật liệu theo TCVN
6. Dùng LLM xác minh và kiểm tra chéo. Đối chiếu logic tổng khối lượng, đơn vị, bỏ sót. Gắn cờ cảnh báo nếu phát hiện bất thường
7. Dùng LLM tổng hợp và trích xuất bảng khối lượng chuẩn: hạng mục, đơn vị, số lượng, ghi chú, giả định, nguôn tham chiếu
8. Xuất file đầu ra dạng markdown tại `./output`