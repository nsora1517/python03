#!/usr/bin/env python3
import random


all_achiev = ['Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
              'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
              'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
              'Boss Slayer', 'Hidden Path Finder']


def gen_player_achievements() -> set[str]:
    num = random.randint(1, len(all_achiev))
    achiev = random.sample(all_achiev, num)
    return set(achiev)


def main() -> None:
    a = gen_player_achievements()
    b = gen_player_achievements()
    c = gen_player_achievements()
    d = gen_player_achievements()
    set_all_achiev = set(all_achiev)
    print(f"Player Alice: {a}")
    print(f"Player Bob: {b}")
    print(f"Player Charlie: {c}")
    print(f"Player Dylan: {d}")
    print()
    print(f"All distinct achievements: {set.union(a, b, c, d)}")
    print()
    print(f"Common achievements: {set.intersection(a, b, c, d)}")
    print()
    print(f"Only Alice has: {a.difference(b, c, d)}")
    print(f"Only Bob has: {b.difference(a, c, d)}")
    print(f"Only Charlie has: {c.difference(a, b, d)}")
    print(f"Only Dylan has: {d.difference(a, b, c)}")
    print()
    print(f"Alice is missing: {set_all_achiev.difference(a)}")
    print(f"Bob is missing: {set_all_achiev.difference(b)}")
    print(f"Charlie is missing: {set_all_achiev.difference(c)}")
    print(f"Dylan is missing: {set_all_achiev.difference(d)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    main()
