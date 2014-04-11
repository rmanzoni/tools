#!/usr/bin/perl

 &defineColors() ;
 &parseARGV() ;
 &find() ;

#======================================================
sub find
{
  &setMatchColor() ;
  
  open(PIPE, "$cmd &|") ;
  while(<PIPE>)
  {
    chomp ;
    if(m/^${path}/)
    { 
      allCharacteristics($_) ;
      print("${ACCyan}${ACBold}_____________________________________________________________________________________________${ACPlain}\n") ;
    } else {
      if( m/($theMatch)/i ) {$theMatch = $1 ;}
      s/$theMatch/${ACRed}${ACBold}${theMatch}${ACPlain}/g ;
      s/^(\d+):/${ACGreen}--> ${ACCyan}${ACBold}${ACReverse}$1${ACPlain} : / ;
      print("$_\n") ;
    }
  }
  print("\n" ) ;
}

#======================================================
sub parseARGV
{
  $nArgs    = scalar @ARGV ;
  $path     = "./" ;
  $fileName = "\*" ;
  $fileName = "\\${fileName}" ;
  $grepArg  = "" ;

  if( $ARGV[0] =~ m/-(-)*h(elp)*/) {printUsage();}

  if( $nArgs == 1 )
  {
   if( $ARGV[0] =~ m/^\-/ ) {printUsage();}
   $theMatch = $ARGV[0] ;
   $cmd = "find $path -name $fileName -exec grep -n -i -I " . "'" . $ARGV[0] . "' {} \\; -print" ; 
   return ;
  }
  if( $nArgs == 2 && $ARGV[0] =~ m/^\-/i)
  {
   unless( $ARGV[0] =~ m/^\-i/ ) {printUsage();}
   $theMatch = $ARGV[1] ;
   $cmd = "find $path -name $fileName -exec grep -n -i -I " . "'" . $ARGV[1] . "' {} \\; -print" ; 
   return ;
  }

  unless( $ARGV[0] =~ m/^\-/ ) 
  {
    $path = $ARGV[0] ;
  }

  for( $i=0; $i<$nArgs; $i++)
  {
    if( $ARGV[$i] =~ m/^-name/) 
    {
      $fileName = $ARGV[${i}+1] ;
      $fileName =~ s/\*/\\*/g ;
      $grepArg = "-exec ls -la {} \\;" ;
    }
    
    if( $ARGV[$i] =~ m/^-exec/ && $ARGV[${i}+1] =~ m/^grep/) 
    {
      if( $ARGV[${i}+2] =~ m/^-i/ )
      {
       $j = 3;
       $option = $ARGV[${i}+2] ;
       $case   = "insensitive" ;
      } else {
       $j = 2;
       $option = "" ;
       $case   = "sensitive" ;
      }
      $theMatch = $ARGV[${i}+${j}] ;
      $grepArg = "-exec grep -n -i -I ${option} " . "'" . $theMatch ."' {} \\;" ;
    }
  } 
  if($path eq "." ) {$path = "./" ;}
  $cmd = "find $path -name $fileName $grepArg -print" ; 
  if($path =~ m/^\.\//) {$path = "\\./";}
  if($path =~ m/^\.\./) {$path = "\.\./";}
}
#======================================================
sub allCharacteristics
{
 my $fileName = @_[0] ;
 open(PIPA, "ls -l $fileName |") ;
 while(<PIPA>)
 {
  @e = split(/\s+/, $_) ;
  print <<EOB ;

    ${ACGreen}${e[4]}${ACPlain} $e[5] $e[6] $e[7] nc ${ACYellow}${ACBold}${e[8]}${ACPlain}
EOB
 }
 close(PIPA) ;
}
#======================================================
sub setMatchColor
{
  $nArgs = scalar @ARGV ;
  print("\n${ACCyan}${ACBold}_______${ACPlain}${ACCyan}${ACBold} Matches found with command: ${ACBlue}${ACBold}${cmd}${ACPlain}\n" ) ;
  print("\n" ) ;
  for( $i=0; $i<$nArgs; $i++)
  {
    if( $ARGV[$i] =~ m/^-exec/ && $ARGV[$i+1] =~ m/^grep/)
    {
#      $theMatch = $ARGV[$i+2]
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
#======================================================
sub printUsage
{
 print <<EOB ;
 
 ${ACBold}${ACUnderline}Usage:${ACPlain}
 
 ${ACBold}trova [path] [-name fileName] [-exec grep [-i] string]${ACPlain}
 
 or
 
 ${ACBold}trova [-i] string${ACPlain} 
 
 where:
 
 ${ACBold}path    :${ACPlain} a valid directory path-name (wildcards accepted)
 ${ACBold}fileName:${ACPlain} a valid file-name           (wildcards accepted)
 ${ACBold}string  :${ACPlain} any character string (if blanks are present, embed in double quotes)
 
 if ${ACBold}path${ACPlain} is omitted, the default is ${ACBold}./${ACPlain} (current directory)
 if ${ACBold}fileName${ACPlain} is omitted, the default is ${ACBold}*${ACPlain} (any file)
 
 
EOB

 exit ;
}

