#!/usr/bin/awk -f

/^index:/ {split($1,INDEX,":")}

END {
	for (i in INDEX) {
		if ( i != 1 ) {
			print INDEX[i]
		}
	}
}	

