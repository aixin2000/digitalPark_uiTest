import random


def randomPhone():
    headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                "186", "187", "188", "189"]
    # print(random.choice(headList) + "".join(random.choice("0123456789") for i in range(8)))
    return random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))


if __name__ == '__main__':
    randomPhone()
