# brightlight-py
usage: brightlight.py [-h]
                      [-v | -p | -r | -w <val> | -i <val> | -d <val> | -wp <val> | -ip <val> | -dp <val> | -m]
                      [-f <dir>]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Print program version and exit.
  -p, --percentage      Read the brightness level as a percentage (0 to 100)
                        instead of the internal scale the kernel uses (such as
                        e.g. 0 to 7812).
  -r, --read            Read the backlight brightness level.
  -w <val>, --write <val>
                        Set the backlight brightness level to <val>, where
                        <val> is a positive integer.
  -i <val>, --increment <val>, --increase <val>
                        Increment/increase the backlight brightness level by
                        <val>, where <val> is a positive integer.
  -d <val>, --decrement <val>, --decrease <val>
                        Decrement/decrease the backlight brightness level by
                        <val>, where <val> is a positive integer.
  -wp <val>, --write-percent <val>
                        Set the backlight brightness level to <val>%, where
                        <val> is a positive integer from 0 to 100.
  -ip <val>, --inc-percent <val>
                        Increment/increase the backlight brightness level by
                        <val>%, where <val> is a positive integer from 0 to
                        100.
  -dp <val>, --dec-percent <val>
                        Decrement/decrease the backlight brightness level by
                        <val>%, where <val> is a positive integer from 0 to
                        100.
  -m, --maximum         get max brightness level of display
  -f <dir>, --file <dir>
                        Specify alternative path to backlight control
                        directory. This is likely to be a subdirectory under
                        /sys/class/backlight/
