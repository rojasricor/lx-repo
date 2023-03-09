# m1 <- matrix(1:9, byrow=TRUE, nrow=3)
# m1

# m2 <- matrix(c(0,-1,4)) # Create a matrix with one column
# m2

# d1 <- diag(3) # Create a diagonal matrix 3x3
# d1

# d2 <- diag(c(1,2,3)) # Create a diagonal matrix and set the vector as diagonal
# d2

# t_m1 <- t(m1) # m1 transpost
# t_m1
# e <- eigen(m1) # AutoValues and AutoVectors list
# e
# d <- det(m1) # The matrix determinant
# d

##########################
# Operations with matrix #
##########################
a_matrix <- matrix(1:9, byrow=TRUE, nrow=3)
a_matrix
b_matrix <- matrix(11:19, byrow=TRUE, nrow=3)
b_matrix

total_matrix <- a_matrix * b_matrix
total_matrix

total_matrix <- a_matrix + 2
total_matrix

rowSums(total_matrix)
colMeans(total_matrix)
max(total_matrix)
