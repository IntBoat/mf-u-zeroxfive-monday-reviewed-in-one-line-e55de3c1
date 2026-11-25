#!/usr/bin/env python3
"""Monday, Reviewed in One Line (make.fun).

Writes the entry -- one-line review of my monday --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Monday's review: the standup ran long, the inbox doubled, and by 5pm my coffee had filed for overtime — one star, would not recommend, will be back tomorrow."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
