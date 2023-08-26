from math import gcd

from core.board import Juggler
from core.models.communicator import NokResult
from core.models.communicator import OkResult
from core.utils.exceptions import UnsolvableException

HISTORIC_RESULTS = dict()


class Checker:
    def __init__(self, jar_x, jar_y, goal):
        self.params = (
            jar_x,
            jar_y,
            goal,
        )
        self._solution = None
        self.result = None
        self._process()

    def _process(self):
        self.result = self._was_solved()
        if self.result:
            self.report()
        if self._is_solvable():
            self._solution = Juggler(*self.params).solve()
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
                f"Goal is bigger than the bigger jar. No space to hold {goal} gallons."
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

    def _is_not_goal_div_by_jars_gcd(self, jar_x, jar_y, goal):
        """Only is solvable if goal can be divided by the GCD of both jars capacity."""
        return goal % gcd(jar_x, jar_y) != 0

    def _is_goal_sum_of_both_jars(self, jar_x, jar_y, goal):
        return jar_x + jar_y == goal

    def _is_goal_gt_bigger_jar(self, jar_x, jar_y, goal):
        return goal > max(jar_x, jar_y)
