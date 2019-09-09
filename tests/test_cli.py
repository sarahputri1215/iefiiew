"""Tests for our main skele CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from today import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['today', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in str(output))



class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['today', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(str(output.decode("utf-8")).strip() , VERSION)
