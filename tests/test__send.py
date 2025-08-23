from unittest import TestCase
from unittest.mock import patch

import _send
from _args import ParsedArgs
from _exit_codes import ExitCode
from _message_level import MessageLevel


class Test(TestCase):
    @patch("requests.post")
    def test_send_return_success_200(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_parsed_args = ParsedArgs(
            webhook_url="https://test.url",
            message="test message",
            message_level=MessageLevel.INFO,
            file_path=None,
        )
        return_value = _send.send(mock_parsed_args)
        self.assertEqual(return_value, ExitCode.SUCCESS)

    @patch("requests.post")
    def test_send_return_success_204(self, mock_post):
        mock_post.return_value.status_code = 204
        mock_parsed_args = ParsedArgs(
            webhook_url="https://test.url",
            message="test message",
            message_level=MessageLevel.INFO,
            file_path=None,
        )
        return_value = _send.send(mock_parsed_args)
        self.assertEqual(return_value, ExitCode.SUCCESS)
