import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name="random_spanish_words",
	version="0.00.2",
	author="Reydel Romeu Alonso",
	author_email="reydelromeu@gmail.com",
	description="Package for returnning random words in Spanish",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ReydelCode/random_spanish_words",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)