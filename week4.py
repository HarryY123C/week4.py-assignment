# Practical Example: Add Line Numbers to a File

filename = input("📂 Enter the filename to read: ")

try:
    # Open file for reading
    with open(filename, "r") as infile:
        lines = infile.readlines()

    # Add line numbers
    modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

    # Save modified content to a new file
    new_filename = "numbered_" + filename
    with open(new_filename, "w") as outfile:
        outfile.writelines(modified_lines)

    print(f"✅ File '{filename}' was processed successfully!")
    print(f"📝 Numbered content saved to '{new_filename}'")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
# Practical Example: Add Line Numbers to a File

filename = input("📂 Enter the filename to read: ")

try:
    # Open file for reading
    with open(filename, "r") as infile:
        lines = infile.readlines()

    # Add line numbers
    modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

    # Save modified content to a new file
    new_filename = "numbered_" + filename
    with open(new_filename, "w") as outfile:
        outfile.writelines(modified_lines)

    print(f"✅ File '{filename}' was processed successfully!")
    print(f"📝 Numbered content saved to '{new_filename}'")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
