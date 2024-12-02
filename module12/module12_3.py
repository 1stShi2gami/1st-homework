import unittest
import runner
import runner_and_tournament

runnST = unittest.TestSuite()

runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner.RunnerTest))
runnST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_and_tournament.TournamentTest))


testy_runner = unittest.TextTestRunner(verbosity=2)
testy_runner.run(runnST)