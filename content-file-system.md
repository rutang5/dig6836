## File System Commands Primer

### Windows

#### Command Prompt

The Command Prompt is a command-line interpreter for Windows systems.

##### Changing Directories

To change the current directory, use the `cd` command followed by the desired directory path. Here are some examples:

```shell
cd C:\path\to\directory    # Change to an absolute path
cd path\to\directory       # Change to a relative path
cd ..                      # Move up one directory
cd                        # Change to the user's home directory
```

##### Listing Files and Directories

To list files and directories in the current directory, use the `dir` command:

```shell
dir                       # List files and directories in the current directory
dir /w                    # Display the listing in wide format
dir /a                    # Display all files, including hidden files
```

##### Creating Directories

To create a new directory, use the `mkdir` command followed by the desired directory name:

```shell
mkdir new_directory      # Create a new directory named "new_directory"
```

##### Copying Files and Directories

To copy a file or directory, use the `copy` command:

```shell
copy source_file destination_file   # Copy a file
copy source_directory destination_directory /s   # Copy a directory and its contents
```

##### Deleting Files and Directories

To delete a file or directory, use the `del` or `rmdir` command:

```shell
del file.txt              # Delete a file
rmdir directory           # Delete an empty directory
rmdir /s directory        # Delete a directory and its contents
```

#### PowerShell

PowerShell is a more advanced command-line shell and scripting language for Windows systems.

##### Changing Directories

To change the current directory, use the `Set-Location` command or its alias `cd` followed by the desired directory path. Here are some examples:

```shell
Set-Location C:\path\to\directory    # Change to an absolute path
Set-Location path\to\directory       # Change to a relative path
Set-Location ..                      # Move up one directory
Set-Location ~                       # Change to the user's home directory
```

##### Listing Files and Directories

To list files and directories in the current directory, use the `Get-ChildItem` command:

```shell
Get-ChildItem                      # List files and directories in the current directory
Get-ChildItem -Force               # Display all files, including hidden files
```

##### Creating Directories

To create a new directory, use the `New-Item` command followed by the desired directory name:

```shell
New-Item -ItemType Directory -Name new_directory      # Create a new directory named "new_directory"
```

##### Copying Files and Directories

To copy a file or directory, use the `Copy-Item` command:

```shell
Copy-Item -Path source_file -Destination destination_file   # Copy a file
Copy-Item -Path source_directory -Destination destination_directory -Recurse   # Copy a directory and its contents
```

##### Deleting Files and Directories

To delete a file or directory, use the `Remove-Item` command:

```shell
Remove-Item -Path file.txt              # Delete a file
Remove-Item -Path directory -Force      # Delete a directory and its contents
```

### Mac

The macOS terminal, also known as the Terminal app, provides access to the Unix shell.

##### Changing Directories

To change the current

 directory, use the `cd` command followed by the desired directory path. Here are some examples:

```shell
cd /path/to/directory    # Change to an absolute path
cd path/to/directory     # Change to a relative path
cd ..                    # Move up one directory
cd                      # Change to the user's home directory
```

##### Listing Files and Directories

To list files and directories in the current directory, use the `ls` command:

```shell
ls                       # List files and directories in the current directory
ls -l                    # Display the listing in long format
ls -a                    # Display all files, including hidden files
```

##### Creating Directories

To create a new directory, use the `mkdir` command followed by the desired directory name:

```shell
mkdir new_directory     # Create a new directory named "new_directory"
```

##### Copying Files and Directories

To copy a file or directory, use the `cp` command:

```shell
cp source_file destination_file   # Copy a file
cp -R source_directory destination_directory   # Copy a directory and its contents
```

##### Deleting Files and Directories

To delete a file or directory, use the `rm` command:

```shell
rm file.txt              # Delete a file
rm -r directory          # Delete a directory and its contents
```

### Linux/Unix

Linux and Unix systems also provide a terminal with access to the Unix shell.

##### Changing Directories

To change the current directory, use the `cd` command followed by the desired directory path. Here are some examples:

```shell
cd /path/to/directory    # Change to an absolute path
cd path/to/directory     # Change to a relative path
cd ..                    # Move up one directory
cd                      # Change to the user's home directory
```

##### Listing Files and Directories

To list files and directories in the current directory, use the `ls` command:

```shell
ls                       # List files and directories in the current directory
ls -l                    # Display the listing in long format
ls -a                    # Display all files, including hidden files
```

##### Creating Directories

To create a new directory, use the `mkdir` command followed by the desired directory name:

```shell
mkdir new_directory     # Create a new directory named "new_directory"
```

##### Copying Files and Directories

To copy a file or directory, use the `cp` command:

```shell
cp source_file destination_file   # Copy a file
cp -r source_directory destination_directory   # Copy a directory and its contents
```

##### Deleting Files and Directories

To delete a file or directory, use the `rm` command:

```shell
rm file.txt              # Delete a file
rm -r directory          # Delete a directory and its contents
```

This primer provides a basic overview of file system commands in the terminal or command prompt for Windows, Mac, and Linux/Unix systems. Use these commands to navigate, list, create, copy, and delete files and directories in your respective operating system.
