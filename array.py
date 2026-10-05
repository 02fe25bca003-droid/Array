def main():
    scores = [78, 85, 90, 66, 88]
    total = sum(scores)
    average = total / len(scores)
    print("=== main/master branch output ===")
    print(f"Score:{scores}")
    print(f"Sum:{total}")
    print(f"Average:{average}")
    print("\n=== local branch output(max & min) ===")
    print(f"Max:{max(scores)}")
    print(f"Min:{min(scores)}")


if __name__ == "__main__":
    main()
