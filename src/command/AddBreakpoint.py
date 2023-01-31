class AddBreakpoint:
    """
    This class is used to demonstrate the `Add Breakpoint` command.

    Usage:
    Open the Source++ Command Palette with `Ctrl+Shift+S` and search for `Add Breakpoint`.

    Command source code:
    https://github.com/sourceplusplus/jetbrains-commander/blob/master/resources/.spp/plugins/add-breakpoint/plugin.kts
    """

    @staticmethod
    def simple_breakpoint():
        """
        Execute the "Add Breakpoint" command with your cursor on line 30 to set up a non-breaking breakpoint
        before the execution of that line. This will open the breakpoint configuration inlay. Hit enter to
        make the breakpoint non-conditional. Hit enter again to make the breakpoint single-use and create
        the breakpoint.

        Once the breakpoint is created, the breakpoint status inlay will appear. This inlay will show the
        current status of the breakpoint and will be marked as "Complete" once the breakpoint is hit. Once
        the breakpoint is hit, the breakpoint status inlay can be expanded to show a table of the breakpoint
        hits. Clicking on a breakpoint hit will open the breakpoint hit data in the traditional debugger
        variables view.
        """

        import random
        random_number = round(random.random() * 100)
        is_even = random_number % 2 == 0
        print(f"{random_number} and is " + ("even" if is_even else "odd"))

    @staticmethod
    def breakpoint_with_redacted_data():
        """
         The "Add Breakpoint" command support PII (Personally Identifiable Information) redaction.
         This allows you to safely add breakpoints to code with sensitive data.

         Try adding a breakpoint to output any of the variables below.
        """

        password = "password123"  # redacted via variable identifier
        ssn = "123-45-6789"  # redacted via regex pattern
        print(f"password: {password}, ssn: {ssn}")
