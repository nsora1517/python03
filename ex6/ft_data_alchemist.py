#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    name_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
                 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {name_list}")

    upper_list = [name.capitalize() for name in name_list]
    print(f"New list with all names capitalized: {upper_list}")

    only_upper_list = [name for name in name_list if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_upper_list}")

    print()

    score_dict = {name: random.randint(1, 100) for name in upper_list}
    print(f"Score dict: {score_dict}")

    aver = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {aver}")

    high_dict = {name: score_dict[name] for name in score_dict
                 if score_dict[name] > aver}
    print(f"High scores: {high_dict}")


if __name__ == "__main__":
    main()
