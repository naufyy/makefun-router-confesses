#!/usr/bin/env python3
"""The Router Confesses entry: writes the winning one-liner to /output/entry.txt.

The line is the router's own excuse for dropping the connection at the
climax of a movie, chosen by proxy judging (Groq) from six candidates
against the published judge brief. The router speaks as a patient,
long-ignored appliance that finally takes its bow at the worst moment.
"""

import os

LINE = "I waited ninety minutes for the kiss, the confession, the twist \u2014 then I realized you only ever notice me when I stop. So I stopped."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
