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