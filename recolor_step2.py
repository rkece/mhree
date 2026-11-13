#!/usr/bin/env python3
"""Step 2: maroon + rose-gold colour replacement. Usage: python recolor_step2.py index.html"""
import re, sys, shutil

path = sys.argv[1] if len(sys.argv) > 1 else "index.html"
shutil.copy(path, path + ".bak")          # backup first
src = open(path, encoding="utf-8").read()

HEX = {
 "#F3D293":"#E8B4A0", "#FCE8C3":"#FFE0D6",
 "#C99E53":"#B5766A", "#CFA559":"#B5766A", "#D4A95B":"#B5766A", "#D5A85E":"#B5766A",
 "#FF7A30":"#D9485F", "#F97316":"#D9485F",
 "#FF9BB2":"#FF8FA3", "#B39DDB":"#A8324F", "#7DD3FC":"#F4A6B7",
 "#8B486F":"#7A1F3D", "#5E347E":"#5A0F2B", "#5E2E49":"#4A0E22",
 "#06040A":"#12040A", "#07050F":"#12040A", "#07060B":"#12040A",
 "#0E0919":"#2A0610", "#120D1A":"#2A0610", "#160F25":"#2A0610",
 "#140E24":"#2A0A16", "#150E23":"#2A0A16", "#18102B":"#2A0A16", "#0F0B1A":"#2A0A16",
 "#1C142E":"#3A0C1E", "#23163C":"#3A0C1E", "#1D1036":"#3A0C1E",
 "#2A1D44":"#4A1228", "#3B285E":"#4A1228", "#35213E":"#4A1228",
}
RGBA = {
 "243,210,147":"232,180,160", "255,122,48":"217,72,95", "255,155,178":"255,143,163",
 "139,72,111":"122,31,61", "94,52,126":"90,15,43",
 "18,12,30":"46,10,22", "14,9,25":"46,10,22",
 "36,22,60":"70,14,32", "38,22,65":"70,14,32", "42,28,68":"70,14,32",
 "9,6,16":"18,4,10", "7,5,14":"18,4,10", "7,5,15":"18,4,10", "5,3,10":"18,4,10",
}

n = 0
for old, new in HEX.items():
    src, c = re.subn(re.escape(old) + r"(?![0-9A-Fa-f])", new, src, flags=re.I); n += c
for old, new in RGBA.items():
    src, c = re.subn(r"rgba\(\s*" + re.escape(old).replace(",", r"\s*,\s*") + r"\s*,", f"rgba({new},", src); n += c

open(path, "w", encoding="utf-8").write(src)
print(f"Done: {n} replacements. Backup saved as {path}.bak")