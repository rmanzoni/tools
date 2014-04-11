#!/usr/bin/perl

#==================================================
# Author: D. Menasce
#==================================================

$selector = $ARGV[0] ;

&defineColors() ;

$env = `printenv` ;

@env = split(/\n/,$env)  ;

$longest = 0 ;

foreach $e (sort @env)
{
 ($key,$val) = split(/=/,$e) ;
 $l = length $key ;
 if( $l > $longest ) {$longest = $l ;}
}

$allblanks = "" ;
foreach $l (0 ... $longest) {$allblanks .= " ";}

foreach $e (sort @env)
{
 ($key,$val) = split(/=/,$e) ;
 $blanks = "" ;
 foreach $l (0 ... $longest - length $key) {$blanks .= " ";}
 @pieces = split(/:/, $val ) ;

 if( $selector ne "" && $key =~ m/$selector/ ) 
 {
  $key =~ s/$selector/${ACBold}${ACCyan}${selector}${ACPlain}/ ;

  &splitPieces() ;
 }
 elsif( $selector eq "" )
 {
  &splitPieces() ;
 }
 
}
#======================================================
sub splitPieces
{
  $i      = 0  ;
  %double = {} ;
  foreach $p (@pieces)
  {
    $double{$p}++ ;
    $color = ${ACPlain} ;
    if( $double{$p} > 1 ) {$color = "${ACBold}${ACRed}" ;}

    if($i++ == 0 ) 
    {
      print("${ACBold}${ACYellow}${key}${ACPlain} $blanks ${color}$pieces[0]${ACPlain}\n") ;
    }
    else
    {
      print("$allblanks  ${color}${p}${ACPlain}\n" ) ;
    }
  }
}

#======================================================
sub defineColors
{
  $ACBlack	 = "\x1B[0;30m";
  $ACBlue	 = "\x1B[0;34m";
  $ACGreen	 = "\x1B[0;32m";
  $ACCyan	 = "\x1B[0;36m";
  $ACRed	 = "\x1B[0;31m";
  $ACPurple	 = "\x1B[0;35m";
  $ACBrown	 = "\x1B[0;33m";
  $ACGray	 = "\x1B[0;37m";
  $ACDarkGray	 = "\x1B[1;30m";
  $ACLightBlue   = "\x1B[1;34m";
  $ACLightGreen  = "\x1B[1;32m";
  $ACLightCyan   = "\x1B[1;36m";
  $ACLightRed	 = "\x1B[1;31m";
  $ACLightPurple = "\x1B[1;35m";
  $ACYellow	 = "\x1B[1;33m";
  $ACWhite	 = "\x1B[1;37m";

  $ACPlain	 = "\x1B[0m";
  $ACBold	 = "\x1B[1m";
  $ACUnderline   = "\x1B[4m";
  $ACBlink	 = "\x1B[5m";
  $ACReverse	 = "\x1B[7m";

  $ACClear	 = "\x1B[2J";
  $ACClearL	 = "\x1B[2K";
}
