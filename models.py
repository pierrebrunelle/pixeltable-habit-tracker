"""The habits table."""
import pixeltable as pxt
import pixeltable.functions as pxtf

from udfs import habit_blurb, streak_label

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
