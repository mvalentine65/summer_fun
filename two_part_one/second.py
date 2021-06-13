def solution(xs):
    result = float('-inf')
    max_panel = 1
    min_panel = 1

    for panel in xs:
        if panel > 0:
            max_panel = max_panel * panel
            min_panel = min(1, min_panel * panel)
        elif panel < 0:
            temp = max_panel
            max_panel = min_panel * panel
            min_panel = temp * panel
        result = max(result, max_panel)
        if max_panel < 0:
            max_panel = 1
        if min_panel > 1:
            min_panel = 1
    return str(result)


if __name__ == "__main__":
    x = [-1000] * 49
    print(len(solution(x)))
