# Automation-scripts

alias tfaplan='python3 /Users/hapham/python/tfaplan.py'

# Support clipboard content target in file .tf
 ~/python  tfaplan
 
atlantis plan -- -target "aws_vpc"."my_vpc" -target "aws_subnet"."my_subnet" -target "aws_network_interface"."foo" 

Number of Resoure target is: 3
Number of Module target is: 0


-----------------------------

# target resource in file .tf
 ~/python  tfaplan aws-test.tf resource                                                                                                                    
atlantis plan -- -target "aws_vpc"."my_vpc" -target "aws_subnet"."my_subnet" -target "aws_network_interface"."foo" 

Number of Resoure target is: 3
Number of Module target is: 0


-----------------------------

#target module in file .tf
 ~/python  tfaplan aws-test.tf module 
 
atlantis plan -- -target module."ec2_instance" 

Number of Resoure target is: 0
Number of Module target is: 1


-----------------------------
#target resource + module in file .tf
 ~/python  tfaplan aws-test.tf                                                                                                                             
atlantis plan -- -target "aws_vpc"."my_vpc" -target "aws_subnet"."my_subnet" -target "aws_network_interface"."foo" -target module."ec2_instance" 

Number of Resoure target is: 3
Number of Module target is: 1


-----------------------------
