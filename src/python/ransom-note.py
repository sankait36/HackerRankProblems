def ransom_note(magazine, ransom):
    mag = {}
    for word in magazine:
        if word not in mag:
            mag[word] = 0
        mag[word] += 1

    ran = {}
    for word in ransom:
        if word not in mag:
            return False
        else:
            if word not in ran:
                ran[word] = 0
            ran[word] += 1

    for key in mag:
        if key in ran:
            if ran[key] > mag[key]:
                return False

    return True    

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
    
