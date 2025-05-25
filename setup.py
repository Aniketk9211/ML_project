from setuptools import find_packages,setup

from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            for line in file_obj:
                line = line.strip()
                if line and not line.startswith('#'):  # Ignore empty lines and comments
                    requirements.append(line)
        # Remove duplicates and handle '-e .' if present
        requirements = list(set(requirements))
        if '-e .' in requirements:
            requirements.remove('-e .')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Aniket',
    author_email='aniketkj9211@gmail.com',
    packages=find_packages(),  # No need for 'where' or 'package_dir'
    install_requires=get_requirements('requirements.txt')
)

# setup(
#     name='mlproject',
#     version='0.0.1',
#     author='Aniket',
#     author_email='aniketkj9211@gmail.com',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )
# setup(
#     name='mlproject',
#     version='0.0.1',
#     author='Aniket',
#     author_email='aniketkj9211@gmail.com',
#     packages=find_packages(where='src'),
#     package_dir={'': 'src'},
#     install_requires=get_requirements('requirements.txt')
# )