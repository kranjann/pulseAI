from pathlib import Path


class LogLoader:
    """
    Responsible only for loading log files.
    """

    @staticmethod
    def _detect_encoding(file_path: Path) -> str:
        with file_path.open("rb") as file:
            first_bytes = file.read(4)

        if first_bytes.startswith(b"\xff\xfe"):
            return "utf-16"

        if first_bytes.startswith(b"\xfe\xff"):
            return "utf-16"

        if first_bytes.startswith(b"\xef\xbb\xbf"):
            return "utf-8-sig"

        return "utf-8"

    def load(self, file_path: Path) -> str:
        encoding = self._detect_encoding(file_path)

        with file_path.open("r", encoding=encoding) as file:
            return file.read()