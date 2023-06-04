#!/usr/bin/env python3

import sys
import os
#This file was made an executable using the chmod +x all_checks.py command


def check_reboot():
    """Returns true if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything is OK")
    sys.exit(0)

main()

print(check_reboot())