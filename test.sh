#!/bin/bash
set -eux

echo "input" | pyperclip.py "--copy"
[ "$(pyperclip.py --paste)" = "input" ]

