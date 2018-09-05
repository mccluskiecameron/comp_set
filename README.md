# Compact Set

One is interested in storing a set of integers within some bound, in as little space as possible. If we know there are `k` integers in our set, and they are chosen from a set of `n` integers (normally `range(n)`), then we know the number of possible such sets is given as `n choose k`. This function can be evaluated in a few different ways.

One is as an index into pascals triangle, where the first row contains a single 1 surrounded otherwise by zeroes, and the cells of each subsequent row are the sum of the two cells above them (each row is offset from the previous by half a cell). We take `n` to give us the index of the row, and `k` to give us the index of the cell in that row, where the leftmost non-zero cell is index zero. 
A faster way is to take `product from i=0 to k-1 of (n-i)/(k-i)`. 

In either case, the number of states has some interesting properties. It is symmetrical, meaning that `n choose k` and `n choose n-k` are always the same. It is strictly less `2**n`, and takes its maximal value at k=n/2. `2**n` is the space used by equivalent bitfield for any value of k. It is therefore strictly more space efficient then the bitfield, and much more efficient for low or high k. 

Time efficiency is something different. The current implementations of both `cs` and `it_cs` have complexity proportional to `k**2`. This is assuming that int operations are constant time, which is not always the case given the size of ints being used. Assuming int operations with time proportional to the number of bits, the complexity becomes `k**2*n` in the worst case. 
