# FitBuddy – AI Fitness Plan Generator

## 📌 Project Overview

FitBuddy is an AI-powered fitness application that generates personalized 7-day workout plans based on user information such as age, weight, fitness goal, and workout intensity.

The application also provides nutrition and recovery guidance and allows users to submit feedback and receive an updated workout plan.

An admin dashboard is included to view registered users, workout plans, feedback, and updated plans.

## 🎯 Objectives

- Generate personalized 7-day workout plans.
- Provide nutrition and recovery guidance.
- Allow users to provide feedback on their workout plans.
- Generate updated plans based on feedback.
- Store user and workout information using SQLite.
- Provide an admin dashboard for viewing saved users and plans.
- Integrate Google Gemini for AI-powered responses.

## ✨ Features

### User Features

- User registration through the FitBuddy form.
- Personalized workout plan generation.
- Nutrition and recovery tips.
- Feedback submission.
- Updated workout plan generation.

### Admin Features

- View all registered users.
- View user information.
- View original workout plans.
- View nutrition and recovery tips.
- View user feedback.
- View updated workout plans.

## 🛠️ Technologies Used

- Python
- FastAPI
- Jinja2
- HTML
- CSS
- SQLAlchemy
- SQLite
- Google Gemini API
- Uvicorn
- python-dotenv

## 🏗️ Project Structure

```text
FitBuddy/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   ├── schemas.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   ├── gemini_helper.py
│   └── updated_plan.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── all_users.html
│
├── static/
│   └── images/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔄 Application Workflow

```text
User enters fitness details
          ↓
Generate Workout Plan
          ↓
7-Day Workout Plan
          ↓
Nutrition & Recovery Tips
          ↓
User submits feedback
          ↓
Updated Workout Plan
          ↓
Data stored in SQLite
          ↓
Admin Dashboard
```

## 🚀 How to Run

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Do not upload the `.env` file to GitHub.

### 5. Run the Application

```bash
python -m uvicorn app.main:app --reload
```

### 6. Open the Application

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🗄️ Database

FitBuddy uses SQLite with SQLAlchemy for data persistence.

The application stores:

- User information
- Fitness goals
- Workout intensity
- Original workout plans
- Nutrition and recovery tips
- User feedback
- Updated workout plans

## 🤖 AI Integration

FitBuddy integrates Google Gemini to generate personalized fitness-related responses.

AI functionality is used for:

- 7-day workout plan generation
- Nutrition and recovery guidance
- Workout plan updates based on user feedback

The application also includes a local fallback response when the Gemini service is temporarily unavailable.

## 🔐 Security

- API keys are stored in environment variables.
- `.env` is excluded from Git using `.gitignore`.
- Sensitive configuration should not be committed to the repository.

## 🔮 Future Enhancements

- User authentication and login
- Advanced fitness analytics
- Progress tracking
- Exercise demonstrations
- AI-based calorie recommendations
- Mobile application
- Cloud database integration
- Cloud deployment
- More personalized AI fitness recommendations

## 👥 Team

Add your actual team member names here.

## 📄 License

This project was developed as an academic project for educational purposes.