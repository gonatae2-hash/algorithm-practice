fr_info = {

    'Summer': ['John', 'Justin', 'Mike'],

    'John':   ['Summer', 'Justin'],

    'Justin': ['John', 'Summer', 'Mike', 'May'],

    'Mike':   ['Summer', 'Justin'],

    'May':    ['Justin', 'Kim'],

    'Kim':    ['May'],

    'Tom':    ['Jerry'],

    'Jerry':  ['Tom'],

}



def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append((start, 0))  # (이름, 친밀도) 튜플로 넣기. 자기 자신은 친밀도 0
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)

        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))  # 친밀도를 1 증가시켜 추가
                done.add(x)


print("=== Summer의 모든 친구와 친밀도 ===")
print_all_friends(fr_info, 'Summer')
