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


def main() -> None:
    gen = gen_event()
    events: list[tuple[str, str]] = []
    print("=== Game Data Stream Processor ===")

    for i in range(3):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    for i in range(10):
        events = events + [next(gen)]
    print(f"Built list of 10 events: {events}")


if __name__ == "__main__":
    main()
