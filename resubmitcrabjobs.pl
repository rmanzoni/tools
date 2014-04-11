#!/usr/bin/perl

use Cwd;

$numArgs = $#ARGV + 1;
if($numArgs < 1)
{
  print(">>>usage: resubmitcrabjobs FOLDER\n");
  exit;
}

$FOLDER = $ARGV[0];

$RESUBMITFLAG = 0;
if($numArgs > 1)
{
  $RESUBMITFLAG = $ARGV[1];
}



print("*************************************************************************************************\n");
print($FOLDER."\n");
print("*************************************************************************************************\n");



# create file with crab report
$REPORTFile = "./report.txt" ;
system("crab -status -c ".$FOLDER." > ".$REPORTFile);



$isExitCodeLine = 0;
$isEventNumberLine = 0;
open(REPORTFILE, $REPORTFile) ;
while(<REPORTFILE>)
{
  chomp;
  s/#.*//;  # no comments
  s/^\s+//; # no leading white
  s/\s+$//; # no trailing white                                                                                                                                      
  
  $line = $_;
  
  if($isEventNumberLine == 1)
  {
    @words = split(" ",$line);
    $eventList = @words[$words-1];
    
    $command = "crab -resubmit ".$eventList." -c ".$FOLDER;
    print($command."\n");
    if($RESUBMITFLAG == 1)
    {
	system($command);
    }
    
    $isEventNumberLine = 0;
  }
  
  if($isExitCodeLine == 1)
  {  
    @words = split(" ",$line);
    $exitCode = @words[$words-1];
    
    if($exitCode != 0)
    {
      print("\nExitCode : ".$exitCode."\n"); 
      $isEventNumberLine = 1;
    }
    
    $isExitCodeLine = 0;
  }
  
  if($isExitCodeLine == 0)
  {
    if( $line eq "crab:  ExitCodes Summary" )
    {
      $isExitCodeLine = 1;
    }
  }
  
}



system("rm ".$REPORTFile);

