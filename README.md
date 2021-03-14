# HeadlessWhatsApp
A method to run selenium WhatsApp Web headless

This project boild for using whatsapp web via selenium in headless mode.

To start using it you can add it to your project and then use the command
```
rn = RunHeadless()
driver = rn.get_browser()
```
Then you have 3 options:

[1] - use new chrome user name "selenium"

[2] - use the Default chrome folder

[3] - chose another user folder name

You can also pass the choise in the start command:
```
rn = RunHeadless("1")
```
How does it work:

 First we open a regular window in the user folder you chose, and then you need to scan the whatspp QR.
 
 After you scan the QR you need to press enter (unless the whatsapp is already connect) and the browser will close automaticly.
 
 We take the user agent from the browser we opened and enter it to the new headless browser, so whatsapp can't know we are in headless mode.

This is my first github, so you are welcome to help me with this!
