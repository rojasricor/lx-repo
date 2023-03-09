# Indexing with positive numbers
m[1, ] # Select the first row
m[1:2, ] # Select the two first rows
m[, 3] # Select the last column
m[, c(1,3)] # Select the first and last column
m[1, ] <- 0 # Set the zeros vector to first row

# Indexing with negative numbers
m[-1, ] # Select all rows excluding the first row
m[-nrow(m), -ncol(m)] # Quit the last row and first column

# Indexing with boolean expresions
m_selection <- matrix(c(T,F,T,F,F,T,T,F,T,F,T,F,T,F,T,F,T), byrow=TRUE, nrow=3)
m[m_selection] # Select depending a booleans matrix
m[m > 7] # All > 7
m[m == 0] # All 0 zeros

# Indexing by names
colnames(m) <- c("c1", "c2", "c3")
rownames(m) <- c("r1", "r2", "r3")
m[, c("c1", "c3")] # Select columns by name
m[c("r1", "r3"), c("c1", "c2")] # Select rows and columns by name
