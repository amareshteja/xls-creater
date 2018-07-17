import xlsxwriter
import os

path = 'output/'
txt_file = 'excel-file-names.txt'

# Get all file names from text file
def get_file_names():
    if os.path.exists(txt_file):
        with open(txt_file, "r") as data:
            text_data = data.read()
            files_list = text_data.split(',')
            return files_list
    else:
        print(txt_file, "file not found!!")



# Create Excel file using given file name
def create_new_xls(file_name, file_number):
    try:
        workbook = xlsxwriter.Workbook(path + file_name)
        worksheet = workbook.add_worksheet()
        workbook.close()
        print("[File no." +str(file_number)+ "] " + file_name + " created!")
    except Exception as e:
        print("ERROR: Problem in creating " + file_name + " file!")



# Starting point of script
def main():
    file_names = get_file_names()
    if file_names:
        print("\nTotal " + str(len(file_names)) + " file names found!\n")
        for file_number, file_name in enumerate(file_names, start=1):
            if not os.path.exists(path + file_name):
                create_new_xls(file_name, file_number)
            else:
                print("[File no." +str(file_number)+ "] " + file_name + " already created!")




if __name__ == "__main__":
    main()
        