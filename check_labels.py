import os

BASE_DIR = "dataset"
splits = ["train", "valid", "test"]

for split in splits:
    img_dir = os.path.join(BASE_DIR, split, "images")
    lbl_dir = os.path.join(BASE_DIR, split, "labels")

    removed = 0

    for label in os.listdir(lbl_dir):
        label_path = os.path.join(lbl_dir, label)

        if os.path.getsize(label_path) == 0:
            img_path = os.path.join(img_dir, label.replace(".txt", ".jpg"))

            os.remove(label_path)
            if os.path.exists(img_path):
                os.remove(img_path)

            removed += 1

    print(f"{split}: removed {removed} empty labels")
