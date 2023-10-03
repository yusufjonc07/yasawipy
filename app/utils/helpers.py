import os

def delete_files(directory: str, extensions: list):
    
    for filename in os.listdir(directory):

        for exs in extensions:
            if filename.endswith(f".{exs}"):
                os.remove(os.path.join(directory, filename))
    return True
