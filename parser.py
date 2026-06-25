import ezdxf
import json
from ezdxf.math import Vec3

def extract_coords(entity):
    """Trích xuất tọa độ từ các loại entity AutoCAD phổ biến"""
    dxftype = entity.dxftype()
    
    if dxftype == 'LINE':
        return [
            (entity.dxf.start.x, entity.dxf.start.y),
            (entity.dxf.end.x,   entity.dxf.end.y),
        ]
    
    elif dxftype == 'LWPOLYLINE':
        # Trả về list (x, y) từ các đỉnh
        return [(p[0], p[1]) for p in entity.get_points()]
    
    elif dxftype == 'POLYLINE':
        return [(v.dxf.location.x, v.dxf.location.y) for v in entity.vertices]
    
    elif dxftype == 'CIRCLE':
        c = entity.dxf.center
        return [('center', c.x, c.y), ('radius', entity.dxf.radius)]
    
    elif dxftype == 'ARC':
        c = entity.dxf.center
        return [
            ('center', c.x, c.y),
            ('radius',      entity.dxf.radius),
            ('start_angle', entity.dxf.start_angle),
            ('end_angle',   entity.dxf.end_angle),
        ]
    
    elif dxftype == 'INSERT':
        # Block reference — trả về điểm chèn + tên block
        ins = entity.dxf.insert
        return [('insert', ins.x, ins.y), ('block', entity.dxf.name)]
    
    elif dxftype == 'TEXT':
        p = entity.dxf.insert
        return [('position', p.x, p.y), ('text', entity.dxf.text)]
    
    elif dxftype == 'MTEXT':
        p = entity.dxf.insert
        return [('position', p.x, p.y), ('text', entity.text)]
    
    elif dxftype == 'SPLINE':
        # Lấy các control points
        return [(p.x, p.y) for p in entity.control_points]
    
    elif dxftype == 'HATCH':
        # Lấy boundary paths
        coords = []
        for path in entity.paths:
            if hasattr(path, 'vertices'):
                coords.extend([(v[0], v[1]) for v in path.vertices])
        return coords
    
    else:
        # Fallback — thử lấy dxf.insert hoặc dxf.start nếu có
        coords = []
        for attr in ('insert', 'start', 'center'):
            if entity.dxf.hasattr(attr):
                pt = getattr(entity.dxf, attr)
                coords.append((pt.x, pt.y))
                break
        return coords
    
def parse_dwg(filepath):
    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()
    
    entities = []
    for entity in msp:
        if entity.dxftype() in ['LINE', 'LWPOLYLINE', 'CIRCLE', 'ARC', 'INSERT']:
            entities.append({
                "type": entity.dxftype(),
                "layer": entity.dxf.layer,
                "coords": extract_coords(entity),
            })
    
    return {
        "layers": list(doc.layers),
        "entities": entities,
        "units": doc.header.get("$INSUNITS", 4),  # 4 = mm
    }