def read_and_modify_file(input_filename, output_filename):
    try:
        # Read from input file
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        # Modify content: for example, convert to uppercase
        modified_lines = [line.upper() for line in lines]

        # Write to output file
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Successfully wrote modified content to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"❌ I/O Error: {e}")


def main():
    input_file = input("📥 Enter the filename to read from: ").strip()
    output_file = input("📤 Enter the filename to write to: ").strip()
    read_and_modify_file(input_file, output_file)


if __name__ == "__main__":
    main()
