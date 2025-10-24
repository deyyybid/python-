## Day 01 - Working with Variables
Today’s session covers Printing, Commenting, Debugging, String Manipulation, and Variables — the foundations of writing clean, expressive Python code.

By the end of this session, you’ll build your very first mini-project: The Band Name Generator.

1. Printing to the Console
> Key Takeaways
- The *print()* function outputs text or data to the console.
- Strings must be enclosed in matching quotation marks.
- Syntax highlighting and error messages help identify mistakes.
- Following the **PEP 8** style guide improves readability and consistency.

```python
# Sample Code
print("Hello, World!")
```

2. String Manipulation and Code Intelligence
> Key Takeaways
- Use the newline character \n to print text on multiple lines in a single statement.
- Combine multiple strings using concatenation (+), and include spaces manually where needed.
- Python is strict about indentation; incorrect spacing causes IndentationError.
- Error messages such as SyntaxError and IndentationError help identify and fix issues efficiently.

```python
# Sample Code
print("Hello, World!\nGoodbye, World!")  # Newline
print("Hello, " + "World!")              # Concatenation

```

3. The input() Function
> Key Takeaways
- The *input()* function allows users to provide data through the console.
- The program pauses and waits for input before continuing.
- Combine *input()* results with other strings for dynamic responses.
- Use comments (#) to describe your code — they’re ignored by the interpreter but useful for humans.

```python
# Sample Code
print(input("What is your name? "))
```

4. Python Variables
> Key Takeaways
- Variables store data for later use and make code more flexible.
- Assign user input to a variable with =.
- The *len()* function returns the number of characters in a string.
- Clear and descriptive variable names make your code easier to maintain.

```python
# Sample Code
username = input("What is your name? ")
print("Name: " + username)

length = len(username)
print("Name Length: " + str(length))
```

<hr>

#### Reminders
- Use consistent and descriptive variable names.
- Variable names cannot contain spaces; use underscores instead.
- Variable names cannot start with numbers or use Python keywords.
- A NameError usually means a variable is misspelled or not yet defined.

#### Possible errors to watch out for:
- **SyntaxError:** Something is typed incorrectly, and Python can’t understand it.
- **IndentationError:** Wrong number of spaces or tabs at the start of a line.
- **ValueError:** Input has the correct type but an invalid value.
- **NameError:** You tried to use a variable or function name that doesn’t exist.