# Humanities Showcase

## Introduction
In this assignment, you will explore the Flask library in Python and build a web application called "Flask Humanities Showcase." The application will highlight various aspects of humanities, such as literature, art, philosophy, or history. You will create multiple routes/pages, each representing a different aspect of the humanities, and showcase relevant content.

## Task
Your task is to build the Flask Humanities Showcase web application. Each route/page should focus on a specific theme within the humanities, presenting information, images, or interactive elements related to that theme.

## Instructions

1. **Install Flask**: If you don't have Flask installed, use the following command to install it:
   ```
   pip install flask
   ```

2. **Create a new Python script**: Create a new Python script named `flask_humanities_showcase.py`.

3. **Import the necessary modules**: Import the necessary modules in your Python script:
   ```python
   from flask import Flask, render_template
   ```

4. **Create an instance of the Flask class**: Create an instance of the Flask class in your Python script:
   ```python
   app = Flask(__name__)
   ```

5. **Define multiple routes**: Define multiple routes for your application in your Python script. Each route will represent a different theme within the humanities:
   - Route 1: Home page
     - URL: `/`
     - Description: This page will serve as the landing page for your Flask Humanities Showcase application. It should provide an overview of the application and list the available themes within the humanities.

   - Route 2: Literature
     - URL: `/literature`
     - Description: This page should display information, excerpts, or notable works related to a particular literary theme, author, or literary movement.

   - Route 3: Art
     - URL: `/art`
     - Description: This page should showcase artworks, artists, or art movements that have had a significant impact on the humanities.

   - Route 4: Philosophy
     - URL: `/philosophy`
     - Description: This page should explore philosophical ideas, thinkers, or philosophical movements that have shaped the humanities.

   - Route 5: History
     - URL: `/history`
     - Description: This page should delve into historical events, periods, or figures that have influenced the humanities.

   - Feel free to add more routes/pages for additional themes or aspects within the humanities.

6. **Define view functions**: Define view functions for each route in your Python script. Each view function will render the corresponding HTML template:
   - Create a function for the home page route:
     ```python
     @app.route('/')
     def index():
         themes = ["Literature", "Art", "Philosophy", "History"]  # Update with humanities themes
         return render_template('index.html', themes=themes)
     ```

   - Create view functions for each theme route:
     ```python
     @app.route('/literature')
     def literature():
         # Add code to display content related to Literature
         return render_template('literature.html')

     @app.route('/art')
     def art():
         # Add code to display content related to Art
         return render_template('art.html')

     @app.route('/philosophy')
     def philosophy():
         # Add code to display content related to Philosophy
         return render_template('philosophy.html')

     @app.route('/history')
     def history():
         # Add code to display content related to History
         return render_template('history.html')
     ```

   - Remember to add more view functions for additional themes or aspects within the humanities

.

7. **Create HTML templates**: Create HTML templates for each page in your Flask application. Each template will represent a different page/theme:
   - Create an `index.html` template for the home page.
   - Create separate HTML templates for each theme page (`literature.html`, `art.html`, `philosophy.html`, `history.html`, etc.).

8. **Test your application**: Run your Flask application and test it by navigating to different routes in your web browser.

---

Follow these instructions to complete the Flask Humanities Showcase assignment. Customize the content and design of your application to showcase your chosen humanities themes and create an engaging web experience for your users.

Good luck with your assignment!
