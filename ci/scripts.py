import subprocess


MODULE_PATH = "fuzzpyxl"


def test():
    subprocess.run(["pytest", f"--cov={MODULE_PATH}", "tests"])


def test_report():
    subprocess.run(["pytest", f"--cov={MODULE_PATH}", "--cov-report=xml", "tests"])


def lint():
    subprocess.run(["pylint", MODULE_PATH])


def lint_badge():
    from pylint.lint import Run
    import anybadge

    results = Run([MODULE_PATH], do_exit=False)
    score = int(results.linter.stats.global_note)  # MAx of Score is 10
    thresholds = {2: "red", 4: "orange", 6: "yellow", 10: "green"}
    badge = anybadge.Badge("pylint", score, value_suffix="/10", thresholds=thresholds)
    badge.write_badge("pylint.svg")


def typecheck():
    subprocess.run(
        ["mypy", MODULE_PATH],
    )


def typecheck_badge():
    import re
    import anybadge

    nmap_out = subprocess.run(
        ["mypy", MODULE_PATH],
        universal_newlines=True,
        stdout=subprocess.PIPE,
    )

    last_line = nmap_out.stdout.splitlines()[-1]
    if last_line.startswith("Success"):
        badge = anybadge.Badge("mypy", "Succes", default_color="green")
    else:
        matches = re.match(r"Found \d+", last_line)
        num_errors = matches[0][5:]
        error_str = "Errors" if int(num_errors) > 1 else "Error"
        badge = anybadge.Badge("mypy", f"{num_errors} {error_str}", default_color="red")

    badge.write_badge("mypy.svg")
