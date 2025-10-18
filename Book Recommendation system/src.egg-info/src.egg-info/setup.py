from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

    REPO_NAME="ML-Projects"
    AUTHOR_USER_NAME="Ishaaque"
    SRC_REPO="src"
    LIST_OF_REQUIREMENTS=['streamlit', 'pandas', 'numpy', 'scikit-learn']
    setup(
        name=REPO_NAME,
        version="0.0.1",
        author=AUTHOR_USER_NAME,
        description="A machine learning project",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        author_email="ishaaque.ahmed@gmail.com",
        packages=[SRC_REPO],
        license="MIT",
        python_requires=">=3.7",
        install_requires=LIST_OF_REQUIREMENTS
    )