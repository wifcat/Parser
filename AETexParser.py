#   tools made for bully ae modder
#   coded by Ateris https://youtube.com/c/zenichen 
#   usage: python AETexParser.py
#          the base.tex *must* be on the same folder with AETexParser.py, base.tex and aa.py 
#          the aa.py is your dds2tex conversion file, rename it to aa.py
#   discord: wifcat
#   donate: https://saweria.co/ateris
#   github: https://github.com/wifcat

import os
import subprocess
import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "output")
aa_py = os.path.join(base_dir, "aa.py") # make sure your dds2tex.py is the same like this
base_tex = os.path.join(base_dir, "base.tex") # copy one from bully ae obb and rename it to base.tex

# If tex file exist
if not os.path.exists(base_tex):
    print("base.tex not found!")
    exit()

# output folde
os.makedirs(output_dir, exist_ok=True)

# find the dds file that are in the same dir
dds_files = [f for f in os.listdir(base_dir) if f.lower().endswith(".dds")]

if not dds_files:
    print("No dds file found")
    exit()

for dds in dds_files:
    input_path = os.path.join(base_dir, dds)
    filename_no_ext = os.path.splitext(dds)[0]
    final_output_path = os.path.join(output_dir, filename_no_ext + ".tex")

    # overwrite base.tex file name to its dds file name to: /output
    cmd = ["python", aa_py, "-i", input_path, "-o", base_tex, "-c"]

    print(f"\nPARSING {dds} -> base.tex -> output/{filename_no_ext}.tex ...")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"ERROR!:\n{result.stderr}")
            continue

        # the base.tex used for the base tex 
        shutil.copy(base_tex, final_output_path)
        print(f"Converted to {final_output_path}")

    except Exception as e:
        print(f"Error {dds}: {e}")

