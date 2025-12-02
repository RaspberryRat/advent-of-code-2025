
f = open("./data/day1data.txt", 'r')
lines = f.readlines()
f.close()

def calc_zero(lines:list[str]) -> int:
    dial = 50
    zeroCount = 0
    # lines = ['L250', 'R80', 'R20']
    for line in lines:
        line = line.strip()

        direction = line[:1]
        distance = int(line[1:])

        oldDial = dial
        passZero = abs(distance) // 100
        remainder = abs(distance) % 100

        if direction == 'L':
            dial = (dial - distance) % 100
            if remainder >= oldDial and oldDial != 0:
                zeroCount += 1
        else:
            dial = (dial + distance) % 100
            if remainder > 0 and oldDial + remainder >= 100:
                zeroCount += 1

        zeroCount += passZero
    return zeroCount

print(f"num zeros: {calc_zero(lines)}")

