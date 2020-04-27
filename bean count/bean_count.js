const countBs = function(a) {
	let count = 0;
	for(let c = 0; c < a.length; c++) {
		if(a[c] == 'B') {
			count = count + 1;
		}
	}
	return count;
}


