import os
import shutil

def organize_downloads(download_folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.docx', '.xlsx', '.pptx', '.txt', '.md', '.csv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
        'Archives': ['.zip', '.rar', '.tar.gz', '.7z'],
        'Scripts': ['.py', '.js', '.sh', '.bat', '.sql'],
        'Executables': ['.exe', '.msi', '.bin']
    }
    for file in os.listdir(download_folder):
        if os.path.isfile(os.path.join(download_folder, file)):
            file_ext = os.path.splitext(file)[1].lower()
            destination_folder = next((ftype for ftype, exts in file_types.items() if file_ext in exts), 'Others')
            os.makedirs(os.path.join(download_folder, destination_folder), exist_ok=True)
            shutil.move(os.path.join(download_folder, file), os.path.join(download_folder, destination_folder, file))
    print("Downloads organized!")

if __name__ == "__main__":
    downloads_path = 'C:/Users/User/Downloads'  # Replace with the path to your downloads folder
    organize_downloads(downloads_path)