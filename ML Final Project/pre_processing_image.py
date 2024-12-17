from PIL import Image
import csv
import numpy as np
import os


def resize_images(parent_names, output_csvs, shape):
    for parent_name, output_csv in zip(parent_names, output_csvs):

        if os.path.exists(output_csv):
            with open(output_csv, "r") as file:
                reader = csv.reader(file)
                header = next(reader, None)
                expected_columns = 1 + shape[0] * shape[1] * 3
                if header and header[0] == "label" and len(header) == expected_columns:
                    print(f"{output_csv} already exists and is valid. Skipping processing.")
                    continue

        all_image_data = []
        dirs = os.listdir(parent_name)
        for current_dir in dirs:
            dir_path = os.path.join(parent_name, current_dir)
            if os.path.isdir(dir_path):
                label = current_dir
                for file in os.listdir(dir_path):
                    if file.endswith(".ppm"):
                        file_path = os.path.join(dir_path, file)
                        image = Image.open(file_path)
                        image = image.resize(shape)
                        image_array = np.array(image)
                        flattened_array = image_array.flatten()
                        all_image_data.append(
                            [label] + flattened_array.tolist())

        if all_image_data:
            with open(output_csv, "w", newline="") as file:
                writer = csv.writer(file)
                header = ["label"] + \
                    [f"Pixel_{i}" for i in range(len(all_image_data[0]) - 1)]
                writer.writerow(header)
                writer.writerows(all_image_data)
