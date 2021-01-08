from setuptools import find_packages, setup


setup(
    name="spaceship",
    version="0.0.0",
    description="Cosmic web-ecosystem",
    install_requires=["wheel", "setuptools"],
    packages=find_packages(),
    entry_points="""
    [console_scripts]
    spaceship=spaceship.control_center.dispatcher:control
    """
)
