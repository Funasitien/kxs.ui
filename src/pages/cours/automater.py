import os

# Define the file extension to look for (e.g., '.txt')
FILE_EXTENSION = ".mdx"

# Define the dictionary with replacements
REPLACEMENTS = {
    "\n  * [cours](https://kxs.fr/cours/)\n  * [sujets](https://kxs.fr/sujets/)\n  * [fiches](https://kxs.fr/fiches/)\n\n[![Logo de kxs.fr](/img/logo.svg)](https://kxs.fr/)[Cours d'informatique pour\nle lycée et la prépa](https://kxs.fr/cours/)\n": " ",
    "img/": "/cours/",
}

def replace_in_file(file_path, replacements):
    """
    Reads a file, replaces occurrences of specified keys with their values, and writes back the updated content.
    
    Args:
        file_path (str): Path to the file.
        replacements (dict): Dictionary of replacements {old_text: new_text}.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Processed: {file_path}")

def process_files(directory, extension, replacements):
    """
    Recursively processes files in a directory, applying replacements to files with a specific extension.

    Args:
        directory (str): The starting directory.
        extension (str): File extension to search for.
        replacements (dict): Dictionary of replacements {old_text: new_text}.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, replacements)

if __name__ == "__main__":
    # Start processing from the current directory
    current_directory = os.getcwd()
    process_files(current_directory, FILE_EXTENSION, REPLACEMENTS)