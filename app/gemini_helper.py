import time
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

client = None

if API_KEY:
    client = genai.Client(api_key=API_KEY)


MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
]


def generate_with_fallback(prompt):
    """
    Try Gemini first.
    If Gemini is temporarily unavailable, use a local fallback
    so the FitBuddy application can continue working.
    """

    if client:
        for model in MODELS:

            for attempt in range(2):

                try:
                    print(
                        f"Trying Gemini model: {model} "
                        f"(attempt {attempt + 1})"
                    )

                    response = client.models.generate_content(
                        model=model,
                        contents=prompt
                    )

                    if response.text:
                        print(f"Gemini success: {model}")
                        return response.text

                except Exception as error:

                    error_text = str(error)

                    print(
                        f"Gemini error from {model}: "
                        f"{error_text}"
                    )

                    if "503" in error_text or "UNAVAILABLE" in error_text:

                        wait_time = 2 ** attempt

                        print(
                            f"Gemini temporarily unavailable. "
                            f"Retrying in {wait_time} seconds..."
                        )

                        time.sleep(wait_time)

                    else:
                        break

    print("Gemini unavailable. Using FitBuddy local fallback.")

    return local_fitbuddy_response(prompt)


def local_fitbuddy_response(prompt):
    """
    Local fallback response used when Gemini is unavailable.
    """

    prompt_lower = prompt.lower()

    # Workout plan
    if "7-day workout plan" in prompt_lower:

        return """
FITBUDDY 7-DAY WORKOUT PLAN

DAY 1 — CHEST & TRICEPS
• Warm-up: 5–10 minutes brisk walking
• Push-ups: 3 sets × 10 repetitions
• Dumbbell Chest Press: 3 sets × 10 repetitions
• Incline Push-ups: 3 sets × 8 repetitions
• Triceps Extensions: 3 sets × 12 repetitions
• Cool-down: 5 minutes stretching
• Recovery: Drink water and rest adequately.

DAY 2 — BACK & BICEPS
• Warm-up: 5–10 minutes
• Lat Pulldown: 3 sets × 10 repetitions
• Seated Cable Row: 3 sets × 10 repetitions
• Dumbbell Curls: 3 sets × 12 repetitions
• Hammer Curls: 3 sets × 10 repetitions
• Cool-down stretching
• Recovery: Allow the muscles to recover.

DAY 3 — LEGS
• Warm-up: 5–10 minutes
• Bodyweight Squats: 3 sets × 12 repetitions
• Lunges: 3 sets × 10 repetitions
• Leg Press: 3 sets × 10 repetitions
• Calf Raises: 3 sets × 15 repetitions
• Cool-down stretching
• Recovery: Rest and stay hydrated.

DAY 4 — ACTIVE RECOVERY
• 20–30 minutes light walking
• Gentle full-body stretching
• Mobility exercises
• Focus on hydration and sleep.

DAY 5 — SHOULDERS & CORE
• Warm-up: 5–10 minutes
• Shoulder Press: 3 sets × 10 repetitions
• Lateral Raises: 3 sets × 12 repetitions
• Front Raises: 3 sets × 10 repetitions
• Plank: 3 × 30 seconds
• Crunches: 3 sets × 12 repetitions
• Cool-down stretching

DAY 6 — FULL BODY
• Warm-up: 5–10 minutes
• Squats: 3 sets × 10 repetitions
• Push-ups: 3 sets × 10 repetitions
• Dumbbell Rows: 3 sets × 10 repetitions
• Lunges: 3 sets × 10 repetitions
• Plank: 3 × 30 seconds
• Cool-down stretching

DAY 7 — REST & RECOVERY
• Complete rest or gentle walking
• Light stretching
• Hydration
• Focus on quality sleep and recovery.

SAFETY NOTE
Start gradually and use proper exercise technique.
Stop if you experience pain, dizziness, breathing difficulty,
or unusual symptoms and seek appropriate professional advice.
"""


    # Nutrition
    if "nutrition" in prompt_lower or "recovery" in prompt_lower:

        return """
FITBUDDY NUTRITION & RECOVERY TIP

• Eat balanced meals containing protein, carbohydrates,
  healthy fats, vegetables and fruits.
• Include protein-rich foods such as eggs, milk, curd,
  pulses, beans, fish or other suitable protein sources.
• Drink enough water throughout the day.
• Eat regular meals rather than skipping meals.
• Include carbohydrates around workouts for energy.
• Sleep around 7–9 hours when possible.
• Give your muscles enough recovery time between
  demanding workouts.
• Increase food intake gradually if your goal is
  healthy muscle gain.

This is general fitness information and is not medical advice.
"""


    # Updated workout
    if "updated 7-day workout plan" in prompt_lower:

        return """
FITBUDDY UPDATED 7-DAY WORKOUT PLAN

The plan has been adjusted according to your feedback.

DAY 1 — UPPER BODY
• Warm-up: 10 minutes
• Push-ups: 3 × 10
• Chest Press: 3 × 10
• Rows: 3 × 10
• Biceps Curls: 3 × 12
• Cool-down stretching

DAY 2 — LOWER BODY
• Warm-up: 10 minutes
• Squats: 3 × 12
• Lunges: 3 × 10
• Leg Press: 3 × 10
• Calf Raises: 3 × 15
• Cool-down stretching

DAY 3 — RECOVERY
• Light walking
• Mobility exercises
• Full-body stretching

DAY 4 — UPPER BODY
• Shoulder Press: 3 × 10
• Lat Pulldown: 3 × 10
• Dumbbell Press: 3 × 10
• Triceps Extensions: 3 × 12
• Cool-down stretching

DAY 5 — LOWER BODY & CORE
• Squats: 3 × 10
• Step-ups: 3 × 10
• Calf Raises: 3 × 15
• Plank: 3 × 30 seconds
• Crunches: 3 × 12

DAY 6 — FULL BODY
• Push-ups: 3 × 10
• Squats: 3 × 10
• Rows: 3 × 10
• Lunges: 3 × 10
• Plank: 3 × 30 seconds

DAY 7 — REST
• Rest
• Light walking if comfortable
• Stretching
• Hydration and good sleep

SAFETY NOTE
Perform exercises with proper technique and appropriate
resistance. Stop if you experience pain or unusual symptoms.
"""

    return """
FitBuddy is currently using its offline fitness assistant.

Please try again later to use the Gemini-powered personalized
response.
"""