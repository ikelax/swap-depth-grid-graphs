from src.grid_graph import grid_graph


class TestGridGraph:
    def test_empty(self):
        assert grid_graph(0) == [[]]

    def test_one(self):
        assert grid_graph(1) == [[(0, 0)]]

    def test_two(self):
        assert grid_graph(2) == [[(0, 1), (1, 1)], [(0, 0), (1, 0)]]

    def test_three(self):
        assert grid_graph(3) == [
            [(0, 2), (1, 2), (2, 2)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 0), (1, 0), (2, 0)],
        ]
