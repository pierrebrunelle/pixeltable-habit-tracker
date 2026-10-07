"""Pixeltable UDFs for the habit tracker (recorded by module path, e.g. `udfs.streak_label`)."""
import pixeltable as pxt


@pxt.udf
def streak_label(streak_days: int | None) -> str:
    """Bucket a streak into a friendly label."""
    d = streak_days or 0
    if d == 0:
        return 'not started'
    if d < 7:
        return 'getting started'
    if d < 30:
        return 'on a roll'
    return 'unstoppable'


@pxt.udf
def habit_blurb(name: str, category: str) -> str:
    return f'{name} ({category})'
