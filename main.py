import os
import glob
import datetime
import json

TRIGGER_PAYLOAD_PATH = '/github/workflow/event.json'
WORKSPACE_PATH = '/github/workspace/'


def main() -> None:
    now = datetime.date.today()
    print(now.isoformat())

    with open(TRIGGER_PAYLOAD_PATH, 'r') as f:
        input_event = json.load(f)

    schedule = input_event['schedule']
    # TODO: could have an optional input that specifies last run time? Useful for on-demand?

    # TODO: list _posts content. Take first 10 chars to get date. Parse and find between last run and current run


def strip_cron_expression(cron_expression: str) -> int:
    return int(cron_expression.replace('*', '').replace('/', ''))


def get_last_run_date(cron_expression: str) -> datetime.date:
    """Work out the last action run date based on the cron schedule.
        Assumes that the schedule never changes, which isn't great.
        For now only works with a set time every n days.
    """

    expressions = cron_expression.split(' ')

    if len(expressions) != 5:
        raise ValueError(
            f'Unexpected Cron Expression Length. Expected 5: Found {len(expressions)}')

    every_n_days = datetime.timedelta(
        days=strip_cron_expression(expressions[2]))

    return datetime.date.today() - every_n_days


def construct_glob_params(today_date: datetime.date, last_run_date: datetime.date) -> str:
    td = today_date - last_run_date

    return td


if __name__ == "__main__":
    lrd = get_last_run_date("0 12 */3 * *")

    print(construct_glob_params(datetime.date.today(), lrd))
