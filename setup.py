from pathlib import Path
import re

from setuptools import find_packages, setup


ROOT = Path(__file__).parent


def read_version() -> str:
    init_py = ROOT / "mart" / "__init__.py"
    content = init_py.read_text(encoding="utf-8")
    match = re.search(r'__version__\s*=\s*"([^"]+)"', content)
    if not match:
        raise RuntimeError("Unable to find __version__ in mart/__init__.py")
    return match.group(1)


def read_requirements() -> list[str]:
    req_file = ROOT / "requirements.txt"
    lines = req_file.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]

setup(
    name="mart",
    version=read_version(),
    description="Custom app template for Frappe v16 and ERPNext v16",
    author="Mart Team",
    author_email="dev@example.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements(),
)
