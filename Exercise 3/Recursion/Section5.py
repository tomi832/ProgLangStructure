def sortedzip_rec(lists):
    if not lists:
        return []
    return [sorted(lists[0])] + sortedzip_rec(lists[1:])

def sortedzip(lists):
    return zip(*sortedzip_rec(lists))

###############

def sortedzip_tail(lists):
    def helper_recursion(remaining, accumulative):
        if not remaining:
            return zip(*accumulative)
        return helper_recursion(remaining[1:], accumulative + [sorted(remaining[0])])

    return helper_recursion(lists, [])