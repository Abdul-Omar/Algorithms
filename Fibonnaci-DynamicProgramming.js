
/* I use dynamic programming to memoize results that are 
 * unneccessarily repeated in regular fibonnaci recursive function
 * runtime now is O(n) instead of O(2^n)
 */
function fibonnacci_dp(){

	let cache = {};

	return function fibonnacci(n){

		if( n in cache){

			return cache[n];
		}
		else{

			if( n < 2){

				return n;
			}
			else{

				cache[n] = fibonnacci(n-1) + fibonnacci(n-2);
				return cache[n];
			}
		}

	}
}