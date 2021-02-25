import sys
from pathlib import Path
from typing import List, Set, NamedTuple

def main(file_to_read: Path, output_folder: Path):
    """
    Main function of program
    """
    print(f"reading {file_to_read}")
    with file_to_read.open() as ftr:
        for line in ftr.readlines():
            stripped_line: str = line.strip()
            if stripped_line:
                print(f"reading: {stripped_line}")

    output_file = output_folder.joinpath(file_to_read.stem + '_output.txt') 
    print(f"writing to: {output_file}")
    if not output_folder.exists():
        output_folder.mkdir(parents=True)
        print(f"Created output folder {output_folder}")

    with output_file.open('w') as ftw:
        ftw.write('someline')
        ftw.write('someline 2\n')
        ftw.write('someline 3')
        ftw.write('\n')
        ftw.write('end\n')

if __name__ == "__main__":
    # execute only if run as a script
    current_file = Path(sys.argv[1])
    output_folder = Path(sys.argv[2])
    main(current_file, output_folder)
