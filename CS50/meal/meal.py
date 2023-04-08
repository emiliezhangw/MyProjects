def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    if "a.m" in time or "p.m" in time:
        if "a.m" in time:
            hour, minute = time.split()[0].split(":")
            hour, minute = float(hour), float(minute)
        else:
            hour, minute = time.split()[0].split(":")
            hour, minute = float(hour) + 12, float(minute)
        return round(hour + minute / 60, 2)
    else:
        hour, minute = time.split(":")
        return round(float(hour) + float(minute) / 60, 2)


if __name__ == "__main__":
    main()
