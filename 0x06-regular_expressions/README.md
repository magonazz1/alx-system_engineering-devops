# 0x06 Regular Expression

## Overview
This project involves working with regular expressions using Oniguruma, a regular expression library used by Ruby by default. The goal is to create Ruby scripts that accept input arguments and utilize regular expressions to perform matching tasks.

## Background Context
In this exercise, the provided Ruby code serves as a template, and the focus is on replacing the regular expression part. The sample code looks like this:

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

This script takes an argument and applies a regular expression to match a specific pattern.

## Tasks

### 0. Simply Matching School
[task 0](/alx-system_engineering-devops/blob/master/0x06-regular_expressions/rcs/0-%20task%20-%20snipet.png)

- **Requirements:**
  - The regular expression must match the string "School."
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

```bash
sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 0-simply_match_school.rb

### 1. Repetition Token #0
https://github.com/magonazz1/alx-system_engineering-devops/blob/master/0x06-regular_expressions/rcs/1-%20task%20-%20snipet.png

- **Requirements:**
  - Find the regular expression that matches the specified cases.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 1-repetition_token_0.rb

### 2. Repetition Token #1
https://github.com/magonazz1/alx-system_engineering-devops/blob/master/0x06-regular_expressions/rcs/2-%20task%20-%20snipet.png

- **Requirements:**
  - Find the regular expression that matches the specified cases.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 2-repetition_token_1.rb

### 3. Repetition Token #2
- **Requirements:**
  - Find the regular expression that matches the specified cases.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 3-repetition_token_2.rb

### 4. Repetition Token #3
https://github.com/magonazz1/alx-system_engineering-devops/blob/master/0x06-regular_expressions/rcs/4-%20task%20-%20snipet.png

- **Requirements:**
  - Find the regular expression that matches the specified cases.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.
  - The regex should not contain square brackets.

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 4-repetition_token_3.rb

### 5. Not Quite HBTN Yet
- **Requirements:**
  - The regular expression must exactly match a string that starts with 'h,' ends with 'n,' and can have any single character in between.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

```bash
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
```

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 5-beginning_and_end.rb

### 6. Call Me Maybe
- **Requirements:**
  - The regular expression must match a 10-digit phone number.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

```bash
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
```

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 6-phone_number.rb

### 7. OMG WHY ARE YOU SHOUTING?
- **Requirement:**
  - The regular expression must only match capital letters.
  - Create a Ruby script that accepts one argument and passes it to a regular expression matching method.

```bash
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
```

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 7-OMG_WHY_ARE_YOU_SHOUTING.rb

### 8. TextMe (Advanced)
- **Requirements:**
  - Your script should output: [SENDER],[RECEIVER],[FLAGS]
  - The sender phone number or name (including country code if present)
  - The receiver phone number or name (including country code if present)
  - The flags that

 were used
  - Refer to the provided [log file] for examples.

- **Repo:**
  - GitHub repository: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
  - Directory: 0x06-regular_expressions
  - File: 100-textme.rb

## Powered by ALX Africa 2023
Feel free to reach out for any clarifications or assistance. Happy coding!


