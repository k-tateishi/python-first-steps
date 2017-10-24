def get_sum(**args):
    count = 0
    for i in range(args['start'], args['end']+1):
        count += i
    print(count)

get_sum(start=1, end=10)
