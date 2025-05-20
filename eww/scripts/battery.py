#!/usr/bin/env python3
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: battery.py [-c | -s]")
        exit(-1)

    option = sys.argv[1]

    charge_icons = {
        'Charging': '🔌',
        'Not charging': '🔋',
        'Full': '🔋',
        'Discharging': '🗲'
    }

    capacity = int(open("/sys/class/power_supply/BAT0/capacity").read())
    status = open("/sys/class/power_supply/BAT0/status").read().strip()

    if (option == '-c'):
        print(capacity)
        exit(0)

    if (option == '-s'):
        if capacity > 90:
            print("false")
        else:
            print("true")
        exit(0)

    if (option == '-i'):
        print(charge_icons.get(status, "❓"))
        exit(0)

    print("Usage: battery.py [-c | -s]")
    exit(-1)


if __name__ == "__main__":
    main()
