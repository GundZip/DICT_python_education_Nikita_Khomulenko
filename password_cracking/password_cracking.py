import random
import string
import json
import time

print("Power by Stell")


class Server:
    def __init__(self):
        self.login: str = self.create_login()
        self.password: str = self.create_password()

    def create_login(self) -> str:
        """Generating login"""
        with open("logins.txt", 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()

        self.login = random.choice(lines).strip()
        return self.login

    def create_password(self) -> str:
        """Generating password"""
        password = ""
        length = random.randint(4, 10)
        for _ in range(length):
            password += random.choice(list(string.ascii_letters + string.digits))

        self.password = password
        return self.password

    def send_request(self, request_file: str):
        """Getting requests from clients"""
        time.sleep(0.01)

        request_data = json.loads(request_file)

        data_password = request_data["password"]
        data_login = request_data["login"]

        if data_login != self.login:
            return {"result": "Wrong login!"}
        if len(self.password) > len(data_password) and \
                self.password[:len(data_password)] == data_password and len(data_password) > 0:
            return {"result": "Exception happened during login"}
        if data_password != self.password:
            return {"result": "Wrong password!"}
        if data_login == self.login and data_password == self.password:
            return {"result": "Connection success!"}
        return {"result": "Bad request"}


class PasswordCracking:
    def __init__(self):
        self.login: str = ""
        self.password: str = ""

    def crack_login(self, server: Server) -> None:
        """ login"""

        with open("logins.txt", 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()

        for login in lines:
            request = {"login": login.strip(), "password": self.password}
            request_json = json.dumps(request)
            response = server.send_request(request_json)
            response_data = response["result"]

            if response_data == "Wrong password!":
                self.login = login.strip()
                print(f"Login is {self.login}")
                return

    def crack_password(self, server: Server) -> None:
        """password"""

        symbols = string.ascii_letters + string.digits
        tmp_password = ''
        while True:
            for symbol in symbols:
                self.password = tmp_password + symbol
                request = json.dumps({'login': self.login, 'password': self.password})
                response = server.send_request(request)
                result = response['result']
                if result == 'Wrong login!':
                    raise Exception('Wrong login!')
                elif result == 'Exception happened during login':
                    tmp_password += symbol
                    print('Password:', self.password)
                    break
                elif result == 'Wrong password!':
                    continue
                elif result == 'Connection success!':
                    print('Password:', self.password)
                    return
                elif result == 'Bad request':
                    raise Exception('Bad request')


if __name__ == "__main__":
    server = Server()
    print(f"Login is {server.create_login()}, Password is {server.create_password()}")
    print(f"Start cracking!")
    passwordCracking = PasswordCracking()
    passwordCracking.crack_login(server)
    passwordCracking.crack_password(server)
    print("Have a nice day!")

