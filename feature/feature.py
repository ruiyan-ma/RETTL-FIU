import os
import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) < 4: 
        print("Miss arguments.")

    program = sys.argv[1]
    config = sys.argv[2]
    input_folder = sys.argv[3]

    output_ext = '.csv'
    if len(sys.argv) == 5:
        output_ext = sys.argv[4]

    for root, dirs, files in os.walk(input_folder):
        files = [file for file in files if file.endswith('.wav')]
        for file_name in files:
            input_file = os.path.join(root, file_name)
            output_file = os.path.splitext(input_file)[0] + output_ext
            command = [program, '-C', config, '-I', input_file, '-O', output_file]
            res = subprocess.call(command)
