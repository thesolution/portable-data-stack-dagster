from setuptools import find_packages, setup

setup(
    name="postcard_company_dm",
    packages=find_packages(),
    install_requires=[
        "dagster==1.6.3",
        "dagster-dbt==0.22.3",
        "duckdb==0.9.2",
        "dbt-core==1.7.7",
        "dbt-duckdb==1.7.1",
        "dagster-duckdb==0.22.3"
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)
