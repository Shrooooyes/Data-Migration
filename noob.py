import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description='Safe shutdown helper (noob.py)')
    parser.add_argument('--shutdown', action='store_true', help='Perform shutdown command')
    parser.add_argument('--delay', type=int, default=42, help='Seconds until shutdown (default 42)')
    parser.add_argument('--message', default='Hello darkness my old frandd', help='Shutdown message')
    parser.add_argument('--dry-run', action='store_true', help='Show command without executing')

    args = parser.parse_args()

    cmd = f"shutdown /s /t {args.delay} /c \"{args.message}\""

    if args.dry_run:
        print(f"[dry-run] {cmd}")
        sys.exit(0)

    if not args.shutdown:
        print("No action taken. Run with --shutdown to perform shutdown.")
        print(f"Command would be: {cmd}")
        sys.exit(0)

    confirm = input(f"Execute: {cmd}? (y/N): ")
    if confirm.strip().lower() != 'y':
        print('Cancelled')
        sys.exit(0)

    os.system(cmd)


if __name__ == '__main__':
    main()