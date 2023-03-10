# rpi_health

Last update: 2023/03/10 00:29
<br><br>

## Development notes for rpi_health

1. Created the Repo, core files and "sprint 1" board.
2. Made the directories to match the format of my "Using click" documentation.
    - Set up the setup.py too.
        - Based on https://click.palletsprojects.com/en/7.x/setuptools/.
3. Checking that it works with ` pip install -e . `.
    - I can run it with:
        - ` pip install -e . `
        - ` from rpi_health import rpi_health ` - from package import module
        - ` rpi_health.run ` will call the run() function.
4. Looking where to get the live health from.
    - ` armbianmonitor ` - Only works on Armbian, not useful for linus
    - sys/devices/virtual/thermal/thermal_zone0/temp
        - Could be useful. Definitely there on Armbian
        - Not there in Ubuntu
            - ` sudo apt-get install sensors-applet `
            - ` sudo sensors-detect `
                - "Sorry, no sensors were detected. This is relatively common on laptops, where thermal management is hangled by ACPI rather than the OS".
    - Rely on the first option
5. Adding the function to read the value and convert it
    - Value has to be divided by 1000. E.g. the value in the file is 52616, which is 52.6 degrees.
6. Finding the location of all values:
    - CPU temp: sys/devices/virtual/thermal/thermal_zone0/temp
    - Uptime: ` uptime -s `
    - https://pypi.org/project/psutil/
        - Looks like that answers everything for me!
7. Writing a function to grab the values from psutil.
8. Changing it to update a JSON file instead
    - Added a records.json file
    - Made an updateJSON() function to update the file.
    - Changed to json.dumps (instead of json.dump) so that it converts bools properly
9. Adding a check to make sure the size will never be too large.
    - 500 entries in records.json is 157KB, so not much of a concern.
    - 1,000 is 314KB
10. Converted datetime and uptime into arrays.
11. Need to look into auto-running scripts. Maybe with "cron"
    - https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/#:~:text=Cron%20allows%20Linux%20and%20Unix,%2Ftmp%2F%20directories%20and%20more.
    - ` crontab -e `
        - Installed by default on Linux, but no scheduled events set up.
    - @hourly /path/to/ntpdate
        - To run it every hour
        - @daily
12. Adding tox testing.
    - ` python3 -m venv venv `
    - ` . venv/bin/activate `
    - ` pip install tox `
    - ` tox --help `
    - ` tox -q `
        - Quickstart that added a ".tox" file.
    - Created a *tox.ini* file and pasted some contents into it.
    - Added linting to it.
13. Adding a GitHub action to run a pipeline.
14. Finishing touches. Sprint 1 complete!
