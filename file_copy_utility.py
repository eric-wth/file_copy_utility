import shutil
import os

def copy_file(source, destination):
    """
    Copy a file from source to destination

    Arguments:
    source (str): path to the source file
    destination (str): path to the destination file
    """

    try:
        #check if the source file exists
        if not os.path.exists(source):
            print(f"Error: Source file '{source}' does not exist")
            return
        
        #check if destination directory exists, create it if it doesn't
        destination_dir = os.path.dirname(destination)

        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        #copy the file
        shutil.copy2(source, destination)
        print(f"File '{source}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Unable to copy '{source}'.")
    except shutil.SameFileError:
        print(f"Error: Source and destination are the same file.")
    except Exception as e:
        print(f"Error: {e}")
    


def main():
    source_file = input("Enter the source file path: ").strip()
    destination_file = input("Enter the destination file path: ").strip()

    copy_file(source_file, destination_file)


if __name__ == "__main__":
    main()
