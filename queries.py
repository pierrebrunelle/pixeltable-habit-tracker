"""Queries over the habits table."""
import pixeltable as pxt

from models import Habits


@pxt.query
def by_category(category: str):
    """Habits in a category, longest streak first."""
    return Habits.where(Habits.category == category).select(
        Habits.id, Habits.name, Habits.streak_days, Habits.label
    ).order_by(Habits.streak_days, asc=False)
