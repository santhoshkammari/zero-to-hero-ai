# NumPy Section Rewrite Plan

## Style: Brandon Rohrer
- Personal confession opening
- Build from absolute zero with toy examples
- Running example: tiny movie ratings → similarity (3 users, 4 movies)
- Vulnerability moments throughout
- Recurring analogies: bookshelf (memory layout), assembly line (vectorization)

## Concept Ladder (dependency order)
1. Why arrays exist (Python list problem → contiguous memory)
2. The ndarray under the hood (data pointer + shape + strides + dtype = array)
3. Strides - the real trick (how one block of memory becomes any shape)
4. Views vs copies (the consequence of strides)
5. Broadcasting (strides of zero, shape manipulation)
6. Vectorization (C code, BLAS, why loops are slow)
7. **REST STOP** - you now have the mental model
8. Reshaping and the stride connection
9. einsum - the universal tensor language
10. Production patterns and gotchas (memory allocation, dtype, in-place)

## Vulnerability Moments
1. "I avoided looking at how NumPy actually works for years"
2. "broadcasting confused me until I understood strides"
3. "I still print shapes compulsively"
4. "nobody fully understands why BLAS is so fast at the assembly level"
5. "I've been bitten by the view/copy distinction more times than I'd like to admit"

## Running Example
- 3 users rating 4 movies → stored as array
- Compute mean rating per user (axis demo)
- Center the ratings (broadcasting demo)
- Compute similarity between users (vectorization/matmul demo)
- Reshape for batch processing (reshape demo)

## Analogies
1. Bookshelf: contiguous memory = books in order on shelf. Python list = sticky notes pointing to books scattered around library.
2. Assembly line: vectorized ops = conveyor belt processing 1000 items. Python loop = hand-delivering each item to the machine.
