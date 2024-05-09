Feature: Use registration2

    @ui
    Scenario: user sign up and login2

        Given sign up to api2
        When login to api2
        Then user is logged in2
