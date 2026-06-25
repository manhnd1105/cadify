from shapely.geometry import Polygon, LineString
import math

def calculate_quantities(elements, scale_factor):
    """scale_factor: mm/unit từ bản vẽ"""
    results = []
    
    for el in elements:
        qty = {}
        
        if el["type"] == "WALL":
            length = LineString(el["coords"]).length * scale_factor / 1000  # m
            qty = {
                "dien_tich": round(length * el["height"], 2),  # m²
                "the_tich": round(length * el["height"] * el["thickness"], 3),  # m³
            }
        
        elif el["type"] == "FLOOR_SLAB":
            poly = Polygon(el["coords"])
            area = poly.area * (scale_factor/1000)**2
            qty = {
                "dien_tich": round(area, 2),
                "the_tich": round(area * el["thickness"], 3),
            }
        
        results.append({**el, "khoi_luong": qty})
    
    return results