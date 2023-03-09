inputs = list(1,2,34,5,6,"oops",0,12,3)

# for(input in inputs)
# 	print(paste("Log of", input, "=", log(input)))

# for(input in inputs)
	# try(print(paste("Log of", input, "=", log(input))))

for(input in inputs) {
	trycatch(
		print(
			paste("Log of", input, "=", log(input),
				warning = function(w) {
					print(paste("Negative argument", input));
					log(-input)
				},
				error = function(e) {
					print(paste("Non-numeric argument", input));
					NaN
				}
			)
		)
	)
}