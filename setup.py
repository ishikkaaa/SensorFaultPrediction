from setuptools import setup, find_packages

def get_requirements():
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()
        requirements = [r for r in requirements if r and not r.startswith("-e")]
    return requirements

setup(
    name="SensorFaultDetection",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements(),  # must not include '-e .'
)
