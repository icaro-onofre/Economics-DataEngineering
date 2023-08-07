#Okonomikus - CVM project

##Description
This project aims to extract and analyse data from CVM repository, as DRE reports and others.
To do that, this container keeps some python files which were developed to collect data from CVM, unzip all the files, save as csv and then store it on s3 bucket.

Its required to build a docker image based on available Dockerfile. Then run container based on that image. Also is required to set up aws configure in order to write files on s3 bucket.

Follow the steps bellow to set up the enviroment.

##steps to build image and set up aws profile
<!-- build docker image -->
docker build -t okonomikus:cvm-de .

<!-- setting up aws profile -->
aws configure --profile okonomikus-de

AWS Access Key ID [None]:       <access_key_id>
AWS Secret Access Key [None]:   <secret_access_key>
Default region name [None]:     <region_name>
Default output format [None]:   <text/json>

<!-- Storing aws profile -->
$ export AWS_PROFILE=okonomikus-de
$ echo $AWS_PROFILE



