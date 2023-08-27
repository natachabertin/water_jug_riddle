import pytest

from core.board import Juggler

big_num_cases = [
    [50, 30000000, 700],
    [50, 300000000000, 700],
    [50, 3000000000000000000000000, 700],
    [159, 452, 5],
]
big_num_exp = [
    (28, [(50, 0),  (0, 50),  (50, 50),  (0, 100),  (50, 100),  (0, 150),  (50, 150),  (0, 200),  (50, 200),  (0, 250),  (50, 250),  (0, 300),  (50, 300),  (0, 350),  (50, 350),
  (0, 400),  (50, 400),  (0, 450),  (50, 450),  (0, 500),  (50, 500),  (0, 550), (50, 550),  (0, 600),  (50, 600),  (0, 650),  (50, 650),
  (0, 700)]),
(28,
 [(50, 0),
  (0, 50),
  (50, 50),
  (0, 100),
  (50, 100),
  (0, 150),
  (50, 150),
  (0, 200),
  (50, 200),
  (0, 250),
  (50, 250),
  (0, 300),
  (50, 300),
  (0, 350),
  (50, 350),
  (0, 400),
  (50, 400),
  (0, 450),
  (50, 450),
  (0, 500),
  (50, 500),
  (0, 550),
  (50, 550),
  (0, 600),
  (50, 600),
  (0, 650),
  (50, 650),
  (0, 700)]),
    (28,
 [(50, 0),
  (0, 50),
  (50, 50),
  (0, 100),
  (50, 100),
  (0, 150),
  (50, 150),
  (0, 200),
  (50, 200),
  (0, 250),
  (50, 250),
  (0, 300),
  (50, 300),
  (0, 350),
  (50, 350),
  (0, 400),
  (50, 400),
  (0, 450),
  (50, 450),
  (0, 500),
  (50, 500),
  (0, 550),
  (50, 550),
  (0, 600),
  (50, 600),
  (0, 650),
  (50, 650),
  (0, 700)]),
    (244,
 [(159, 0),
  (0, 159),
  (159, 159),
  (0, 318),
  (159, 318),
  (25, 452),
  (25, 0),
  (0, 25),
  (159, 25),
  (0, 184),
  (159, 184),
  (0, 343),
  (159, 343),
  (50, 452),
  (50, 0),
  (0, 50),
  (159, 50),
  (0, 209),
  (159, 209),
  (0, 368),
  (159, 368),
  (75, 452),
  (75, 0),
  (0, 75),
  (159, 75),
  (0, 234),
  (159, 234),
  (0, 393),
  (159, 393),
  (100, 452),
  (100, 0),
  (0, 100),
  (159, 100),
  (0, 259),
  (159, 259),
  (0, 418),
  (159, 418),
  (125, 452),
  (125, 0),
  (0, 125),
  (159, 125),
  (0, 284),
  (159, 284),
  (0, 443),
  (159, 443),
  (150, 452),
  (150, 0),
  (0, 150),
  (159, 150),
  (0, 309),
  (159, 309),
  (16, 452),
  (16, 0),
  (0, 16),
  (159, 16),
  (0, 175),
  (159, 175),
  (0, 334),
  (159, 334),
  (41, 452),
  (41, 0),
  (0, 41),
  (159, 41),
  (0, 200),
  (159, 200),
  (0, 359),
  (159, 359),
  (66, 452),
  (66, 0),
  (0, 66),
  (159, 66),
  (0, 225),
  (159, 225),
  (0, 384),
  (159, 384),
  (91, 452),
  (91, 0),
  (0, 91),
  (159, 91),
  (0, 250),
  (159, 250),
  (0, 409),
  (159, 409),
  (116, 452),
  (116, 0),
  (0, 116),
  (159, 116),
  (0, 275),
  (159, 275),
  (0, 434),
  (159, 434),
  (141, 452),
  (141, 0),
  (0, 141),
  (159, 141),
  (0, 300),
  (159, 300),
  (7, 452),
  (7, 0),
  (0, 7),
  (159, 7),
  (0, 166),
  (159, 166),
  (0, 325),
  (159, 325),
  (32, 452),
  (32, 0),
  (0, 32),
  (159, 32),
  (0, 191),
  (159, 191),
  (0, 350),
  (159, 350),
  (57, 452),
  (57, 0),
  (0, 57),
  (159, 57),
  (0, 216),
  (159, 216),
  (0, 375),
  (159, 375),
  (82, 452),
  (82, 0),
  (0, 82),
  (159, 82),
  (0, 241),
  (159, 241),
  (0, 400),
  (159, 400),
  (107, 452),
  (107, 0),
  (0, 107),
  (159, 107),
  (0, 266),
  (159, 266),
  (0, 425),
  (159, 425),
  (132, 452),
  (132, 0),
  (0, 132),
  (159, 132),
  (0, 291),
  (159, 291),
  (0, 450),
  (159, 450),
  (157, 452),
  (157, 0),
  (0, 157),
  (159, 157),
  (0, 316),
  (159, 316),
  (23, 452),
  (23, 0),
  (0, 23),
  (159, 23),
  (0, 182),
  (159, 182),
  (0, 341),
  (159, 341),
  (48, 452),
  (48, 0),
  (0, 48),
  (159, 48),
  (0, 207),
  (159, 207),
  (0, 366),
  (159, 366),
  (73, 452),
  (73, 0),
  (0, 73),
  (159, 73),
  (0, 232),
  (159, 232),
  (0, 391),
  (159, 391),
  (98, 452),
  (98, 0),
  (0, 98),
  (159, 98),
  (0, 257),
  (159, 257),
  (0, 416),
  (159, 416),
  (123, 452),
  (123, 0),
  (0, 123),
  (159, 123),
  (0, 282),
  (159, 282),
  (0, 441),
  (159, 441),
  (148, 452),
  (148, 0),
  (0, 148),
  (159, 148),
  (0, 307),
  (159, 307),
  (14, 452),
  (14, 0),
  (0, 14),
  (159, 14),
  (0, 173),
  (159, 173),
  (0, 332),
  (159, 332),
  (39, 452),
  (39, 0),
  (0, 39),
  (159, 39),
  (0, 198),
  (159, 198),
  (0, 357),
  (159, 357),
  (64, 452),
  (64, 0),
  (0, 64),
  (159, 64),
  (0, 223),
  (159, 223),
  (0, 382),
  (159, 382),
  (89, 452),
  (89, 0),
  (0, 89),
  (159, 89),
  (0, 248),
  (159, 248),
  (0, 407),
  (159, 407),
  (114, 452),
  (114, 0),
  (0, 114),
  (159, 114),
  (0, 273),
  (159, 273),
  (0, 432),
  (159, 432),
  (139, 452),
  (139, 0),
  (0, 139),
  (159, 139),
  (0, 298),
  (159, 298),
  (5, 452)])
]

class TestBigCases:
    @pytest.mark.parametrize(
        "case, expected",
        [
            pytest.param(
                big_num_cases[0],
                big_num_exp[0],
            ),
            pytest.param(
                big_num_cases[1],
                big_num_exp[1],
            ),
            pytest.param(
                big_num_cases[2],
                big_num_exp[2],
            ),
            pytest.param(
                big_num_cases[3],
                big_num_exp[3],
            ),
        ],
    )
    def test_solvable_big_nums(self, case, expected):
        res = Juggler(*case).solve()

        assert res == expected
