import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    args = sys.argv
    total_args = len(args)

    print(f"Program name: {args[0]}")

    if total_args == 1:
        print("No arguments provided!")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Arguments received: {total_args - 1}")

        for i in range(1, total_args):
            print(f"Argument {i}: {args[i]}")

        print(f"Total arguments: {total_args}")
