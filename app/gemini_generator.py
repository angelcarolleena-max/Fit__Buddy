from .gemini_helper import generate_with_fallback


def generate_workout_gemini(username, age, weight, goal, intensity):
    prompt = f"""
You are FitBuddy, an AI fitness plan generator.

Create a personalized 7-day workout plan for this user:

Name: {username}
Age: {age}
Weight: {weight} kg
Fitness Goal: {goal}
Workout Intensity: {intensity}

Requirements:

1. Create a complete 7-day workout plan.
2. Clearly separate Day 1 through Day 7.
3. Include:
   - Warm-up
   - Main workout
   - Cool-down
   - Recovery/rest guidance
4. Give exercises with sets, repetitions, or duration where appropriate.
5. Keep the plan appropriate for the user's goal and intensity.
6. Include rest/recovery days where appropriate.
7. Do not recommend dangerous or extreme exercises.
8. Add a short safety note telling the user to stop if they
   experience pain or unusual symptoms and seek professional
   medical advice when appropriate.
9. Format the response using clear headings and bullet points.
10. Do not use markdown tables.

Return only the workout plan.
"""

    return generate_with_fallback(prompt)