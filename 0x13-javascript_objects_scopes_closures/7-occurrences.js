#!/usr/bin/node
exports.nbOccurences = function(list, searchElement){
    let count = 0;
    for (const items of list) {
	if (items === searchElement){
            count += 1;
	}
    }
    return count;
};
