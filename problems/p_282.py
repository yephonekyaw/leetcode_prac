import pprint
def addOperators(num, target):
    if int(num) != 0 and int(num) == target:
        return [num]

    combinations = []
    operators = "*+-"
    def find_combinations(start, que, op, per_val):  
        for lg in range(start + 1, len(num) + 1):
            cur = int(num[start:lg])
            # if leading zeros, no more calculation
            if len(str(cur)) != len(num[start:lg]):
                continue

            val = per_val
            # if operator is None, there is no need to calculate
            if op is None:
                que.append(cur)
                for new_op in operators:
                    find_combinations(lg, que, new_op, cur)
                que.pop()
            else:
                # just add, subtract, or multiply with the current val
                if len(que) == 1:
                    val = val * cur if op == "*" else val + cur if op == "+" else val - cur
                else:
                    if op == "*":
                        i, l, prod = 0, len(que) - 1, 1
                        while l - i > 0:
                            if str(que[l - i]).isdigit():
                                prod *= que[l - i]
                            else:
                                last_op = que[l - i]
                                if last_op != "*":
                                    break
                            i += 1
                        if last_op == "*":
                            val *= cur
                        elif last_op == "+":
                            val = (val - prod) + (prod * cur)
                        else:
                            val = (val + prod) - (prod * cur)
                    else:
                        val = val + cur if op == "+" else val - cur
                que.append(op)
                que.append(cur)
                
                if lg == len(num) and val == target:
                    combinations.append("".join([str(i) for i in que]))
                
                if lg < len(num):
                    for new_op in operators:
                        find_combinations(lg, que, new_op, val)
                que.pop()
                que.pop()

    find_combinations(0, [], None, None)
    return combinations

def main():
    num = "2147"
    target = -2147
    pprint.pprint(addOperators(num, target))

main()