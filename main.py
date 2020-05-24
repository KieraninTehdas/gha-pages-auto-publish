from pprint import pprint
import datetime
import json

TRIGGER_PAYLOAD_PATH = '/github/workflow/event.json'


def main() -> None:
    now = datetime.date.today()
    print(now.isoformat())

    with open(TRIGGER_PAYLOAD_PATH, 'r') as f:
        input_event = json.load(f)

    schedule = input_event['schedule']


def parse_cron(cron_expression: str) -> datetime.timedelta:
    expressions = cron_expression.split(' ')

    if len(expressions) != 5:
        raise ValueError(
            f'Unexpected Cron Expression Length. Expected 6: Found {len(expressions)}')

    datetime.timedelta(m)


if __name__ == "__main__":
    ['minutes', 'hours']
    pprint(datetime.timedelta(**{'minutes': 1}))
