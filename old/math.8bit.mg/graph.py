
def graph():
    for n in range(256):
        yield (
            "math.8b",
            f"{n:d} (base 10)",
            f"{n:08b} (base 2)",
        )

