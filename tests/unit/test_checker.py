from unittest.mock import patch

import pytest

from core.board import Juggler
from core.checker import Checker
from core.checker import HISTORIC_RESULTS
from core.utils.models import NokResult
from core.utils.models import OkResult


class TestSolvedBefore:
    """Request DB is empty before 1st query
    1st query case is returned and added to DB
    2nd query -same case- is returned from DB and no added again"""

    def test_solved_before(self):
        case = [5, 4, 3]

        num_of_solved_cases = len(HISTORIC_RESULTS.keys())

        res = Checker(*case, Juggler).report()

        assert (5, 4, 3) in HISTORIC_RESULTS.keys()
        assert len(HISTORIC_RESULTS.keys()) == num_of_solved_cases + 1
        assert isinstance(res, OkResult)
        assert (
            str(res)
            == "OK in the following 4 moves: [(0, 4), (4, 0), (4, 4), (5, 3)]"
        )

        res = Checker(*case, Juggler).report()

        assert (5, 4, 3) in HISTORIC_RESULTS.keys()
        assert len(HISTORIC_RESULTS.keys()) == num_of_solved_cases + 1
        assert isinstance(res, OkResult)
        assert (
            str(res)
            == "OK in the following 4 moves: [(0, 4), (4, 0), (4, 4), (5, 3)]"
        )

    def test_solved_before_dont_call_solver_again(self):
        num_of_solved_cases = len(HISTORIC_RESULTS.keys())

        with patch("core.checker.Juggler") as solver:
            case = [5, 3, 10]
            res = Checker(*case, Juggler).report()

            solver.call_count == 1
            assert len(HISTORIC_RESULTS.keys()) == num_of_solved_cases + 1

            res = Checker(*case, Juggler).report()

            assert len(HISTORIC_RESULTS.keys()) == num_of_solved_cases + 1
            solver.call_count == 0

        res = Checker(*case, Juggler).report()


class TestChecker:
    def test_solvable_returns_object_result(self):
        case = [5, 4, 3]
        res = Checker(*case, Juggler).report()

        assert isinstance(res, OkResult)
        assert (
            str(res)
            == "OK in the following 4 moves: [(0, 4), (4, 0), (4, 4), (5, 3)]"
        )

    def test_solvable_new_case_calls_solver(self):
        with patch("core.checker.Juggler") as solver:
            case = [5, 4, 3]
            res = Checker(*case, Juggler).report()

        solver.call_count == 1

    @pytest.mark.parametrize(
        "case, expected",
        [
            pytest.param(
                [1, 2, 3],
                "No solution: Goal is the sum of both jars, only can be measured separately",
                id="goal eq sum of jars",
            ),
            pytest.param(
                [6, 4, 3],
                "No solution: Goal is not divisible by the GCD of both jars.",
                id="even both jars and goal odd",
            ),
            pytest.param(
                [5, 3, 7],
                "No solution: Goal is bigger than bigger jar. No space to hold 7 gallons.",
                id="even both odd and goal even",
            ),
            pytest.param(
                [0, 0, 0],
                "No solution: Goal is zero or both jars are.",
                id="all 0 >> you need a goal, not steps",
            ),
            pytest.param(
                [10, 1, 0],
                "No solution: Goal is zero or both jars are.",
                id="goal 0, jugs not",
            ),
            pytest.param(
                [0, 0, 1],
                "No solution: Goal is zero or both jars are.",
                id="jugs 0, goal not",
            ),
        ],
    )
    def test_unsolvable(self, case, expected):
        res = Checker(*case, Juggler).report()

        assert isinstance(res, NokResult)
        assert str(res) == expected
