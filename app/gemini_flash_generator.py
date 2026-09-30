from .gemini_helper import generate_with_fallback


def generate_nutrition_tip_with_flash(username, age, weight, goal, intensity):
    prompt = f"""
You are FitBuddy, an AI fitness and wellness assistant.

Create a concise nutrition and recovery tip for:

Name: {username}
Age: {age}
Weight: {weight} kg
Fitness Goal: {goal}
Workout Intensity: {intensity}

Include:
- General nutrition guidance
- Protein and balanced food guidance
- Hydration
- Sleep and recovery
- Practical advice that is easy to follow

Keep the response under 250 words.

Do not provide medical diagnosis or treatment.
Return only the nutrition and recovery advice.
"""

    return generate_with_fallback(prompt)