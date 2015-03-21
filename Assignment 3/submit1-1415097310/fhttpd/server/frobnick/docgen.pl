#!/usr/bin/perl -w

my $numdocs = 100;
my $i;
for ($i = 1; $i <= $numdocs; $i++) {

  	my $ov = int(rand(2345));
	my $zorch = rand(27);
	my $zing = rand(123123);
	my $pronk = int(rand(3700));
	my $belzor = int(rand(2202));
	my $belpronk = $pronk / $belzor;
	my $total = (($ov * $zorch) / 2 * $zing) + $belzor + ($pronk ^ $belpronk);
	open (FILE, ">$i.frob");
	print FILE "Frobozz Magic Statistics Company\n";
	print FILE "Daily Results of Total Frobnick Output\n";
	print FILE "-----------------------------------------\n";
	print FILE "Frobnick Generator: $i\n\n";
	print FILE "Output Volume: $ov\n";
	print FILE "Zorch Index: $zorch\n";
	print FILE "Zing Factor: $zing\n";
	print FILE "Pronk/day: $pronk\n";
	print FILE "Belzor Number: $belzor\n";
	print FILE "Pronk/Belzor: $belpronk\n";
	print FILE "-----------------------------------------\n";
	print FILE "Total: $total\n";
	print FILE "-----------------------------------------\n";
	close FILE;
}
