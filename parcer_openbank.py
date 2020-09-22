import argparse
import csv
import os


def main(input_folder_path, output_file_path, server, app):
    with open(output_file_path, "w", encoding='utf-8', newline='') as file_write:
        writer = csv.writer(file_write, delimiter='\t')
        for path in os.listdir(input_folder_path):
            input_file_path = "%s\\%s" % (input_folder_path, path)
            with open(input_file_path, encoding='utf-8', newline='') as file:
                reader = csv.reader(file, delimiter='\t')
                for row in reader:
                    if row and row[0] == "EventContext":
                        new_row = row + [server, app]
                        writer.writerow(new_row)


parser = argparse.ArgumentParser()
parser.add_argument("--source-folder")
parser.add_argument("--target-file")
parser.add_argument("--server")
parser.add_argument("--app")
args = parser.parse_args()
main(input_folder_path=args.source_folder, output_file_path=args.target_file, server=args.server, app=args.app)