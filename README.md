# Barry Oumar Portfolio Web application with Flask


#### Description:

This project is a personal portfolio web application for Barry Oumar, designed to showcase my skills, education, professional experience, and projects as a chemical engineer and aspiring web developer. The site is built using Python (Flask) and Frozen-Flask to generate a static site, with Bootstrap 5 for styling.

---

## Features

- **Homepage:**  
  Displays a summary of featured projects and a dynamic list of skills. Visitors can easily navigate to learn more about me or view my full resume.

- **Projects Gallery:**  
  All projects are listed with images, descriptions, technologies used, and links to external resources.

- **Resume Page:**  
  Education and professional experience entries are displayed in a visually appealing card format.

- **About Page:**  
  Provides a brief introduction and displays skills grouped by category.

- **Contact Page:**  
  Simple contact information display.

- **CV Download:**  
  Visitors can download my CV directly from the site.

---

## File Overview

- **app.py:**  
  The main Flask application file used to generate the static site.

- **data.py:**
  Contains all the content data (projects, skills, experience, etc.) in Python dictionaries.

- **freeze.py:**
  Script to freeze the Flask application into static HTML files.

- **templates/**  
  - `layout.html`: The base template for all pages.
  - `index.html`: Homepage.
  - `projects.html`: Project gallery.
  - `parcours.html`: Resume/Experience page.
  - `services.html`: Services page.
  - `contact.html`: Contact page.
  - `404.html`: Custom error page.

- **static/**  
  - `css/styles.css`: Custom CSS.
  - `images/`: Logos and project images.
  - `cv/`: Contains the downloadable CV PDF.
  - `js/`: JavaScript files.

---

## Design Choices

- **Flask & Frozen-Flask:**  
  Used to generate a static website from dynamic templates, combining the ease of development of Flask with the performance and hosting simplicity of static files.

- **Bootstrap 5:**  
  Ensures a modern, responsive design.

- **Data Separation:**
  Content is separated from logic in `data.py`, making it easy to update the portfolio without touching the HTML templates.

---

## Future Improvements

- Add more interactive elements.
- Improve SEO metadata.
- Add a blog section.

---

This project demonstrates my ability to design and implement a clean, professional web portfolio.