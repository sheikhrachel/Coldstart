# Coldstart.py
from logo import present_logo
from validate_responses import validate_create_project
from create_environment import language_validation


# main class to orchestrate scripts in order
def main():
    present_logo()
    validate_create_project()
    language_validation()


if __name__ == "__main__":
    main()
