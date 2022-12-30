from typing import Literal
import datetime
import os.path


class Console:

    def __init__(self, name: str, auto_create: bool = True):
        self.name = name
        self.log_files = [f"{self.name.upper()}_session.txt", f"{self.name.upper()}_always.txt"]

        if auto_create is True:
            self.create_console()

    def create_console(self) -> None:
        file_names = [f"{self.name.upper()}_session", f"{self.name.upper()}_always"]

        for file in file_names:
            if not os.path.exists(f"./{file}.txt"):
                current_file = open(f"./{file}.txt", "w")
                current_file.write(f"Python console implementation by PhotonSoftware & GabHas\n")
                current_file.write(f"[v] Console \"{self.name}\" initialized successfully.\n")
                current_file.close()

    def log(self, content: str) -> None:
        # Preventing type error
        if not isinstance(content, str):
            raise ValueError(f"Error: Expected type \"str\" but got \"{type(content)}\"")

        # Writing in the file
        current_time = datetime.datetime.now().strftime('%b %d %Y %H:%M:%S')

        for file in self.log_files:
            with open(file, "a") as cur_file:
                cur_file.write(f"[{current_time}] {content}\n")

    def get_log(self, cache: Literal["session", "always", "both"], number_of_line: int | Literal["all"]) -> list:

        if cache == "both":
            file_list = ["session", "always"]
        else:
            file_list = [cache]

        file_content = []

        for item in file_list:
            with open(f"./{self.name.upper()}_{item}.txt", "r") as file:
                content = file.readlines()

                if number_of_line == "all":
                    file_content.append(content)
                elif len(content) >= number_of_line:
                    file_content.append(content[-number_of_line:])
                else:
                    file_content.append(content)

        return file_content

    def clear_log(self, cache: Literal["session", "always", "both"]) -> None:

        def empty_file(file_name: str) -> None:
            with open(file_name, "w"):
                pass

        match cache:
            case "both":
                for file in self.log_files:
                    empty_file(file)
            case "session":
                empty_file(self.log_files[0])
            case "always":
                empty_file(self.log_files[1])
            case _:
                pass

        self.log(f"Log cleared with argument : \"{cache}\"")
