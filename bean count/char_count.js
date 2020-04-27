const countBs = function(a,b) {
	let count = 0;
	for(let c = 0; c < a.length; c++) {
		if(a[c] == b) {
			count = count + 1;
		}
	}
	return count;
}


