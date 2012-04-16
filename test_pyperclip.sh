#!/bin/bash
set -eux

echo -e "input \xE2\x98\xA0" | pyperclip.py "--copy"
[ "$(pyperclip.py --paste)" = "input ☠" ]

