from pathlib import Path

from app.loaders.log_loader import LogLoader
from app.parser.log_parser import LogParser

def main():
    loader = LogLoader()
    parser = LogParser()

    raw_log = loader.load(Path("sample_data/pipeline.log"))

    report = parser.parse(raw_log)

    print(report.model_dump())

if __name__ == "__main__":
    main()