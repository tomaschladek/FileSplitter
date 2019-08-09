import csv
import os,sys

def createOutFile(index,full_path_out,file_name):
    new_path = os.path.join(full_path_out, file_name + str(index).zfill(4) + ".csv")
    csv_file_out = open(new_path, mode='w', newline='')
    csv_writer = csv.writer(csv_file_out)
    return (csv_file_out,csv_writer)

def splitFile (full_path_in, full_path_out, limit):
    with open(full_path_in) as csv_file_in:
        csv_reader = csv.reader(csv_file_in, delimiter=',')
        next(csv_reader)
        index = 0;
        file_name = os.path.basename(full_path_in).split('.')[0]

        (csv_file_out, csv_writer) = createOutFile(index,full_path_out,file_name)
        line_count = 0
        for row in csv_reader:
            line_count += 1
            csv_writer.writerow(row)
            if line_count == limit:
                csv_file_out.close()
                index += 1
                (csv_file_out, csv_writer) = createOutFile(index, full_path_out, file_name)
                line_count = 0
        csv_file_out.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("Not enought parameters")
    splitFile(sys.argv[1],sys.argv[2],sys.argv[3])