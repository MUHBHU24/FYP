# FYP
Final Year Project

A web application exploring the theme of lexical variation and its regional differences in the UK. The main purpose of the app is providing a tool for researchers and language enthusiasts alike in surveying a wider population and demographic of users, thus exploring cultural differences through verbal communication and dialect.


--- TODO LIST ---

maybe allow users to add comments to surveys they partake in, and allow them to view other users comments on the same survey
allow surveys to expire after a certain amount of time

create conda env, install python, django, vite, etc
create the project and configure 
setup database
create superuser

Project setup:
-Create a new directory for your project and set up a virtual environment for Python.
-Install Django and create a new Django project using django-admin startproject projectName.
-Set up Vue.js by installing Node.js, Vue CLI, and create a new Vue project using vue create projectName.
-Install the necessary dependencies like Axios, Vue Router, and Bootstrap-Vue.

Django backend:
-Create a new Django app using python manage.py startapp appName.
-Define the models for the survey, questions, and answers. Models: basic user, researcher (admin), survey, question, answer, comments etc
-Set up the Django REST Framework for the API and create serializers for the models.
-Create the views and URLs for the API endpoints.

Vue.js frontend:
-Set up Vue Router for navigation between pages.
-Create components for the main page, survey creation, survey update, and survey display.
-Use Axios to communicate with the Django backend and fetch/create/update surveys.
-Use Bootstrap-Vue to style the components.

Geographical graphing:
-Integrate a mapping library like Leaflet or Mapbox into your Vue app.
-Use the collected data to display regional trends on the map.
-Customize the map style to make it simple and clear.
-Here's a rough outline of the components and their functionalities:

MainPage.vue:
-Display the list of available surveys.
-Provide links to create a new survey or take an existing one.

CreateSurvey.vue:
-Allow the admin user to create a new survey with an image, question, and pre-defined answers.
-Send the survey data to the Django backend for storage.

UpdateSurvey.vue:
-Allow the admin user to update an existing survey by adding more answers.
-Send the updated survey data to the Django backend.

TakeSurvey.vue:
-Display the survey question, image, and available answers.
-Allow users to submit their answers.
-Send the user's answer to the Django backend for storage and analysis.

MapView.vue:
-Display the collected data on a map using a geographical graphing tool.
-Show regional trends and variation in a simple, clear manner.
