#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 27, 2021
# Converts level mark into average percentage


def level_4_plus():
    return "97.5%"


def level_4_():
    return "90.5%"


def level_4_minus():
    return "83%"


def level_3_plus():
    return "78%"


def level_3_():
    return "74.5%"


def level_3_minus():
    return "71%"


def level_2_plus():
    return "68%"


def level_2_():
    return "64.5%"


def level_2_minus():
    return "61%"


def level_1_plus():
    return "58%"


def level_1_():
    return "54.5%"


def level_1_minus():
    return "51%"


def level_R():
    return "24.5%"


def invalid_input():
    return -1


def main():
    mark_level = (input("Enter mark level: "))

    if (mark_level == "4+"):
        level_4_plus()
        level_percent = level_4_plus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "4":
        level_4_()
        level_percent = level_4_()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "4-":
        level_4_minus()
        level_percent = level_4_minus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "3+":
        level_3_plus()
        level_percent = level_3_plus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "3":
        level_3_()
        level_percent = level_3_()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "3-":
        level_3_minus()
        level_percent = level_3_minus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "2+":
        level_2_plus()
        level_percent = level_2_plus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "2":
        level_2_()
        level_percent = level_2_()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "2-":
        level_2_minus()
        level_percent = level_2_minus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "1+":
        level_1_plus()
        level_percent = level_1_plus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "1":
        level_1_()
        level_percent = level_1_()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "1-":
        level_1_minus()
        level_percent = level_1_minus()
        print("Level {0} is {1}".format(mark_level, level_percent))
    elif mark_level == "R":
        level_R()
        level_percent = level_R()
        print("Level {0} is {1}".format(mark_level, level_percent))
    else:
        invalid_input()
        invalid = invalid_input()
        print("{}".format(invalid))
    print("Done.")


if __name__ == "__main__":
    main()
