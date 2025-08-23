from unittest import TestCase
from unittest.mock import patch

import notify
from _exit_codes import ExitCode


class Test(TestCase):
    @patch("notify._args.parse_args")
    @patch("notify._send.send")
    @patch("sys.exit")
    def test_send_exit_code_success_passed(self, mock_exit, mock_send, mock_parse_args):
        mock_send.return_value = ExitCode.SUCCESS
        notify.main()
        mock_exit.assert_called_once_with(ExitCode.SUCCESS.value)

    @patch("notify._args.parse_args")
    @patch("notify._send.send")
    @patch("sys.exit")
    def test_send_exit_code_warning_passed(self, mock_exit, mock_send, mock_parse_args):
        mock_send.return_value = ExitCode.WARNING
        notify.main()
        mock_exit.assert_called_once_with(ExitCode.WARNING.value)

    @patch("notify._args.parse_args")
    @patch("notify._send.send")
    @patch("sys.exit")
    def test_send_exit_code_error_passed(self, mock_exit, mock_send, mock_parse_args):
        mock_send.return_value = ExitCode.ERROR
        notify.main()
        mock_exit.assert_called_once_with(ExitCode.ERROR.value)
