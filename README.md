PROJECT TITLE: Toolx
Video Demo:  <URL HERE>

Intro 
So toolx is a python based digital toolkit that predominantly focuses on file conversion at the moment but I am hoping to add additional features to this soon. This is the final assignment for my CS50 course but will still be maintained after submission. 

index.html is the homepage for this app which has its own CSS and does not extend any layout. it is the page where users can select which category of tools they want to use. after selecting the tool app will redirect them to their desired tool page where they will have all the available operations in that category in a dropdown. some of them may feel silly and unnecessary operations but there will be more added soon I just wanted to get this up as soon as possible.

The rest of the HTML is extended from layout.html and not all of them are directly handled by the app like operations in 'text.html' and 'numbers.html' is coded in javascript because of the simplicity of the tasks they perform so information on these pages do not go to the server itself (For Now at Least)

apology.html is the webpage to display error/alerts which is straight-up taken from the cs50 problem set and it worked for me so far but it may get completely replaced by javascript alerts as in some pages of toolx just because there are faster and does not redirect the user to a different page.

helpers.py is where all functions are written and then imported to app.py majority of libraries are also imported in this file.

uploads folder is the main saving place of the server so renaming or removing it will cause an error helpers.py will generate a subfolder for every operation separately to not get any error and the original uploaded file will be removed right after completion of the operations.

All the original files that will be uploaded to the server will instantly be deleted after completion but the resulting copy of that file will be kept for a few hours before being deleted

