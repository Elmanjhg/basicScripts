#!/usr/bin/env python3
import argparse
import os


"""
function to create a directory if not already exists
"""
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"created directory: {path}")
    else:
        print(f"Warning: Directory already exists: {path}")

"""
create new file with content
"""
def create_new_file(path, content=""):
    if not os.path.exists(path):
        with open(path, "w") as file:
            file.write(content)
        print(f"created new file: {path}")
    else:
        print(f"Warning: File already exists: {path}")


if __name__ == "__main__":
    print("C++ Project Setup")

    #create ArgumentParser object
    parser = argparse.ArgumentParser()

    #new Terminal arg -> project_name with flag: --help -> Project name
    parser.add_argument("project_name", help="Project name")


    # parse from parser object args to args object
    args = parser.parse_args()

    # example usage could be:
    # print("This is the project name: " + args.project_name)

    """
     Creating Project Structure
    """

    # Define project root path
    project_path = os.path.join(os.getcwd(), args.project_name)
    create_directory(project_path)

    # Create subdirectories
    create_directory(os.path.join(project_path, "src"))
    create_directory(os.path.join(project_path, "build"))

    # Create files
    create_new_file(os.path.join(project_path, "README.md"), f"# {args.project_name}\n")
    create_new_file(os.path.join(project_path, "src", "main.cpp"),
                    '#include <iostream>\n\nint main() {\n    // TODO Implement here\n    return 0;\n}')




