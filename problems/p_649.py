def predictPartyVictory(senate):
    prev_que = list(senate)
    banned_r, banned_d = 0, 0

    while True:
        next_que = []
        r_in_que, d_in_que = 0, 0
        while prev_que:
            s = prev_que.pop(0)
            if s == "R":
                if banned_r == 0:
                    next_que.append(s)
                    r_in_que += 1
                    banned_d += 1
                else:
                    banned_r -= 1
            elif s == "D":
                if banned_d == 0:
                    next_que.append(s)
                    d_in_que += 1
                    banned_r += 1
                else:
                    banned_d -= 1
        prev_que = next_que
        if r_in_que == 0:
            return "Dire"
        elif d_in_que == 0:
            return "Radiant"

def main():
    senate = "DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR"
    print(predictPartyVictory(senate))

main()