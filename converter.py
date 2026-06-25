import os
import subprocess
OUT_DIR = "./output/tmp/"

def convert_file(filepath):
    os.makedirs(OUT_DIR, exist_ok=True)
    subprocess.run([
        'ODAFileConverter', os.path.dirname(filepath),
        OUT_DIR, 'ACAD2018', 'DXF', '0', '1'
    ], check=True)
    dxf_path = OUT_DIR + os.path.basename(filepath).replace('.dwg', '.dxf')
    return dxf_path