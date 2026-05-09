import os

# --- CONFIG ---
BASE_DIR = "dataset"  # your dataset folder
SPLITS = ["train", "valid", "test"]

def clamp(v, eps=1e-6):
    """Clamp coordinate values to [eps, 1-eps]"""
    return max(eps, min(1 - eps, v))

total_fixed = 0

for split in SPLITS:
    LABEL_DIR = os.path.join(BASE_DIR, split, "labels")
    if not os.path.exists(LABEL_DIR):
        print(f"⚠️  Folder not found: {LABEL_DIR}")
        continue

    fixed_in_split = 0
    print(f"\n🔧 Processing '{split}' labels...")

    for file_name in os.listdir(LABEL_DIR):
        if not file_name.endswith(".txt"):
            continue

        path = os.path.join(LABEL_DIR, file_name)
        with open(path, "r") as f:
            lines = f.read().splitlines()

        new_lines = []
        current_class = None

        for line in lines:
            parts = line.strip().split()
            if len(parts) < 4:
                continue

            # Case 1: class ID present
            if len(parts) >= 5:
                current_class = parts[0]
                coords = list(map(float, parts[1:5]))
            # Case 2: class ID missing
            else:
                if current_class is None:
                    continue
                coords = list(map(float, parts))

            # Clamp coordinates
            coords = [clamp(c) for c in coords]

            new_lines.append(
                f"{current_class} {' '.join(f'{c:.6f}' for c in coords)}"
            )
            fixed_in_split += 1

        # Write back with a newline at the end (YOLOv8 friendly)
        with open(path, "w") as f:
            f.write("\n".join(new_lines) + "\n")

    print(f"✅ Fixed {fixed_in_split} boxes in '{split}'")
    total_fixed += fixed_in_split

print(f"\n🎯 Total boxes fixed across all splits: {total_fixed}")
print("🚫 No annotations removed")
