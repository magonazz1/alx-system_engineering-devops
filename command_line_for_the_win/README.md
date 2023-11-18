# Command Line for the Win: My Bash Scripting Project

## Project Overview

**Command Line for the Win** is my exciting project designed to assess my proficiency in utilizing protocols within the command line interface, with a specific focus on Bash scripting. This README provides a detailed guide on how I can transfer screenshot files from my local machine to a sandbox environment and push them to a GitHub repository using Bash scripting.

## Steps

Follow these steps along with the specific commands to harness the power of Bash scripting and seamlessly accomplish the file transfer and repository update:

1. **Open Intranet Sandbox Menu:**
   - I initiate the process by accessing the Intranet Sandbox Menu, my gateway to the testing environment.

2. **Locate and Click SFTP Button:**
   - Within the sandbox menu, I find and click on the SFTP button to obtain the hosting address for the client.

3. **Open Git-Bash Terminal:**
   - I launch the Git-Bash terminal on my local machine, setting the stage for executing powerful Bash commands.
     ```bash
     Martz@HP-Envy-x360 MINGW64/
     $
     ```

4. **Paste SFTP Client Address:**
   - I copy and paste the SFTP client address provided by my sandbox into the Git-Bash terminal, establishing a secure connection.
     ```bash
      $ 😜😜😜😜😜😜😜😜@host😜😜😜😜
     ```

5. **Navigate to Screenshot Folder:**
   - Using the `lcd` command, I navigate to the directory on my local machine where the screenshot files are stored.
     ```bash
     sftp> lcd C://Martz/Desktop/screenshots
     ```

6. **Recursively Copy Screenshots:**
   - I employ the command `get -r screenshots` to efficiently and recursively copy all contents from my local machine to the sandbox environment.
     ```bash
     sftp> get -r screenshots
     ```

7. **Verify Screenshot Placement:**
   - I ensure the correct placement of all screenshots within the sandbox directory using appropriate verification commands.
     ```bash
     $ ls -l alx-system_engineering-devops/command_line_for_the_win/
     ```

8. **Push Screenshots to Repository:**
   - I seal the deal by pushing all the screenshots to my GitHub repository, showcasing my Bash scripting prowess and preserving my work.
     ```bash
     $ git add .
     $ git commit -m "Add screenshots"
     $ git push
     ```
## License

This project is licensed under the MIT License - [LICENSE](./LICENSE)
