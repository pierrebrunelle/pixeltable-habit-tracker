"""Habit Tracker API built with Pixeltable.

    pxt schema update app.py habits
    pxt service run app.py habits
"""
import pixeltable as pxt
import pixeltable.functions as pxtf
from pixeltable.serving import FastAPIRouter

from udfs import habit_blurb, streak_label

# ---- tables ----
TableModel = pxt.model_base()


class Habits(TableModel, name='habits'):
    id = pxt.Column(value=pxtf.uuid.uuid7(), primary_key=True)
    name: pxt.String
    category: pxt.String
    streak_days: pxt.Int | None
    notes: pxt.String | None

    label = streak_label(streak_days)
    name_upper = pxtf.string.upper(name)
    name_blurb = habit_blurb(name, category)


# ---- queries ----
@pxt.query
def by_category(category: str):
    """Habits in a category, longest streak first."""
    return Habits.where(Habits.category == category).select(
        Habits.id, Habits.name, Habits.streak_days, Habits.label
    ).order_by(Habits.streak_days, asc=False)


# ---- routes ----
habits_api = FastAPIRouter(name='habits_api')
habits_api.add_insert_route(
    Habits, path='/habits',
    inputs=[Habits.name, Habits.category, Habits.streak_days, Habits.notes],
    outputs=[Habits.id, Habits.label, Habits.name_upper, Habits.name_blurb],
)
habits_api.add_update_route(Habits, path='/habits/update', inputs=[Habits.streak_days],
                            outputs=[Habits.id, Habits.streak_days, Habits.label])
habits_api.add_compute_route(Habits, path='/streak-label', inputs=[Habits.streak_days], outputs=[Habits.label])
habits_api.add_query_route(path='/habits/by-category', query=by_category, method='get')
