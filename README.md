# Barry Oumar Portfolio Web application with Flask

#### Video Demo:  https://youtu.be/y52nrHBGFiE

#### Description:

This project is a personal portfolio web application for Barry Oumar, designed to showcase my skills, education, professional experience, and projects as a chemical engineer and aspiring web developer. The site is built using Python (Flask), SQLite, Bootstrap 5, and includes features for both public visitors and admin management.

---

## Features

- **Homepage:**  
  Displays a summary of featured projects and a dynamic list of skills pulled from the database. Visitors can easily navigate to learn more about me or view my full resume.

- **Projects Gallery:**  
  All projects are listed with images, descriptions, technologies used, and links to external resources if available. Projects are stored in the database and can be managed via the admin interface.

- **Resume Page:**  
  Education and professional experience entries are displayed in a visually appealing card format, each with institution/company logos, periods, and descriptions. Skills are also shown, grouped and styled by category.

- **About Page:**  
  Provides a brief introduction and displays skills grouped by category, dynamically loaded from the database.

- **Contact Page:**  
  Visitors can send messages via a contact form. Messages are validated, sent to my email using Flask-Mail, and also stored in the database for admin review. Social media links (GitHub, LinkedIn, Facebook, Instagram) are included in both the footer and contact page.

- **Admin Panel:**  
  Secure login for admin management. Admin can add, edit, and delete projects, skills, and resume entries. All forms include validation and support for uploading logos for institutions and companies.

- **Internationalization (I18N):**  
  The site supports both English and French. All public-facing text can be translated using a simple dictionary-based system. Users can switch languages via a dropdown in the navbar.

- **Error Handling:**  
  Custom 404 and 500 error pages provide a friendly experience for users.

- **CV Download:**  
  Visitors can download my CV directly from the site.

---

## File Overview

- **app.py:**  
  The main Flask application file. Contains all route definitions, database interactions, email configuration, session management, error handlers, and internationalization logic.

- **templates/**  
  - `layout.html`: The base template for all pages, includes the navbar, footer, and Bootstrap integration.
  - `index.html`: Homepage with featured projects and skills.
  - `projects.html`, `projects_paginated.html`: Project gallery pages.
  - `resume.html`: Public resume page showing education, experience, and skills.
  - `about.html`: About me and grouped skills.
  - `contact.html`: Contact form and social links.
  - `admin/`: Contains all admin management templates for projects, skills, and resume entries.
  - `404.html`, `500.html`: Custom error pages.

- **static/**  
  - `styles.css`: Custom CSS for additional styling.
  - `images/`: Logos and project images.
  - `cv/`: Contains the downloadable CV PDF.

- **helpers.py:**  
  Contains utility functions, including the `login_required` decorator for admin routes.

- **portfolio.db:**  
  SQLite database storing users, projects, skills, resume entries, and contact messages.

---

## Design Choices

- **Flask & SQLite:**  
  Chosen for simplicity and ease of deployment for a personal portfolio. SQLite is lightweight and sufficient for the expected data volume.

- **Bootstrap 5:**  
  Ensures a modern, responsive design with minimal custom CSS required.

- **Internationalization:**  
  Implemented via a dictionary and context processor for maintainability and performance. This allows easy addition of new languages in the future.

- **Security:**  
  Admin routes are protected by session-based authentication. Passwords are hashed using Werkzeug. Sensitive information (like email credentials) is stored in environment variables and loaded via `python-dotenv`.

- **Contact Form:**  
  Messages are both emailed and stored in the database for reliability and future reference. Validation ensures only legitimate messages are accepted.

- **Modular Templates:**  
  All pages extend a base layout for consistency. Admin templates are separated for clarity and maintainability.


---

## Future Improvements

- Add file upload support for logos and CV.
- Implement pagination for skills and resume entries.
- Add admin interface for viewing contact messages.
- Enhance internationalization with more languages and dynamic content translation.

---

This project demonstrates my ability to design, implement, and deploy a full-featured web application with modern best practices. Every aspect, from database design to user experience, has been considered