import os
import shutil
import random
import glob

def organize_plate_dataset():
    raw_dir = 'raw_data'
    target_root = 'Plate_Detection'
    
    # Check if raw_data exists
    if not os.path.exists(raw_dir):
        print(f"Error: {raw_dir} folder not found. Please add .jpg images and .txt labels.")
        return
    
    # Find all .jpg images
    image_paths = sorted(glob.glob(os.path.join(raw_dir, '*.jpg')))
    if not image_paths:
        print(f"No .jpg files found in {raw_dir}.")
        return
    
    # Pair with labels
    pairs = []
    for img_path in image_paths:
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        label_path = os.path.join(raw_dir, base_name + '.txt')
        if os.path.exists(label_path):
            pairs.append((img_path, label_path))
        else:
            print(f"Warning: No label for {os.path.basename(img_path)}")
    
    if not pairs:
        print("No matching image-label pairs found.")
        return
    
    # Shuffle
    random.shuffle(pairs)
    n = len(pairs)
    train_count = int(0.7 * n)
    val_count = int(0.2 * n)
    test_count = n - train_count - val_count
    
    # Create directories
    for split in ['train', 'val', 'test']:
        os.makedirs(os.path.join(target_root, split, 'images'), exist_ok=True)
        os.makedirs(os.path.join(target_root, split, 'labels'), exist_ok=True)
    
    # Move files
    train_pairs = pairs[:train_count]
    val_pairs = pairs[train_count:train_count + val_count]
    test_pairs = pairs[train_count + val_count:]
    
    splits = {'train': train_pairs, 'val': val_pairs, 'test': test_pairs}
    
    for split_name, split_pairs in splits.items():
        for img_path, label_path in split_pairs:
            shutil.move(img_path, os.path.join(target_root, split_name, 'images', os.path.basename(img_path)))
            shutil.move(label_path, os.path.join(target_root, split_name, 'labels', os.path.basename(label_path)))
    
    # Print counts
    print(f"Dataset organized successfully!")
    print(f"Train: {len(train_pairs)} pairs")
    print(f"Val: {len(val_pairs)} pairs")
    print(f"Test: {len(test_pairs)} pairs")
    
    # Generate YAML
    yaml_content = f"""path: ./{target_root}
train: train/images
val: val/images
test: test/images

nc: 1
names: ['license_plate']
"""
    yaml_path = os.path.join(target_root, 'plate_data.yaml')
    with open(yaml_path, 'w') as f:
        f.write(yaml_content)
    
    print(f"Generated {yaml_path}")

if __name__ == '__main__':
    organize_plate_dataset()

