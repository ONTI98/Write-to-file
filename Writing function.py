#Programme will write to a file
#Programme will ask for user input
#One variable for text to be written,another for name of file

def main():
    write_to_file()
    return

#variables

def write_to_file():

    fileName=input("insert file name (File.txt/csv): ")
    fileLocation=f"C:\\Users\
    \\User\\source\\repos\\PythonApplication7\\PythonApplication7\\{fileName}"
    WRITE='w'
    text=input("Please insert text to write to file:")
    with open (fileName,mode=WRITE) as file:
        file.write(text)
        print(f"File written successfully in {fileLocation}")

main()
