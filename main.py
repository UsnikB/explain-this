import argparse
import subprocess

parser = argparse.ArgumentParser(description="A Script that gives details about a file or folder")
parser.add_argument("-f", "--file", type=str, help="Specify an input file.")
parser.add_argument("-d", "--folder", type=str, help="Specify an input folder.")

args = parser.parse_args()

# Check if tree is installed
if shutil.which("tree") is None:
    print("Error: 'tree' command not found.")
    sys.exit(1)

if args.file:
    print(f"Input file provided: {args.file}")
    print(f"Full path: {subprocess.run(['cat', args.file], capture_output=True, text=True).stdout}")
else:
    print("No input file specified.")

if args.folder:
    print(f"Folder provided: {args.folder} ")
    print(f"Full path: {subprocess.run(['tree', args.folder])}")
else:
    print("No Input folder in specified.")

