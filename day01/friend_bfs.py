fr_info = {

    'Summer': ['John', 'Justin', 'Mike'],   # John, Justin, Mike

    'John':   ['Summer', 'Justin'],           # Summer, Justin

    'Justin': ['John', 'Summer', 'Mike', 'May'],  # John, Summer, Mike, May

    'Mike':   ['Summer', 'Justin'],           # Summer, Justin

    'May':    ['Justin', 'Kim'],           # Justin, Kim

    'Kim':    ['May'],                   # May

    'Tom':    ['Jerry'],                   # Jerry

    'Jerry':  ['Tom'],                   # Tom

}

print("=== Summer의 모든 친구 ===")

print_all_friends(fr_info, 'Summer')

print()

print("=== Jerry의 모든 친구 ===")

print_all_friends(fr_info, ______)
