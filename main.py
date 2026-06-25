import parser
import identity
import calculation
import output_generator
import converter
import os

INPUT_FILE_PATH = "./dataset/01. XS. Workshop mo rong - Nen xe trolley.dwg"
OUTPUT_FILE_PATH = "./output/01. XS. Workshop mo rong - Nen xe trolley.md"
if not os.path.isfile(INPUT_FILE_PATH):
    print("File path not found")
    
dxf_file_path = converter.convert_file(INPUT_FILE_PATH)
metadata = parser.parse_dwg(dxf_file_path)
elements = identity.identify_elements(dxf_file_path, metadata)
calculation_result = calculation.calculate_quantities(elements, 1)
output = output_generator.generate(calculation_result, "Du an moi")

with open(OUTPUT_FILE_PATH, "w") as f:
    f.write(output)
    print(f"Output file generated at {OUTPUT_FILE_PATH}")
