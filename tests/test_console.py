#!/usr/bin/python3

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import sys
import os


class CreateTests(unittest.TestCase):
    '''Create Tests'''
    pass


class AllTests(unittest.TestCase):
    pass


class ShowTests(unittest.TestCase):
    pass


class DestroyTests(unittest.TestCase):
    pass


class UpdateTests(unittest.TestCase):
    pass


class QuitTest(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
