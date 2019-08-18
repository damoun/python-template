#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import unittest.mock

from click.testing import CliRunner

from python_template import cli


class CommandLineTest(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_help(self):
        """Test the CLI."""
        result = self.runner.invoke(cli.main, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn(
            '--help  Show this message and exit.', result.output
        )

    def test_default_run(self):
        result = self.runner.invoke(cli.main)
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Hello World', result.output)
