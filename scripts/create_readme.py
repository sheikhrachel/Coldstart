# create_readme.py


# Create baseline README.md with template sections
def create_readme(project_name: str):
    f = open('README.md', 'w+')
    f.write('# ' + project_name)
    f.write('\n\n')
    f.write('## Features')
    f.write('\n\n')
    f.write('## Prerequisites')
    f.write('\n\n')
    f.write('## Usage')
    f.write('\n\n')
    f.close()
