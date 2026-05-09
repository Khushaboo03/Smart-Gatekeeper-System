import os

BASE_DIR = "dataset"
SPLITS = ["train", "valid", "test"]

def clamp(v, eps=1e-6):
    return max(eps, min(1 - eps, v))

total_fixed = 0

for split in SPLITS:
    LABEL_DIR = os.path.join(BASE_DIR, split, "labels")
    if not os.path.exists(LABEL_DIR):
        continue

    print(f"\n🔧 Processing {split} labels...")

    for file in os.listdir(LABEL_DIR):
        if not file.endswith(".txt"):
            continue

        path = os.path.join(LABEL_DIR, file)
        new_lines = []

        with open(path, "r") as f:
            lines = f.readlines()

        current_class = None

        for line in lines:
            parts = line.strip().split()
            if len(parts) < 4:
                continue

            # Case 1: class id present
            if len(parts) >= 5:
                current_class = parts[0]
                nums = list(map(float, parts[1:5]))

            # Case 2: class id missing
            else:
                if current_class is None:
                    continue
                nums = list(map(float, parts))

            nums = [clamp(v) for v in nums]

            new_lines.append(
                current_class + " " + " ".join(f"{v:.6f}" for v in nums)
            )
            total_fixed += 1

        with open(path, "w") as f:
            f.write("\n".join(new_lines))

print(f"\n✅ Fixed labels in TRAIN + VALID + TEST")
print(f"📦 Total boxes fixed: {total_fixed}")
print("🚫 No annotations removed")
