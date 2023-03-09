#!/usr/bin/perl

# Modules used
# use strict;
# use warnings;

$edad = 18;

if ($edad == 18) {
	print "Es mayor de edad\n";
} else {
	print "Es menor de edad\n";
}

# for (my $var = 0; $var < 5; $var++) {
# 	print $var;
# 	print "\n";
# }

@number = (23,45,23,5,2,6,8,10);

# foreach my $x (@number) {
# 	print $x;
# 	print "\n";
# }

# for (my $var = 0; $var < @number.length; $var++) {
# 	print @number[$var];
# 	print "\n";
# }

@arr2 = qw /This is a Perl Tutorial by GeeksforGeeks/;
foreach my $x (@arr2) {
	print $x;
	print "\n";
}

# Print function
# print "Hola mundo!\n";