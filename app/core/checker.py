from math import gcd

from core.board import Juggler
from core.utils.exceptions import UnsolvableException
from core.utils.models import NokResult
from core.utils.models import OkResult


HISTORIC_RESULTS = dict()


class Checker:
    """Interacts between core and with API/CLI as the orchestration logic.
    Receives params as integers; and the "solver" class
    (uncoupling the algorithm from the orchestration logic).

    Checks if those params were historically solved
    (if so, returns from db instead of calculating
    -historic data includes unsolvable puzzles).

    If not solved yet, calls the selected algorithm to solve it.

    Returns results object, modeled depending on solvable.
    """

    def __init__(self, jar_x, jar_y, goal, solver):
        self.params = (
            jar_x,
            jar_y,
            goal,
        )
        self._solution = None
        self.result = None
        self._process(solver)

    def _process(self, solver):
        self.result = self._was_solved()
        if self.result:
            self.report()
        if self._is_solvable():
            self._solution = solver(*self.params).solve()
            self._process_solvable()

    def _is_solvable(self):
        try:
            return self._solvable_checks()
        except UnsolvableException as e:
            self._process_unsolvable(e)

    def _was_solved(self):
        """Historic results IRL should be a DB, in here is:
        dict((x,y,z): Result)
        """
        return HISTORIC_RESULTS.get(self.params)

    def report(self):
        return self.result

    def _solvable_checks(self):
        jar_x, jar_y, goal = self.params
        if goal == 0 or (jar_y == 0 and jar_x == 0):
            raise UnsolvableException("Goal is zero or both jars are.")
        if self._is_not_goal_div_by_jars_gcd(jar_x, jar_y, goal):
            raise UnsolvableException("Goal is not divisible by the GCD of both jars.")
        if self._is_goal_sum_of_both_jars(jar_x, jar_y, goal):
            raise UnsolvableException(
                "Goal is the sum of both jars, only can be measured separately"
            )
        if self._is_goal_gt_bigger_jar(jar_x, jar_y, goal):
            raise UnsolvableException(
                f"Goal is bigger than bigger jar. No space to hold {goal} gallons."
            )
        return True

    def _process_unsolvable(self, error):
        self.result = NokResult(error)
        self._store_result(self.result)

    def _process_solvable(self):
        self.result = OkResult(*self._solution)
        self._store_result(self.result)

    def _store_result(self, result):
        HISTORIC_RESULTS.update({self.params: result})

    @staticmethod
    def _is_not_goal_div_by_jars_gcd(jar_x, jar_y, goal):
        """Only is solvable if goal can be divided by
        the GCD of both jars capacity."""
        return goal % gcd(jar_x, jar_y) != 0

    @staticmethod
    def _is_goal_sum_of_both_jars(jar_x, jar_y, goal):
        return jar_x + jar_y == goal

    @staticmethod
    def _is_goal_gt_bigger_jar(jar_x, jar_y, goal):
        return goal > max(jar_x, jar_y)
