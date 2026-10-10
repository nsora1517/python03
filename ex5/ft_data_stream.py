#!/usr/bin/env python3
import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield (event[0], event[1])


def main() -> None:
    gen = gen_event()
    events: list[tuple[str, str]] = []
    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    for _ in range(10):
        events = events + [next(gen)]
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
