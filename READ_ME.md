# Create a virtual environment and install dependencies
conda env create -f environment.yml
conda activate <env_name>

pip install -r requirements.txt

# Run the frontend (using Vite) in a separate terminal, from the fyp_frontend directory, after activating the virtual environment
npm install
npm run dev

# Run the backend (using django) in a separate terminal, from the fyp_backend directory, after activating the virtual environment
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Django admin page can be accessed at http://localhost:8000/admin after running backend
username: muhbhu
password: muhbhu

# Website login credentials or create your own using the register page
username: mo1
password: mo123456
username: bob1
password: bob123456

# OR Create a superuser to access the admin page using the following command and follow the prompts
python manage.py createsuperuser
