def getPageFinal(a,l):
    if a%l == 0: return a/l - 1
    else: return a/l

def pageSplit(list,limit,now):

    new_list = []
    new_list = list[limit*now:limit*(now+1)]
    # page dealt

    final = getPageFinal(len(list),limit)

    class page:pass
    page.list = []

    if now < 4: # pre 3 not change show style
        if final < 5:
            for i in range(final + 1):
                page.list.append(str(i))
        else:
            for i in range(5):
                page.list.append(str(i))
            if final > 4:
                page.list.append('...')
    else: # show pre 2 and next 2(if has)
        page.list.append('...')
        for i in now-2, now-1:
            page.list.append(str(i))
        page.list.append(str(now))
        if (final - now) <= 2:
            print range(final - now)
            for i in range(final - now):
                page.list.append(str(now+i+1))
            if final> 4:
                page.list.append('...')

    page.now = str(now)
    page.pre = str(now-1)
    page.next = str(now+1)
    page.final = str(final)

    return new_list,page
