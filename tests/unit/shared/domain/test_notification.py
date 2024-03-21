# sourcery skip: no-loop-in-tests
import pytest

from src.shared.domain.notification import Notification


class TestNotification:
    def test_notification_happy_path(self):
        test_cases = [
            ([], "", False),  # No errors
            (["Error 1"], "Error 1", True),  # single error
            (["Error 1", "Error 2"], "Error 1,Error 2", True),  # multiple errors
        ]

        for errors, expected_messages, expected_has_errors in test_cases:
            notification = Notification()
            for error in errors:
                notification.add_error(error)
            err_messages = notification.messages
            has_errors = notification.has_errors

            assert err_messages == expected_messages
            assert has_errors == expected_has_errors

    def test_notification_edge_cases(self):
        test_cases = [
            ([""], ""),  # empty string error
            ([" "], " "),  # whitespace string error
            ([None], ""),  # none as error should be ignored
        ]
        for errors, expected_str in test_cases:
            notification = Notification()
            for error in errors:
                notification.add_error(error)
            actual_str = str(notification)
            assert actual_str == expected_str
