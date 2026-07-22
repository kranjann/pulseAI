from app.models.log_models import FailedTest, PipelineReport

class LogParser:

    def _extract_failed_tests(self, lines:list[str]) -> list[FailedTest]:
        failed_tests =[]

        for line in lines:
            if "::" not in line:
                continue

            file_path, remainder = line.split("::", maxsplit=1)

            if "FAILED" not in remainder:
                continue

            test_name = remainder.split()[0]

            failed_tests.append(
                FailedTest(
                    test_name=test_name,
                    file_path=file_path,
                    line_number=0,
                    assertion_message=""
                )
            )

        return failed_tests

    def _extract_assertions(self, lines: list[str], failed_tests: list[FailedTest]) -> None:
        current_failure: FailedTest | None = None

        for line in lines:
            for failed_test in failed_tests:
                if failed_test.test_name in line:
                    current_failure = failed_test
                    break

            if current_failure is None:
                continue

            if "AssertionError" in line:
                _, extracted_message = line.split("AssertionError:", maxsplit=1)

                
                current_failure.assertion_message = extracted_message.strip()


    def _extract_locations(self, lines, failed_tests):

        current_failure: FailedTest | None = None

        for line in lines:
            for failed_test in failed_tests:
                if failed_test.test_name in line:
                    current_failure = failed_test
                    break
            
            if current_failure is None:
                continue

            if "AssertionError" in line and ".py" in line:
                line_number = line.rsplit(":", maxsplit=2)[1]

                current_failure.line_number = int(line_number)
            


    def parse(self, raw_logs:str) -> PipelineReport:
        lines = raw_logs.splitlines()

        failed_tests = self._extract_failed_tests(lines)
        self._extract_assertions(lines, failed_tests)
        self._extract_locations(lines, failed_tests)

        # return failed_tests
        return PipelineReport(
            failed_tests=failed_tests,
            total_failed=len(failed_tests)
        )
    
   