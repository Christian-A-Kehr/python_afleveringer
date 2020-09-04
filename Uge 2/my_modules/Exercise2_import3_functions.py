
#exc 2.1 
def print_file_content(file):
    """print content of a text file to the console"""

    with open(file) as infile_object:
        lines = infile_object.readlines()
    for line in lines:
        print(line.rstrip())

#check        
#print_file_content("Exercise2_ ex1_input.txt")

#exc 2.2
def write_list_to_file(output_file, lst):
    """can take a list or tuple and write each element to a new line in file
    
    
    Parameters:
    output_file: The file to write. 
    1st: what to write in output_file
    
    """
    #newfile = Path(Path.cwd()/ "docker_notebooks" / "notebooks" / "my_notebooks" / "python_afleveringer"/ output_file)
     
    with open(output_file, "w") as file_object:
        [file_object.write(((item.replace("\n", "")).replace(" ", "")) + "\n") for item in lst if item.strip()]
        
    print ("file saved")  
    
#check
#list_of_elements = ["Bob", "John", "Joe"]
#write_list_to_file("Exercise2_ex1_output.txt", list_of_elements)

#exc 2.3
import csv

def read_file(input_file):
    """take a csv file and read each row into a list
    
    Parameters:
    input_file: csv file to be read 
    """
    
    with open(input_file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        print(header_row)
        data_row1 = next(reader)
        print(data_row1)
        cvs_list = []
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))
            cvs_list.append(str(row))
        
        print (cvs_list)
        


#check
#filename = './befkbhalderstatkode.csv'
#read_file(filename)