import os
import shutil

def delete_pycache_and_pyc_files(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip .venv and its subdirectories
        if '.venv' in dirpath.split(os.sep):
            continue

        # Delete __pycache__ directories
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            print(f"Deleting folder: {pycache_path}")
            shutil.rmtree(pycache_path)
            dirnames.remove('__pycache__')  # Prevent walking into deleted dir

        # Delete .pyc and .pyo files
        for filename in filenames:
            if filename.endswith('.pyc') or filename.endswith('.pyo'):
                file_path = os.path.join(dirpath, filename)
                print(f"Deleting file: {file_path}")
                os.remove(file_path)

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    delete_pycache_and_pyc_files(root)
