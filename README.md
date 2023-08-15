
![Icon(2)](https://github.com/Sir-Sorg/Arconer/assets/66873974/099166e7-1fa8-4ec7-bc67-f559d90d46d0)


# Arconer 📇
This is a script in Python language to connect to the Aberclass site and data mining the information of students and classes in the future schedule to create the class completion text automatically. In it, there are `POST` and `GET` mechanisms to bypass and go through the identity verification process.
## Explanation code Snippet 📂
`abar_conten.py` is a Python script interacts with a website using the `requests` and `BeautifulSoup` libraries to extract information. Here are the key components and their explanations:

1. **Importing Libraries and Modules:**
   - `requests`: Used for sending HTTP requests to a website and receiving responses.
   - `BeautifulSoup`: Used for parsing and extracting information from web pages.

2. **Function Definitions:**
   - `readCookies()` and `writeCookies(cookies)`: Functions for reading and writing cookie data to/from a JSON file to store and reuse cookies for subsequent sessions.
   - `loggin()`: A function for logging into the system by sending POST requests with relevant parameters.

3. **`Classroom` Class:**
   - A class to represent information about a classroom session, with attributes like student name, class date and time, and subject.
   - The `content()` function generates a descriptive text about the class.

4. **Website Communication:**
   - Configurations like `User-Agent` and other headers for HTTP requests.
   - Use of the `readCookies()` function to read cookies from a file and store them in the session using `session.cookies.update()`.
   - Sending a GET request to the specified URL.

5. **Logging In and Extracting Information:**
   - Using the `loggin()` function to log into the system through POST requests and relevant inputs.
   - Extracting information about upcoming classes and creating instances of the `Classroom` class.
   - Displaying class information using the `content()` function.
   - In this part of the code, `if` statement is used to check the successful login. This function tries up to 5 times to enter the sent pin code correctly and checks the login status. If logged in correctly, a login success message will be printed; Otherwise, a login failure message will be printed it depended to Pic code that user input to app.

## Notice 📑
Do not forget to change the `phone` variable value in ***line 23*** of the program to your phone number.

## Contact 
This provides an overview of the code's components and functionalities. If you have any questions or would like more detailed explanations or if you want to upgrade a part of the program contact me: [Email](mailto:sinaorojlo53@gmail.com)
