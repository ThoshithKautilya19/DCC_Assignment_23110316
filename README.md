# DCC_Assignment_23110316
This is my GitHub repository for the DCC Assignment.

Step-1: Download my template and main.py files from the branch 'Templates_Main'. Template files end with .html and main file with .py. Make sure that templates file are in a separate 'templates' folder to be used.

Step-2: A few edits I would like you to do is edit the CSV file of the Databases, such that their Column headings have no 'big spaces' like '
     'this between each word. It caused a lot of problems when executing in MySQL. Also, change the datatype in Denominations from 'text' to 'int', so that you will be able to calculate the sum of all the Electoral Bond Values.

Step-3: Make sure you have imported the Databases for the Electoral Bonds data into MySQL, and check the names of the tables in  my files and yours to prevent errors. Also, do check Host, User, Password and Database in 'app.config'.

Step-4: I have made demarcations using Comments, which will tell which function belongs to which question/ operates on which type of database.

Step-5: On opening the server, your browser launches and shows index.html template. Then, I have given two Select buttons for each question, which asks you if you want to know about the Political Parties or Individuals/Companies, and it redirects you to either of them.

Step-6: For Question-1, you go into pp.html/ indi.html, where I have provided Search boxes based on almost all types of info on a Political party; use the correct search box and then click on submit. It will give you a table of all rows having that particular value.

Step-7 For Question -2, you go into pp_bond_info.html/ indi_bond_info.html, where I have provided a DROP-DOWN to select a particular political party/ individual and see the total number of bonds they have and the total value of those bonds too.
