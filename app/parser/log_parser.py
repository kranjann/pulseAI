from app.models.log_models import FailedTest, PipelineReport

class LogParser:

    def _extract_failed_test(self, lines:list[str]) -> list[FailedTest]:
        failed_tests =[]

        for line in lines:
            if "::" not in line:
                continue

            print(line)

            file_path, remainder = line.split("::", maxsplit=1)
            print(file_path)

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


    def parse(self, raw_logs:str) -> PipelineReport:
        lines = raw_logs.splitlines()

        failed_tests = self._extract_failed_test(lines)

        return PipelineReport(
            failed_tests=failed_tests,
            total_failed=len(failed_tests)
        )
    
   