# Blank Row inserter:
# How it works:
# take two integers from the terminal : sys.argv N1 N2
# N1 -> the starting row
# N2 -> the number of blanck rows
# ---
# you will need to spreadsheet to read it
# then take two integers from user
# then write out the old spreadsheet into the new one
# then  by using for loop
# start at N1 row and put N2 rows blanck and write the rest of the old spread into the rest ones

import openpyxl, sys

def insert_blank_rows_copy():
    """
    Inserts blank rows into an Excel file by copying data to a new workbook.
    This version fixes the original code's issue by saving the output to a new file.
    """
    try:
        # Get command-line arguments.
        # N is the starting row number, M is the number of blank rows to insert.
        # filename is the original Excel file.
        # new_filename is the name for the modified file.
        N = int(sys.argv[1])
        M = int(sys.argv[2])
        filename = sys.argv[3]
        new_filename = sys.argv[4]
    except (IndexError, ValueError):
        # If command-line arguments are not provided or invalid, prompt the user.
        print("Please provide four command-line arguments:")
        print("1. Start row number (N)")
        print("2. Number of blank rows to insert (M)")
        print("3. Original filename (e.g., myProduce.xlsx)")
        print("4. New filename for the output (e.g., myProduce_modified.xlsx)")
        return
    
    try:
        # Load the original workbook and get the active sheet
        wb = openpyxl.load_workbook(filename)
        sheet = wb.active

        # Create a new workbook to hold the modified data
        wb_new = openpyxl.Workbook()
        new_sheet = wb_new.active

        # Copy rows from the original sheet up to row N-1
        for row in range(1, N):
            for col in range(1, sheet.max_column + 1):
                new_sheet.cell(row=row, column=col).value = sheet.cell(
                    row=row, column=col
                ).value

        # Copy the remaining rows from the original sheet,
        # but shifted down by M rows in the new sheet.
        for row in range(N, sheet.max_row + 1):
            for col in range(1, sheet.max_column + 1):
                new_sheet.cell(row=row + M, column=col).value = sheet.cell(
                    row=row, column=col
                ).value

        # Save the new workbook with the specified new filename
        wb_new.save(new_filename)
        print(f"Blank rows have been added. The new spreadsheet is saved as '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function when the script is executed
if __name__ == "__main__":
    insert_blank_rows_copy()
