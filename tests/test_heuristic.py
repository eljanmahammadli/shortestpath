from shortestpath.main import State, heuristic

def test_heuristic_1():
    state = State([0, 3, 0])
    target = 1
    h = heuristic(state=state, target_volume=target)
    assert h == 1.5

def test_heuristic_2():
    state = State([0, 0, 0])
    target = 143
    h = heuristic(state=state, target_volume=target)
    assert h == 143.0

def test_heuristic_3():
    state = State([72, 0, 0, 0, 72, 0])
    target = 143
    h = heuristic(state=state, target_volume=target)
    assert h == 36.0