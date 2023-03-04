# rpi_health

Last update: 2023/03/04 21:24
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
