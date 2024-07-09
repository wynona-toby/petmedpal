
# PETMEDPAL - Pet HealthCare Web Application

PetMedPal is a comprehensive pet care web application designed to streamline pet ownership responsibilities, while improving the health and wellbeing of the pets. The application employs a user-friendly interface to provide a variety of features including: monitoring pet health through digital pet profiles, scheduling and setting reminders` for vet appointments, vaccinations, and feeding times, dietary suggestions based on breed, age; and an easy access to the pet’s profile for ease of handling which makes it different from the other existing systems. 

## Features

- User Registration: Users can create profiles with personal information, including name, gender, contact details, and address.
- Pet Registrations: Pet owners can register their pets, providing details such as pet name, age, gender, breed, and any relevant prior medical information.
- Medical Services: Set reminders for vaccinations, nearest veterinary clinics, history of past vaccinations
- Wellness: Living conditions, grooming needs, and walking requirements
- Diet Consultations: Dietary needs, BMI (Body Mass Index) tracking, and guidance on foods to avoid.


## Web Design

View the design template of the project on Figma : [Figma Prototype Link](https://www.figma.com/proto/9nqLaexzGbOMSnn5qSKmWB/PMP(FINAL-DESIGNS)?node-id=0-1&t=12mKHqmJxZ9Mkid7-1)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/petmedpal.git
```

2. Navigate to the project directory:

```bash
cd petmedpal
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the application at [http://localhost:8000](http://localhost:8000)

## Usage

1. Create a superuser account:

```bash
python manage.py createsuperuser
```

2. Log in to the admin interface at [http://localhost:8000/admin](http://localhost:8000/admin) to manage users and events.

3. Visit [http://localhost:8000](http://localhost:8000) to access the application and start creating, viewing, and managing events.

## Run Server

1. Activate your virtual environment. The environment used here is eventsease
```bash
your_env_name\scripts\Activate
```
2. Run the server and access the output at port 8000
```bash
python manage.py runserver
```
3. Go to url http://127.0.0.1:8000/landing/ to access landing page and move forward with web view

