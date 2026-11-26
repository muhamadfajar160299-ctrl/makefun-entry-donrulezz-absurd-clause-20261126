"""Write the one-liner entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib-only, deterministic. Writes exactly one file, only inside the
output directory named by the MAKEFUN_OUTPUT_DIR environment variable
(default /output). Never writes next to this script or into the cwd.
"""

import os
# Output goes only to the directory named by MAKEFUN_OUTPUT_DIR.
import sys

LINE = "Section 12.7: upon account deletion, the user's shadow remains the property of the Company and may be sublet to third parties at market rates."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.txt")
    payload = LINE.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
