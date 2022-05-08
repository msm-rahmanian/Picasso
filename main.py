from circle import Circle


def main():
    circle1 = Circle("circle", 1)
    area_circle = circle1.calculate_area()
    print(f"area of {circle1.name} is {area_circle}")


if __name__ == "__main__":
    main()
