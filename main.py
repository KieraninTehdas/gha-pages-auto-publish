from pprint import pprint
import datetime
import json

TRIGGER_PAYLOAD_PATH = '/github/workflow/event.json'


def main() -> None:
    now = datetime.date.today()
    print(now.isoformat())

    with open(TRIGGER_PAYLOAD_PATH, 'r') as f:
        input_event = json.load(f)

    pprint(input_event)


if __name__ == "__main__":
    main()
