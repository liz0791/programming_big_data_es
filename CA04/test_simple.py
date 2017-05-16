#Elisandra Silva - 10247211

import unittest

from simple1 import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('change.txt')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self, commits):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self, commits):
        commits = get_commits(self.data)
        self.assertEqual('r1551925', commits[0]['revision'])
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', commits[0]['date']
       
    def test_last_commit(self, commits):
        commits = get_commits(self.data)
        self.assertEqual('r1491146', commits[421]['revision'])
        self.assertEqual('Thomas', commits[421]['author'])
        self.assertEqual('2015-07-13 09:21:48 +0100 (Mon, 13 Jul 2015)', commits[421]['date']
        
    def test_get_info(self, commits):
        commits = get_commits(self.data)
        self.assertEqual(['r1551925', 'Thomas', '2015-11-27', '16:57:44', '1'], csv_file[0])
        
if __name__ == '__main__':
    unittest.main()



 #getting error: NameError: name 'commits' is not defined?????


