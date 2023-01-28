pytest -vs -m "sanity" --html=reports/report.html --capture=tee-sys testcases/ --browser chrome
REM pytest -vs -m "sanity or regression" --html=reports/report.html --capture=tee-sys testcases/ --browser chrome
REM pytest -vs -m "sanity and regression" --html=reports/report.html --capture=tee-sys testcases/ --browser chrome
REM pytest -vs -m "regression" --html=reports/report.html --capture=tee-sys testcases/ --browser chrome
pause