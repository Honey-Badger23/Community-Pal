from setuptools import setup, find_packages

setup(
    name="community_registration",  # Name of the app (same as in pyproject.toml)
    version="0.0.1",  # You can replace this with a dynamic version mechanism if desired
    description="Entities and their roles in the community",  # From pyproject.toml
    author="Michael",  # From pyproject.toml
    author_email="michaeldavis2990@gmail.com",  # From pyproject.toml
    packages=find_packages(),  # Automatically discovers all the Python packages in the app
    include_package_data=True,  # Ensures that non-Python files like static assets are included
    zip_safe=False,  # Makes sure the app is not zipped (common for Frappe apps)
    install_requires=[  # List of Python dependencies
        "frappe",  # Frappe dependency, you may want to pin a version if necessary
    ],
    classifiers=[  # Add relevant classifiers for PyPi
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",  # Adjust if your license is different
    ],
    python_requires=">=3.10",  # Ensures your app runs on Python 3.10 or newer
)
