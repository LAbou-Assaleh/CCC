import math
def main(vals) -> int:
    nums = {}
    vals = [int(x) for x in vals]
    if (vals[0]+1)*(vals[0]/2) < vals[2]:
        print(-1)
    elif vals[0] > vals[2]:
        print(-1)
    else:
        track = 1
        current = 0
        location = 0
        increase = 1
        debug = 0
        seq = []
        for i in range(1, vals[0]+1):
            if track > vals[1]:
                track = 1
            if i > 1:
                if seq[location] == track:
                    increase = i-location-1
                else:
                    increase = i - location
            else:
                increase = i - location
            if debug:
                print(f"track is: {track} current is: {current} location is: {location} increase is: {increase} i is: {i} seq is: {seq} nums is: {nums}")
            if increase+vals[0]-i >= vals[2]-current and i != vals[0] and i != 1:
                place = ((vals[2]-current)-(vals[0]-i))
                if place > vals[1] or place > len(seq):
                    pass
                else:
                    track = seq[place*-1]
            elif current + increase > vals[2] and i == vals[0]:
                track = seq[((vals[2]-current)%(vals[1]+1))*-1]
            if track not in nums.keys():
                nums[track] = len(seq)
            else:
                location = nums[track]+1
                nums[track] = len(seq)
                increase = i - location
            current += increase
            seq.append(track)
            track += 1
        if current == vals[2]:
            text = ""
            for i in seq:
                text += str(i) + " "
            print(text[:-1])
        else:
            print(-1)
if __name__ == '__main__':
    vals = input().split()
    main(vals)

