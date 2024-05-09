Feature: Use registration

    Scenario: user sign up and login

        Given sign up to api
        When login to api
        Then user is logged in