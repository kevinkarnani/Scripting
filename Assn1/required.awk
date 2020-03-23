#!/usr/bin/awk -f

/^required:/ {split($1,REQ,":")}

END {
	for (i in REQ) {
		if ( i != 1) {
			print REQ[i]
		}
	}
}

