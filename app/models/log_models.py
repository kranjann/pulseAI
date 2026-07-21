from pydantic import BaseModel


class FailedTest(BaseModel):
    test_name: str
    file_path: str
    line_number: int
    assertion_message: str


class PipelineReport(BaseModel):
    failed_tests: list[FailedTest]
    total_failed: int