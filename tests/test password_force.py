from django.test import RequestFactory, TestCase

from gerenciaAula.views.SignUpView import check_password_request


class TestPasswordForce(TestCase):
    """
    Test creating an author user
    """

    def setUp(self):
        self.factory = RequestFactory()

    def test_password_force(self):
        pass1_to_match = "Abcdef123456#"
        pass2_equal = "Abcdef123456#"
        pass3_not_equal = "aBcdef123456@"
        pass4_short = "Abc123$"
        pass5_missing_upper = "abcdef123456#"
        pass6_missing_number = "abdCefghijk"
        pass7_missing_special = "abCdef123456"

        self.assertTrue(
            check_password_request(pass1_to_match, pass2_equal),
            "Passwords aren't matching.",
        )
        self.assertFalse(
            check_password_request(pass1_to_match, pass3_not_equal),
            "Check pass function is accepting different passwords.",
        )
        self.assertFalse(
            check_password_request(pass4_short, pass4_short),
            "Short password is being accepted.",
        )
        self.assertFalse(
            check_password_request(pass5_missing_upper, pass5_missing_upper),
            "Upper validation failed.",
        )
        self.assertFalse(
            check_password_request(pass6_missing_number, pass6_missing_number),
            "Number validation failed.",
        )
        self.assertFalse(
            check_password_request(pass7_missing_special, pass7_missing_special),
            "Special validation failed.",
        )
