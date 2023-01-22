import argparse
from collections import namedtuple
from datetime import datetime
from typing import TypeAlias, Sequence, Tuple, MutableSequence

MonthDayPair = namedtuple("MonthDayPair", ["month", "day"])
CalculationStep = namedtuple("CalculationStep", ["explanation", "value"])
CalculationPath: TypeAlias = Sequence[CalculationStep]
MutableCalculationPath: TypeAlias = MutableSequence[CalculationStep]


def get_century_drift(year: int) -> Tuple[int, CalculationPath]:
    century: int = year // 100
    path: MutableCalculationPath = [
        CalculationStep("Take the century of the years date", century)
    ]
    century_is_before_18 = century < 18
    path.append(
        CalculationStep("Check if the century is before 18", century_is_before_18)
    )
    while century_is_before_18:
        century += 4
        path.append(CalculationStep("Add 400 years", century))
        century_is_before_18 = century < 18
        path.append(
            CalculationStep("Check if the result is before 18", century_is_before_18)
        )
    assert century >= 18, f"century: expected in {'{'}18..{'}'}, got {century}"

    century_is_after_22 = century > 22
    path.append(
        CalculationStep("Check if the century is after 22", century_is_after_22)
    )
    while century_is_after_22:
        century -= 4
        path.append(CalculationStep("Subtract 400 years", century))
        century_is_after_22 = century > 22
        path.append(
            CalculationStep("Check if the result is after 22", century_is_after_22)
        )

    assert century <= 22, f"century: expected in {'{'}..22{'}'}, got {century}"
    assert 18 <= century <= 22, f"century: expected in {'{'}18..22{'}'}, got {century}"
    drifts = {18: 5, 19: 3, 20: 2, 21: 0}
    century_drift = drifts[century]
    path.append(
        CalculationStep(
            "Get the results drift, {18: 5, 19: 3, 20: 2, 21: 0}", century_drift
        )
    )
    return century_drift, path


def get_decade_drift(year: int) -> Tuple[int, CalculationPath]:
    decade: int = year % 100
    drift: int = decade
    path: MutableCalculationPath = [
        CalculationStep("Take the decade of the years date", drift)
    ]
    drift_is_odd = drift % 2 != 0
    path.append(CalculationStep("Check if the decade is odd", drift_is_odd))
    if drift_is_odd:
        drift += 11
    path.append(CalculationStep("If yes add 11", drift))
    drift //= 2
    path.append(CalculationStep("Divide by 2", drift))
    drift_is_odd = drift % 2 != 0
    path.append(CalculationStep("Check if result is odd", drift_is_odd))
    if drift_is_odd:
        drift += 11
    path.append(CalculationStep("If yes add 11", drift))
    drift %= 7
    path.append(CalculationStep("Take result mod 7", drift))
    drift = 7 - drift
    path.append(CalculationStep("Subtract result from 7", drift))
    return drift, path


def get_doomsday(
    year: int, month: int, day: int
) -> Tuple[MonthDayPair, CalculationPath]:
    path: MutableCalculationPath = [
        CalculationStep("Take the month and day of the date", (month, day))
    ]
    is_leap_year: bool = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if 1 <= month <= 2:
        path.append(
            CalculationStep(
                "Check if the year is a leap year, if the month is January or February",
                is_leap_year,
            )
        )
    if month == 1:
        if not is_leap_year:
            doomsday = MonthDayPair(1, 3)
            explanation = "This months doomsday is January 3rd. Mnemonic: 3 years it is on the January 3rd"
        else:
            doomsday = MonthDayPair(1, 4)
            explanation = "This months doomsday is January 4th. Mnemonic: In the 4th year it is on the January 4th"
    elif month == 2:
        if not is_leap_year:
            doomsday = MonthDayPair(2, 28)
            explanation = "This months doomsday is February 28th."
        else:
            doomsday = MonthDayPair(2, 29)
            explanation = "This months doomsday is February 29th."
        explanation += " Mnemonic: The last day of February"
    elif month % 2 == 0:
        doomsday = MonthDayPair(month, month)
        explanation = f"This months doomsday is the {month}th of the month. Mnemonic: The {month}th of {month}"
    elif month == 3:
        doomsday = MonthDayPair(3, 0)
        explanation = "This months doomsday is the 0th of March. Mnemonic: The 0th of March is the last day of February"
    elif month == 5:
        doomsday = MonthDayPair(5, 9)
        explanation = (
            "This months doomsday is the 9th of May. Mnemonic: I work 9-5 at 7-11."
        )
    elif month == 7:
        doomsday = MonthDayPair(7, 11)
        explanation = (
            "This months doomsday is the 11th of July. Mnemonic: I work 9-5 at 7-11."
        )
    elif month == 9:
        doomsday = MonthDayPair(9, 5)
        explanation = "This months doomsday is the 5th of September. Mnemonic: I work 9-5 at 7-11."
    elif month == 11:
        doomsday = MonthDayPair(11, 7)
        explanation = (
            "This months doomsday is the 7th of November. Mnemonic: I work 9-5 at 7-11."
        )
    else:
        raise ValueError(f"month: expected in {'{'}1..12{'}'}, got {month}")
    path.append(CalculationStep(explanation, doomsday))
    return doomsday, path


def get_weekday(
    century_drift: int, decade_drift: int, doomsday: MonthDayPair, day: int
) -> Tuple[str, CalculationPath]:
    drift: int = (century_drift + decade_drift) % 7
    weekday: int = doomsday.day
    path: MutableCalculationPath = [CalculationStep("Take the doomsday", weekday)]

    weekday_is_after_day = weekday > day
    path.append(
        CalculationStep(
            "Check if the months doomsday is after the day", weekday_is_after_day
        )
    )
    while weekday_is_after_day:
        weekday -= 7
        path.append(CalculationStep("Subtract 7", weekday))
        weekday_is_after_day = weekday > day
        path.append(
            CalculationStep(
                "Check if the result is after the day", weekday_is_after_day
            )
        )
    assert weekday <= day, f"weekday: expected in {'{'}..{day}{'}'}, got {weekday}"

    weekday_is_at_least_one_week_before_day = weekday + 7 < day
    path.append(
        CalculationStep(
            "Check if the result is at least one week before the day",
            weekday_is_at_least_one_week_before_day,
        )
    )
    while weekday_is_at_least_one_week_before_day:
        weekday += 7
        path.append(CalculationStep("Add 7", weekday))
        weekday_is_at_least_one_week_before_day = weekday + 7 < day
        path.append(
            CalculationStep(
                "Check if the result is at least one week before the day",
                weekday_is_at_least_one_week_before_day,
            )
        )

    assert (
        weekday <= day <= weekday + 6
    ), f"weekday: expected in {'{'}{weekday}..{weekday + 6}{'}'}, got {day}"

    gap: int = day - weekday
    path.append(CalculationStep("Take the gap between the result and the day", gap))
    weekday = drift + gap
    path.append(CalculationStep("Add the drift to the gap", weekday))
    weekday %= 7
    path.append(CalculationStep("Take the result mod 7", weekday))
    weekdays = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }
    path.append(
        CalculationStep(
            "Get the weekday {0: Sunday, 1: Monday, 2: Tuesday, 3: Wednesday, 4: Thursday, 5: Friday, 6: Saturday}",
            weekdays[weekday],
        )
    )
    return weekdays[weekday], path


def calculate_weekday(year: int, month: int, day: int) -> Tuple[str, CalculationPath]:
    century_drift, path_century = get_century_drift(year)
    decade_drift, path_decade = get_decade_drift(year)
    doomsday, path_doomsday = get_doomsday(year, month, day)
    weekday, path_weekday = get_weekday(century_drift, decade_drift, doomsday, day)
    path: MutableCalculationPath = []
    path.extend(path_century)
    path.extend(path_decade)
    path.extend(path_doomsday)
    path.extend(path_weekday)
    return weekday, path


def main(year: int, month: int, day: int) -> None:
    weekday, path = calculate_weekday(year, month, day)
    for step in path:
        print(f"{step.explanation}: {step.value}")
    print(f"{year}-{month}-{day} is a {weekday}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Get the weekday of a date.")
    parser.add_argument(
        "year",
        nargs="?",
        type=int,
        default=None,
        help="The year of the date. Default: today's year.",
    )
    parser.add_argument(
        "month",
        nargs="?",
        type=int,
        default=None,
        help="The month of the date. Default: today's month.",
    )
    parser.add_argument(
        "day",
        nargs="?",
        type=int,
        default=None,
        help="The day of the date. Default: today's day.",
    )
    parser.add_argument(
        "--year",
        "-y",
        type=int,
        dest="year_option",
        default=None,
        help="The year of the date. Default: today's year.",
    )
    parser.add_argument(
        "--month",
        "-m",
        type=int,
        dest="month_option",
        default=None,
        help="The month of the date. Default: today's month.",
    )
    parser.add_argument(
        "--day",
        "-d",
        type=int,
        dest="day_option",
        default=None,
        help="The day of the date. Default: today's day.",
    )

    args, _ = parser.parse_known_intermixed_args()
    return args


if __name__ == "__main__":
    args: argparse.Namespace = parse_args()
    today: datetime = datetime.today()
    year: int = args.year or args.year_option or today.year
    month: int = args.month or args.month_option or today.month
    day: int = args.day or args.day_option or today.day

    # print(f"{year}-{month}-{day} is a {datetime(year, month, day).strftime('%A')}.")

    main(year, month, day)
