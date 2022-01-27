def cal():
    make_q = float(input("만드는 양\n"))
    make_time = int(input("만드는 시간\n"))
    make_value = int(input("만드는데 들어가는 재료\n"))
    need_make = float(input("만들어야하는 양\n"))
    b = float(input("건물 생산속도\n0.5, 1, 1.5중에서 선택\n"))
    p = int(input("가속제 설정\n1: 결과물 + 25%  2: 2배속\n"))
    prolif_extra, prolif_speed = 1, 1
    if p == 1:
        prolif_extra = 1.25
    else:
        prolif_speed = 2

    need_build = need_make / (make_q * prolif_extra / make_time * b * prolif_speed)
    need_value = need_build * (make_value / make_time * b * prolif_speed)
    print("만드는 양 초당: ", need_make, "개\n")
    print("만드는데 필요한 건물: ", need_build, "개\n")
    print("만드는데 필요한 재료의 양: ", need_value, "개\n")

