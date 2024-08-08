# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:


"""
# view the queue
print(".................\nViewing queue 1st way :\n", gfs)

print(".................\nViewing queue 2nd way :\n")
for line in gfs:
    print(line)

print(".................\nViewing queue 3rd way :\n")
print([l for l in gfs])
"""

from collections import deque


def view(q):
    for x in q:
        print(x)
    print()


def main():
    # defining queue using deque will help in doing queue operation, actually it can work like 2 way queue
    gfs = deque(["Smarika", "Deeya", "Anjana", "Deepa"])
    # view how queue looks like at first
    view(gfs)
    # adding items in queue
    gfs.append("Stranger")
    # view after append
    view(gfs)
    # pop item in queue
    gfs.popleft()
    # view after popping
    view(gfs)
    gfs.appendleft("Crush")
    view(gfs)


if __name__ == "__main__":
    main()
