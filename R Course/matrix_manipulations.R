a_matrix <- matrix(1:9, byrow=TRUE, nrow=3)
b_matrix <- matrix(11:19, byrow=TRUE, nrow=3)

# matrix unions by columns
big_matrix_2 <- cbind(a_matrix, b_matrix)
big_matrix_2

# matrix union with vector by columns
big_matrix_2 <- cbind(big_matrix_2, c(1,5,6))
big_matrix_2

# matrix unions by rows
big_matrix_1 <-rbind(a_matrix, b_matrix)
big_matrix_1

# matrix union with vector by rows
big_matrix_1 <- rbind(big_matrix_1, c(1,5,6))
big_matrix_1
