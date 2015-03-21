#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use strict;

# Barbazzo Fernap barbazzo@gue.com
# Gustar Woomax gustar@gue.com
# Wilbar Memboob wilbar@gue.com

# By the Frobozz Magic Software Company
# Released under the Grue Public License
# Suspendur 9th, 1068 GUE

# THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED
# BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE 
# COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” 
# WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, 
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND 
# FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY 
# AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE 
# DEFECTIVE, *AND IT WILL*, YOU ASSUME THE COST OF ALL NECESSARY 
# SERVICING, REPAIR OR CORRECTION.
	
my %labels; # global of pretty labels for memo pathnames

# glob through the homedirs for an array of paths to memos sorted by date
sub list_memo_selector {
	my @memos = </home/memo-users/memo/*>; # all memos are in this directory; show these on site
	foreach (@memos) {
		$_ =~ m#^.+/([^/]+)$#; # regex extract filename
		my $temp = $1;
		$temp =~ s/_/ /g; # convert _ to " "
		$labels{$_} = $temp; # assign pretty label name
	}
	print popup_menu(-name=>'memo',
									 -values=>\@memos,
								   -labels=>\%labels);
	print submit("Read memo");

}

print header();
print "<html><head><title></title></head><body>\n";

print h1("FrobozzCo Memo Distribution Website");
print h4("Got Memo?");
print hr();

print p('Select a memo from the popup menu below and click the "Read memo" button.');
print p("<form method='post' name='main'>\n");

if (!param('memo')) {
	list_memo_selector();
} else { # there is a memo selected
	list_memo_selector();
	my $memo = param('memo');

	if($memo !~ m#^\/home\/memo-users\/memo\/.*$#) {
		$memo = ""; # if memo does not start with "/home/memo-users/memo/", set memo to nothing
	}
	$memo =~ s/\.\.\///g; # globally remove all "../" matches to prevent executing other level directories
	my $author = "root";
	my @stat = stat $memo;
	my $date = localtime $stat[9];
	if ($memo =~ m#^/home/([^/]+)/.*$#) {
		$author = $1;
	}
	print "<hr>\n";
	print "<blockquote>";
	print '<table border=1><tr><td>';
	print "<center><b>$labels{$memo}</b></center>";
	print '</td></tr>';
	print "<tr><td>\n<p>";
	print "<b>Author:</b> $author<br />\n";
	print "<b>Subject:</b> $labels{$memo}<br />";
	print "<b>Date:</b> $date<br />\n";
	print "\n</p></td></tr>\n";
	print "<tr><td><p>&nbsp;</p>\n";
	print "<blockquote><p>\n";
	
	open (MEMO, $memo);
	
	foreach (<MEMO>) {
		$_ =~ s#\n$#</p><p>#; # HTMLize newlines for formatting
		print "$_\n";
	}
	print "</p></blockquote>\n";
	print '<p>&nbsp;</p></td></tr></table>';
	print "</blockquote>";
	print "<hr>\n";
}

print h2("To publish a memo:");
print <<TEXT;

<ol>
<li>Create a directory named 'memo' in your home directory.</li>
<li>Edit text files in that directory.</li>
<li>Save the file using underscores (_) for spaces, e.g. "free_lunch".</li>
</ol>

TEXT

print p('To remove your memo from publication, simply delete the file from tme memo directory.');

print "</form>\n";
print "</body></html>";
