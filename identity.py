import anthropic, base64
import json

def identify_elements(image_path, entities_json):
    client = anthropic.Anthropic()
    
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode()
    
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "base64", "media_type": "image/png", "data": img_b64}
                },
                {
                    "type": "text",
                    "text": f"""Phân tích bản vẽ xây dựng này và dữ liệu layer:
{json.dumps(entities_json, ensure_ascii=False)}

Hãy nhận diện và phân loại các cấu kiện:
- Tường (gạch/bê tông), cột, dầm, sàn
- Cửa đi, cửa sổ, cầu thang
- Hệ thống MEP (nếu có)

Trả về JSON với danh sách cấu kiện, tọa độ, layer tương ứng."""
                }
            ]
        }]
    )
    return json.loads(response.content[0].text)