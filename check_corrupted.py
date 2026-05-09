import os

img_dir = "dataset/train/images"
lbl_dir = "dataset/train/labels"

for label in os.listdir(lbl_dir):
    label_path = os.path.join(lbl_dir, label)
    if os.path.getsize(label_path) == 0:
        img_path = os.path.join(img_dir, label.replace(".txt", ".jpg"))
        os.remove(label_path)
        if os.path.exists(img_path):
            os.remove(img_path)

print("Empty labels removed")
