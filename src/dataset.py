import os
import random
import shutil

# FIX 1: Correct base path
BASE_DIR = "../dataset"

IMAGE_DIR = os.path.join(BASE_DIR, "train/images")
LABEL_DIR = os.path.join(BASE_DIR, "train/labels")

# Create valid & test folders
for split in ["valid", "test"]:
    os.makedirs(os.path.join(BASE_DIR, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, split, "labels"), exist_ok=True)

# Read only image files
images = [f for f in os.listdir(IMAGE_DIR) if f.endswith((".jpg", ".png", ".jpeg"))]

random.shuffle(images)

total = len(images)
valid_count = int(0.2 * total)
test_count = int(0.1 * total)

valid_images = images[:valid_count]
test_images = images[valid_count:valid_count + test_count]

def move_files(image_list, split):
    for img in image_list:
        label = os.path.splitext(img)[0] + ".txt"   #converts img-> .txt

        shutil.move(
            os.path.join(IMAGE_DIR, img),
            os.path.join(BASE_DIR, split, "images", img)
        )

        shutil.move(
            os.path.join(LABEL_DIR, label),
            os.path.join(BASE_DIR, split, "labels", label)
        )

move_files(valid_images, "valid")
move_files(test_images, "test")

print("✅ Dataset split completed successfully")
print(f"Train images left: {len(os.listdir(IMAGE_DIR))}")
print(f"Valid images: {len(os.listdir(os.path.join(BASE_DIR,'valid/images')))}")
print(f"Test images: {len(os.listdir(os.path.join(BASE_DIR,'test/images')))}")
