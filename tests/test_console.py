#!/usr/bin/python3

import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
import sys
import os


class CreateTests(unittest.TestCase):
    '''Create Tests'''

    def test_no_input(self):
        '''test when only create is parsed on the console'''
        output = '** class name missing **'
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('create')
            mock_print.assert_called_once_with(output)

    def test_invalid_class(self):
        '''parse invalid command'''
        output = '** class doesn\'t exist **'
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('create city')
            mock_print.assert_called_once_with(output)

    def test_valid_input(self):
        '''test when valid inputs are parsed to the console
        we'll use type of output to test
        '''
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('create User')
            output = mock_print.call_args[0][0]
            self.assertIsInstance(output, str)
            key = "User.{}".format(output)
            self.assertIn(key, storage.all().keys())


class AllTests(unittest.TestCase):
    """Test cass for all command"""

    def test_invalid_class(self):
        '''parse invalid command'''
        output = '** class doesn\'t exist **'

        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('all user')
            mock_print.assert_called_once_with(output)

        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('user.all()')
            mock_print.assert_called_once_with(output)

    def test_valid_input(self):
        '''test when valid inputs are parsed to the console
        we'll use type of output to test'''
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('all User')
            output = mock_print.call_args[0][0]
            self.assertIsInstance(output, list)


class ShowTests(unittest.TestCase):
    '''test case for show command'''

    def test_invalid_class(self):
        '''parse invalid command'''
        output = '** class doesn\'t exist **'
        with patch('builtins.print') as mock_print:
            with patch('builtins.print') as mock:
                HBNBCommand().onecmd('create City')
                id = mock.call_args[0][0]
            HBNBCommand().onecmd('show city ' + id)
            mock_print.assert_called_once_with(output)

        with patch('builtins.print') as mock_print:
            with patch('builtins.print') as mock:
                HBNBCommand().onecmd('create City')
                id = mock.call_args[0][0]
            key = 'city.show({})'.format(id)
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    def test_invalid_id(self):
        "test when invalid id is parsed"
        output = '** no instance found **'
        with patch('builtins.print') as mock_print:
            id = '1234-567-8910'
            HBNBCommand().onecmd('show City ' + id)
            mock_print.assert_called_once_with(output)

        with patch('builtins.print') as mock_print:
            key = 'City.show({})'.format(id)
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    def test_missing_id(self):
        """id missing"""
        output = '** instance id missing **'
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd(' show City')
            mock_print.assert_called_once_with(output)
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('City.show()')
            mock_print.assert_called_once_with(output)


class DestroyTests(unittest.TestCase):
    """destroy tests"""

    def test_invalid_class(self):
        '''parse invalid command'''
        output = '** class doesn\'t exist **'
        with patch('builtins.print') as mock_print:
            with patch('builtins.print') as mock:
                HBNBCommand().onecmd('create City')
                id = mock.call_args[0][0]
            HBNBCommand().onecmd('destroy city ' + id)
            mock_print.assert_called_once_with(output)

        with patch('builtins.print') as mock_print:
            with patch('builtins.print') as mock:
                HBNBCommand().onecmd('create City')
                id = mock.call_args[0][0]
            key = 'city.destroy({})'.format(id)
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    def test_invalid_id(self):
        "test when invalid id is parsed"
        output = '** no instance found **'
        with patch('builtins.print') as mock_print:
            id = '1234-567-8910'
            HBNBCommand().onecmd('destroy City ' + id)
            mock_print.assert_called_once_with(output)

        with patch('builtins.print') as mock_print:
            key = 'City.destroy({})'.format(id)
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    def test_missing_id(self):
        """id missing"""
        output = '** instance id missing **'
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd(' destroy City')
            mock_print.assert_called_once_with(output)
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd('City.destroy()')
            mock_print.assert_called_once_with(output)


class UpdateTests(unittest.TestCase):
    '''Update test cases'''

    def test_invalid_class(self):
        '''parse invalid command'''
        output = '** class doesn\'t exist **'
        with patch('builtins.print') as mock_print:
            with patch('builtins.print') as mock:
                HBNBCommand().onecmd('create City')
                id = mock.call_args[0][0]
            HBNBCommand().onecmd('destroy city ' + id)
            mock_print.assert_called_once_with(output)

        with patch('builtins.print') as mock_print:
            with patch('builtins.print') as mock:
                HBNBCommand().onecmd('create City')
                id = mock.call_args[0][0]
            key = 'city.destroy({})'.format(id)
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    def test_invalid_id(self):
        "test when invalid id is parsed"
        output = '** no instance found **'
        key = 'update City {} Name \"John Doe\"'.format('654646')
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)
        with patch('builtins.print') as mock_print:
            key = 'City.update({}, {}, {})'.format(
                '654', 'Name', '\"John Doe\"')
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    # def test_missing_id(self):
    #     """id missing"""
    #     output = '** attribute name missing **'
    #     with patch('builtins.print') as mock_print:
    #         key = 'update City'
    #         HBNBCommand().onecmd(key)
    #         mock_print.assert_called_once_with(output)
    #     with patch('builtins.print') as mock_print:
    #         param = 'City.update({})'.format(key)
    #         HBNBCommand().onecmd(param)
    #         mock_print.assert_called_once_with(output)

    def test_missing_attr_name(self):
        "test when attr name is missing"
        output = '** no instance found **'
        key = 'update City {} Name \"John Doe\"'.format('654646')
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)
        with patch('builtins.print') as mock_print:
            key = 'City.update({}, {}, {})'.format(
                '654', 'Name', '\"John Doe\"')
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)

    def test_missing_attr_value(self):
        "test when invalid id is parsed"
        output = '** no instance found **'
        key = 'update City {} Name \"John Doe\"'.format('654646')
        with patch('builtins.print') as mock_print:
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)
        with patch('builtins.print') as mock_print:
            key = 'City.update({}, {}, {})'.format(
                '654', 'Name', '\"John Doe\"')
            HBNBCommand().onecmd(key)
            mock_print.assert_called_once_with(output)


class QuitTest(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            print('sd')
            print(HBNBCommand().onecmd("quit"))
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
