import csv
import os

input_folder_path = "C:\\logs\\New_logs\\004_SCCO\\SCCO"
output_file_path = "C:\\Users\\Yunin_RA\\Desktop\\filtered_new_logs\\log_1.log"
server = "004"
app = "SCCO"
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