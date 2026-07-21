from pathlib import Path

from app.loaders.log_loader import LogLoader


def main():
    loader = LogLoader()

    log_text = loader.load(Path("sample_data/pipeline.log"))

    print(log_text[:500])


if __name__ == "__main__":
    main()