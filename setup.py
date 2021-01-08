from distutils.core import setup


setup(
    name="spaceship",
    version="0.0.0",
    description="Cosmic web-ecosystem",
    entry_points="""
    [console_scripts]
    spaceship=spaceship.control_center.dispatcher:control
    """
)
