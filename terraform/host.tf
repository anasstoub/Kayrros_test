provider "aws" {
  region = "eu-west-3"
}

# EC2 instance to host FastAPI application
resource "aws_instance" "myFastAPIapp" {
  ami           = "ami-0302f42a44bf53a45"  
  instance_type = "t2.micro"
  key_name      = "testt"      

  # User data to install necessary dependencies and run the app
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y python3-pip git
              pip3 install uvicorn fastapi pandas
              git clone https://github.com/anasstoub/Technical_test.git /home/ubuntu/my_test
              cd /home/ubuntu/my_test
              uvicorn main:app --reload 
              EOF
   
  tags= {
    Name = "MyFastAPIInstance"
  } 
  
}