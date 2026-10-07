"""Habit Tracker API built with Pixeltable.

    pxt schema update app.py habits
    pxt service run app.py habits
"""
from pixeltable.serving import FastAPIRouter

from models import Habits, TableModel  # noqa: F401  (TableModel lets `pxt schema` find the models)
from queries import by_category

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
