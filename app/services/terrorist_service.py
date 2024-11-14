from flask import jsonify

from app.repository.terrorist_repository import find_terrorist_by_email


def get_all_terrorist_by_email():
    print(jsonify(find_terrorist_by_email().unwrap()))

if __name__ == '__main__':
    get_all_terrorist_by_email()