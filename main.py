import os
import shutil
from pathlib import Path


def organize_files(source_directory, destination_directory):

    extensions = {
        "Images" : [".png", ".jpg", ".jpeg", ".gif", ".avif", ".webp"],
        "Videos" : [".mp4", ".mkv", ".mov"],
        "Archives" : [".zip", ".7z", ".rar", ".tar.gz"],
        "Documents" : [".txt", ".pdf", ".doc", ".docx", ".xlsx", ".pptx", ".odt"],
        "Music" : [".mp3", ".wav", ".flac", ".m4a", ".aac"],
        "Fonts" : [".ttf", ".otf", ".woff", ".woff2"],
        "Scripts" : [".py", ".sh", ".js", ".java", ".swift"],
        "Installers" : [".exe", ".msi", ".deb", ".dmg"]
    }
    
    
    if not os.path.exists(source_directory):
        print(f"{source_directory} does not exist")
        return
    
    for filename in os.listdir(source_directory):
        source_path = os.path.join(source_directory, filename)
        
        if os.path.isfile(source_path):
            file_extension = Path(filename).suffix.lower()
            
            subfolder_name = "Others"
            for folder, extension in extensions.items():
                if file_extension in extension:
                    subfolder_name = folder
                    break 
            
        
        destination_folder = os.path.join(destination_directory, subfolder_name)
        Path(destination_folder).mkdir(parents=True, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)

    print("File Organized successfully !")
            



if __name__ == "__main__":
    source_directory = input("Enter the source directory: ")
    destination_directory = input("Enter the destination directory: ")

    organize_files(source_directory, destination_directory)
    


