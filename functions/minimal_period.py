def minimal_period(n):
    
    # Initialize least common multiple accumulator
    p = 1

    # Create n x n matrix of ones (to mark unvisited positions)
    li = o([n, n])

    # Iterate through every pixel (i, j)
    for i in range(n):
        for j in range(n):

            # If the current position has not been visited
            if int(li[i][j]) == 1:

                # Count steps (c) in the orbit of (i, j)
                c = 1
                i_1 = i
                j_1 = j

                # Apply the ACM repeatedly until we return to the original pixel
                while ((2 * i_1 + j_1) % n) != i or ((i_1 + j_1) % n) != j:
                    a = i_1
                    i_1 = (2 * i_1 + j_1) % n
                    j_1 = (a + j_1) % n
                    c += 1

                    # Mark this position as visited
                    li[i_1][j_1] = 0

                # Update the least common multiple with the orbit length
                p = l(p, c)

    return p