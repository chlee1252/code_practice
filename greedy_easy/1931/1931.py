N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))

end = meetings[0][1]
count = 1
for meeting in meetings[1:]:
    start, cur_end = meeting
    if start >= end:
        count += 1
        end = cur_end

print(count) 