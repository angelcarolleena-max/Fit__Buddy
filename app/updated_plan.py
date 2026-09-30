from .gemini_helper import generate_with_fallback


def update_workout_plan(original_plan, feedback):
    prompt = f"""
You are FitBuddy, an AI fitness plan assistant.

Here is the user's original 7-day workout plan:

{original_plan}

The user provided this feedback:

{feedback}

Create an updated 7-day workout plan based on the feedback.

Requirements:

1. Keep the plan personalized and practical.
2. Clearly separate Day 1 through Day 7.
3. Include:
   - Warm-up
   - Main workout
   - Cool-down
   - Recovery/rest guidance
4. Modify the plan according to the user's feedback.
5. Keep useful parts of the original plan when appropriate.
6. Do not recommend dangerous or extreme exercises.
7. Include a short safety note.
8. Use clear headings and bullet points.
9. Do not use markdown tables.

Return only the updated workout plan.
"""

    return generate_with_fallback(prompt)