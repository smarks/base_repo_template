"""Smoke tests: the project is wired up and Django's system checks pass."""

from django.core.management import call_command


def test_django_system_check_passes() -> None:
    # Raises SystemCheckError if anything in the project is misconfigured.
    call_command("check")
