Depth-First Search Approach

How it works:

When you encounter an island fragment (an element with a value of 1), you increment the island counter.
Search the neighboring elements, setting all ones belonging to the same island to zero to prevent recounting them.

Downsides:

Modifies the input matrix