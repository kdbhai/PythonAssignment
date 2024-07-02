import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, filename)
                if os.path.exists(dest_file):
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    dest_file = os.path.join(dest_dir, f"{filename}_{timestamp}")
                shutil.copy2(source_file, dest_file)
                print(f"Copied '{source_file}' to '{dest_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        backup_files(source_dir, dest_dir)
