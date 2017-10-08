def countValleys(n, steps):
    height = 0
    prev_height = 0
    count = 0
    valleys = 0
    for step in steps:
        if count == 0:
            if step == 'U':
                height += 1
            else:
                height -= 1
            count += 1
        else:
            if step == 'U':
                prev_height = height
                height += 1
                if prev_height < 0 and height == 0: # Crossed a valley
                    valleys += 1
            else: # If you're going down, you can't cross a valley
                prev_height = height
                height -= 1
    return valleys

n = int(raw_input().strip())
steps = raw_input().strip()
valleys = countValleys(n, steps)
print valleys