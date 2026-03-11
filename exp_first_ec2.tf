provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "example" {
    ami           ="ami-02dfbd4ff395f2a1b"
    instance_type = "t2.micro"
    subnet_id     = "subnet-0a5bed300335b3a23"
}