from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import (
    get_db,
    save_user,
    update_plan,
    get_original_plan,
    get_user,
    get_all_users
)

from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan


router = APIRouter()

templates = Jinja2Templates(directory="templates")


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


# ---------------------------------------------------------
# GENERATE WORKOUT
# ---------------------------------------------------------

@router.post("/generate-workout", response_class=HTMLResponse)
async def generate_workout(
    request: Request,
    user_id: str = Form(...),
    username: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    db: Session = Depends(get_db)
):

    try:

        # Generate 7-day workout plan
        workout_plan = generate_workout_gemini(
            username=username,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity
        )

        # Generate nutrition tip
        nutrition_tip = generate_nutrition_tip_with_flash(
            username=username,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity
        )

        # Check whether user already exists
        existing_user = get_user(db, user_id)

        if existing_user:

            existing_user.username = username
            existing_user.age = age
            existing_user.weight = str(weight)
            existing_user.goal = goal
            existing_user.intensity = intensity
            existing_user.original_plan = workout_plan
            existing_user.updated_plan = None
            existing_user.nutrition_tip = nutrition_tip
            existing_user.feedback = None

            db.commit()
            db.refresh(existing_user)

        else:

            save_user(
                db=db,
                user_id=user_id,
                username=username,
                age=age,
                weight=weight,
                goal=goal,
                intensity=intensity,
                original_plan=workout_plan,
                nutrition_tip=nutrition_tip
            )

        # Show result page
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "user_id": user_id,
                "username": username,
                "workout_plan": workout_plan,
                "nutrition_tip": nutrition_tip,
                "revised_plan": None,
                "feedback": None
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "error": str(e),
                "username": username,
                "user_id": user_id
            }
        )


# ---------------------------------------------------------
# SUBMIT FEEDBACK
# ---------------------------------------------------------

@router.post("/submit-feedback", response_class=HTMLResponse)
async def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db)
):

    try:

        # Get original workout plan
        original_plan = get_original_plan(db, user_id)

        if not original_plan:

            return templates.TemplateResponse(
                request=request,
                name="result.html",
                context={
                    "request": request,
                    "error": "No workout plan found for this User ID.",
                    "user_id": user_id
                }
            )

        # Generate revised plan using feedback
        revised_plan = update_workout_plan(
            original_plan=original_plan,
            feedback=feedback
        )

        # Save revised plan
        update_plan(
            db=db,
            user_id=user_id,
            updated_plan=revised_plan,
            feedback=feedback
        )

        # Get user information
        user = get_user(db, user_id)

        # Show updated result
        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "user_id": user_id,
                "username": user.username if user else "User",
                "workout_plan": None,
                "revised_plan": revised_plan,
                "nutrition_tip": user.nutrition_tip if user else "",
                "feedback": feedback,
                "updated": True
            }
        )

    except Exception as e:

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "request": request,
                "error": str(e),
                "user_id": user_id
            }
        )


# ---------------------------------------------------------
# ADMIN / COACH DASHBOARD
# ---------------------------------------------------------

@router.get("/view-all-users", response_class=HTMLResponse)
async def view_all_users(
    request: Request,
    db: Session = Depends(get_db)
):

    users = get_all_users(db)

    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={
            "request": request,
            "users": users
        }
    )