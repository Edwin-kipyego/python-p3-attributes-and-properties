#!/usr/bin/env python3
class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name="unknown", job="unknown"):
        # Use the property setters to ensure validation and formatting
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case before saving
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in Person.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)