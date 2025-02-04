# RapidEngine

RapidEngine is a Python-based program designed to synchronize folders between multiple locations or devices to maintain consistency on Windows systems. It ensures that files and directories are identical in both the source and destination paths.

## Features

- **Folder Synchronization**: Automatically copies new and updated files from the source to the destination.
- **File Consistency**: Removes files from the destination that are no longer present in the source.
- **Recursive Handling**: Handles nested directories and files.

## Requirements

- Python 3.x
- Windows Operating System

## Installation

1. Make sure Python 3.x is installed on your Windows system.
2. Download or clone the repository.
3. Navigate to the directory containing the `RapidEngine.py` file.

## Usage

1. Open a terminal or command prompt.
2. Run the script using Python:

   ```bash
   python RapidEngine.py
   ```

3. When prompted, enter the path of the source folder and the destination folder.
4. The program will synchronize the folders, ensuring consistency.

## Example

Here's a simple example of how to use RapidEngine:

```bash
Enter the path of the source folder: C:\Users\YourName\Documents\SourceFolder
Enter the path of the destination folder: D:\Backup\DestinationFolder
```

## Note

- Ensure that both source and destination paths are accessible and that you have the necessary permissions to read and write to these directories.
- This script is intended for use on Windows systems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for suggestions or improvements.