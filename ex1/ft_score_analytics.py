import sys


def main() -> None:
    args = sys.argv[1:]
    score: list[int] = []
    print("=== Player Score Analytics ===")
    for arg in args:
        try:
            score = score + [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if len(score) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score) / len(score)}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")


if __name__ == "__main__":
    main()
