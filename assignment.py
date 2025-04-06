def file_read_write():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read from: ")
        
        # Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content 
        modified_content = content.upper()
        
        # Ask the user for the output file name
        output_file = input("Enter the name of the file to write to: ")
        
        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Content successfully written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read or written. Please check permissions or disk space.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_read_write()