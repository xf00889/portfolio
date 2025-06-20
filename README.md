# Portfolio Website

A personal portfolio website built with Django.

## Deployment Instructions for Render

### Prerequisites
- A [Render](https://render.com/) account
- Git repository with your project

### Steps to Deploy

1. **Login to Render**
   - Go to [render.com](https://render.com/) and sign in or create an account

2. **Create a New Web Service**
   - Click on "New +" button in the dashboard
   - Select "Web Service"

3. **Connect Your Repository**
   - Connect your GitHub/GitLab account if not already connected
   - Select the portfolio repository

4. **Configure the Web Service**
   - Name: `portfolio` (or your preferred name)
   - Environment: `Python`
   - Region: Choose the closest to your target audience
   - Branch: `main` (or your default branch)
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn portfolio.wsgi:application`
   - Plan: Free

5. **Add Environment Variables**
   - Click on "Advanced" and add the following environment variables:
     - `SECRET_KEY`: (Generate a secure random key)
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `.onrender.com`
     - `PYTHON_VERSION`: `3.10.13`

6. **Deploy**
   - Click "Create Web Service"
   - Wait for the build and deployment process to complete

7. **Access Your Website**
   - Once deployed, your site will be available at `https://[service-name].onrender.com`

## Local Development

### Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver` 