from setuptools import find_packages, setup

from mart import __version__ as version

with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="mart",
    version=version,
    description="Custom app template for Frappe v16 and ERPNext v16",
    author="Mart Team",
    author_email="dev@example.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
