import os
import pyttsx3
import getpass
import boto3 
import subprocess as sb
import webbrowser as wb

apass = "redhat"

pyttsx3.speak("How can I help you")
pyttsx3.speak("please enter the password to use the services")
passwd = getpass.getpass("Enter Your Password :")
if passwd != apass:
	print("Authentication Incorrect")
	pyttsx3.speak("Your Password in Wrong")
	exit()
else:
	pyttsx3.speak("welcome to the world of python automation")
	print("\t\t\t***********************************************************************************")

	print("\t\t\tWelcome to the world's advanced program I will do everything for you")


	print("\t\t\t***********************************************************************************")

	
	print("""
	available services:
	1. EC2
	2. S3
	3.cloudfront
	4.Docker
	5.Hadoop""")
	pyttsx3.speak("Please simply write the name of service from the above list")
	print("Which service you want to use:", end='')
	service = input()
	print(service)
	if service == "EC2":
		while True:
			pyttsx3.speak("Thanks for choosing EC2 services")
			ec2 = boto3.client('ec2', 
				'ap-south-1', 
				aws_access_key_id='', 
				aws_secret_access_key='') 

	
			response = ec2.describe_instances() 
			


			print("""\t\t\tPress1 : To launch a new instance.
			press2 : To describe a particular instance.
			press3 : To Start an instance that already created.
			press4 : To stop an instance.
			press5 : To create new volume.
			press6 : To create new security group.
			press7 : To create new key-pair.
			press8 : To attach a volume to the instance.
			press9 : To terminate the instance.
			press10 : To exit from the EC2""")
			pyttsx3.speak("choose the option accroding to your need")
			print("choose your option:", end='')
			ch1 = input("choose a option:")
			if int(ch1) == 1:
				pyttsx3.speak("please select a region")
				region = input("please select a region:")
				
				pyttsx3.speak("I need some information to launch the instance")
				pyttsx3.speak("please type the image-id:")
				image_id = input("please give me image id:")

				pyttsx3.speak("please write the key name")
				key_name = input("which key you want to use:")

				pyttsx3.speak("select a instance type")
				instance_type = input("select the instance type:")

				pyttsx3.speak("please select a security group")
				security_group = input("choose a security group:")
				os.system("aws ec2 run-instances --image-id {} --count 1 --instance-type {} --key-name {} --security-group-ids {} --subnet-id subnet-64c6cf0c".format(image_id,instance_type,key_name,security_group))
				
			elif int(ch1) == 2:
				pyttsx3.speak("Give a instance id")
				instance_id = input("give the instance-id:")
				os.system("aws ec2 describe-instances --instance-id {}".format(instance_id))

			elif int(ch1) == 3:
				pyttsx3.speak("Please give me the instance id so i will start the instance")
				start_instance = input("give a instance-id for start the o.s:")
				os.system("aws ec2 start-instances --instance-ids {}".format(start_instance))

			elif int(ch1) == 4:
				pyttsx3.speak("please tell instance id to stop the instance")
				stop_instance = input("please tell instance id to stop the instance:")
				os.system("aws ec2 stop-instances --instance-ids {}".format(stop_instance))

			elif int(ch1) == 5:
				size = input("give the size for volume(in GB):")
				pyttsx3.speak("please tell the size of the volume")				
				os.system("aws ec2 create-volume --availability-zone ap-south-1a --size {} --volume-type gp2".format(size))

			elif int(ch1) == 6:
				pyttsx3.speak("give a name for the security group")
				security = input("give a name for the security group:")
				os.system(" aws ec2 create-security-group --group-name {} --description {}".format(security))
			elif int(ch1) == 7:
				key_name = input("give a name of your key:")
				os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
			
			elif int(ch1) == 8:
				pyttsx3.speak("Give the instance id")
				instance_id = input("Choose an instance for this volume:")
				pyttsx3.speak("choose a volume which you want to use")
				volume_id = input("give the volume id:")
				os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/sdf".format(instance_id,volume_id))
			elif int(ch1) == 9:
				pyttsx3.speak("Give the instance id")
				instance_id = input("Choose an instance for termiante:")
				os.system("aws ec2 terminate-instances --instance-ids {}".format(instance_id))	
			elif int(ch1) == 10:
				break				
			else:
				pyttsx3.speak("Please choose a valid option")
				print("option does not support!!")
			input("enter to continue...")
			os.system("cls")


	elif service == "S3":
		while True:
			pyttsx3.speak("Thanks for choosing S3 services")
			ec2 = boto3.client('ec2', 
				'ap-south-1', 
				aws_access_key_id='', 
				aws_secret_access_key='')

	
			print("""\t\t\tPress1 : To see the data inside a S3 bucket.
			press2 : To create a new bucket.
			press3 : To see the complete list of s3 buckets.
			press4 : To delete a bucket.
			press5 : To delete an object from the bucket
			press6 : To copy the data from one bucket to another bucket.
			press7 : To upload the data in S3 bucket.
			press8 : To exit...""")
			print("choose your option:", end='')
			pyttsx3.speak("choose the option accroding to your need")
			ch1 = input()
			print(ch1)
			if int(ch1) == 1:				
				pyttsx3.speak("please select a bucket")
				bucket_name = input("choose a bucket to see the data:")
				os.system("aws s3 ls s3://{}".format(bucket_name))

			elif int(ch1) == 2:				
				pyttsx3.speak("please give  a bucket name your bucket name must be unique")
				bucket_name = input("give a name for the bucket:")
				os.system("aws s3 mb s3://{}".format(bucket_name))

			elif int(ch1) == 3:
				pyttsx3.speak("These are buckets in your aws account")
				os.system("aws s3 ls")


			elif int(ch1) == 4:				
				pyttsx3.speak("please give  a bucket name that you want to delete")
				bucket_name = input("give a bucket name:")
				os.system("aws s3 rb s3://{} --force".format(bucket_name))
				
			elif int(ch1) == 5:
				pyttsx3.speak("please tell me the object and bucket name")
				bucket_name = input("give the bucket name:")
				folder = input("give the object name:")
				os.system("aws s3 rm s3://{}/{}".format(bucket_name,folder))

			elif int(ch1) == 6:
				pyttsx3.speak("Give the bucket name that have object")
				first_bucket = input("Give the source bucket name:")
				pyttsx3.speak("Give the object that you want to copy")
				object = input("give the object name that you want to copy:")
				pyttsx3.speak("in which bucket yo want to copy the object")
				second_bucket = input("give the target bucket name:")
				os.system("aws s3 cp s3://{}/{} s3://{}/".format(first_bucket,object,second_bucket))

			elif int(ch1) == 7:
				pyttsx3.speak("Please give the folder or file which you want to upload")
				path = input("give the complete path that you want to upload:")
				pyttsx3.speak("In which bucket you want to upload the data ")
				bucket_name = input("Give the bucket name:")
				os.system("aws s3 sync {} s3://{}".format(path,bucket_name))

			elif int(ch1) == 8:
				pyttsx3.speak("closing the program")
				exit()
			
			else:
				pyttsx3.speak("Please choose a valid option")
				print("option does not support!!")	
			input("enter to continue...")
			os.system("cls")


	elif service == "cloudfront":
		while True:
			pyttsx3.speak("Thanks for choosing cloudfront services")
			ec2 = boto3.client('ec2', 
				'ap-south-1', 
				aws_access_key_id='', 
				aws_secret_access_key='')

	
			print("""\t\t\tPress1 : To get the information of a cloud distribution.
			press2 : To create a new cloudfront distribution.
			press3 : To delete a cloudfront distribution.
			press4 : To get the list of all the distribution.
			press5 : To exit...""")
			print("choose your option:", end='')
			pyttsx3.speak("choose the option accroding to your need")
			ch1 = input()
			print(ch1)
			if int(ch1) == 1:				
				pyttsx3.speak("please enter a cloudfront distribution id")
				id = input("Enter a cloudfront id:")
				os.system("aws cloudfront get-distribution --id {}".format(id))

			elif int(ch1) == 2:				
				pyttsx3.speak("please give  a bucket name that already created")
				bucket_name = input("give a bucket name:")
				os.system("aws cloudfront create-distribution --origin-domain-name  {}.s3.amazonaws.com".format(bucket_name))

			elif int(ch1) == 3:
				pyttsx3.speak("please enter a cloudfront distribution id")
				id = input("Enter a cloudfront id:")
				pyttsx3.speak("please give distribution's ETag so i can verify your distribution, if you don't know Etag you can get it from option 1")
				etag = input("give the distribution's Etag id:")
				os.system("aws cloudfront delete-distribution --id {} --if-match {}".format(id,etag))


			elif int(ch1) == 4:				
				os.system("aws cloudfront list-distributions")
				

			elif int(ch1) == 5:
				pyttsx3.speak("closing the program")
				exit()
			
			else:
				pyttsx3.speak("Please choose a valid option")
				print("option does not support!!")	
			input("enter to continue...")
			os.system("cls")
	elif service == "Docker":
		while True:
			pyttsx3.speak("Thanks for choosing docker services...This docker is installed in the instance in cloud which is configured as a web server and you all can access it through CGI ,so basically it is the integration of docker, webserver and AWS cloud ")
			print("""\t\t\tPress1 : To display all docker images.
			press2 : To launch a new docker container.
			press3 : To display all running docker containers.
			press4 : To list all running or stopped docker containers.
			press5 : To delete the specified container
			press6 : To delete all the containers
			press7 : To exit...""")
			print("choose your option:", end='')
			pyttsx3.speak("choose the option accroding to your need")
			ch1 = input()
			print(ch1)
			if int(ch1) == 1:				
				pyttsx3.speak("ok ,Listing the available docker images from your linux instance")
				wb.open("http://13.126.190.104//cgi-bin/shivame.py?x=sudo+docker+images")
			elif int(ch1) == 2:
				print("Please specify the name you want to give to your docker container ")
				pyttsx3.speak("Please specify the name you want to give to your docker container")
				k=input()
				print("Please specify the name of the docker image you want to launch ")
				pyttsx3.speak("Please specify the name of the docker image you want to launch")	
				l=input()	
				pyttsx3.speak("ok ,Launching the specified docker container with specified name from your linux instance")		
				wb.open("http://13.126.190.104/cgi-bin/shivame.py?x=sudo+docker+run+-d+-it+--name+{0}+{1}+".format(k,l))
			elif int(ch1) == 3:				
				pyttsx3.speak("ok ,Listing the running docker containers from your linux instance")
				wb.open("http://13.126.190.104/cgi-bin/shivame.py?x=sudo+docker+ps")
			elif int(ch1) == 4:
				pyttsx3.speak("ok ,Listing all running or stopped docker containers from your linux instance")
				wb.open("http://13.126.190.104/cgi-bin/shivame.py?x=sudo+docker+ps+-a")	
			elif int(ch1) == 5:
				print("Please specify the name of the container you want to delete")
				pyttsx3.speak("Please specify the name of the container you want to delete")	
				k=input()
				pyttsx3.speak("ok ,Deleting the specified container from your linux instance")
				wb.open("http://13.126.190.104/cgi-bin/shivame.py?x=sudo+docker+rm+{}+-f".format(k))
			elif int(ch1) == 6:
				pyttsx3.speak("ok ,clearing all the containers from your linux instance")
				wb.open("http://13.126.190.104/cgi-bin/shivame.py?x=sudo+docker+container+rm+-f++%24%28sudo+docker+container+ls+-a+-q%29")
			elif int(ch1) == 7:
				pyttsx3.speak("closing the program")
				exit()	
			else:
				pyttsx3.speak("Please choose a valid option")
				print("option does not support!!")	
			input("enter to continue...")
			os.system("cls")
	elif service == "Hadoop":
		
		while True:
			pyttsx3.speak("Thanks for choosing hadoop services.. ")
			print("""\t\t\tPress1 : To upload any file in the hadoop cluster.
			press2 : To see all the uploaded files in the cluster.
			press3 : To read a particular file.
			press4 : To remove a file from the cluster.
			press5 : To upload a file with the specified block size in the cluster
			press6 : To exit...""")
			print("choose your option:", end='')
			pyttsx3.speak("choose the option accroding to your need")
			ch1 = input()
			print(ch1)
			if int(ch1) == 1:
				print("Please specify the name of the file(along with location) you want to upload ")
				pyttsx3.speak("Please specify the name of the file along with location you want to upload")
				
				k=input("file name:")
				sb.getoutput('ssh -i "{}"  ec2-user@{} "sudo hadoop fs -put {} /;".format(key_name,ip,k)') 
				print("file uploaded in the cluster")
			elif int(ch1) == 2:
				
				pyttsx3.speak("ok, listing all the files uploaded in the cluster")
				sb.getoutput('ssh -i "key_name"  ec2-user@ip "hadoop fs -ls /"')
			elif int(ch1) == 3:
				print("Please specify the name of the file you want to read from the cluster ")
				pyttsx3.speak("Please specify the name of the file you want to read from the cluster")
				key_name = input("Enter your key name:")
				ip = input("Enter your client ip:")
				k=input()
				sb.getoutput('ssh -i "{}"  ec2-user@{} "sudo hadoop fs -cat /{};".format(key_name,ip,k)')
			elif int(ch1) == 4:
				print("Please specify the name of the file you want to delete from the cluster ")
				pyttsx3.speak("Please specify the name of the file you want to delete from the cluster")
				k=input("file name:")
				sb.getoutput('ssh -i "<keyname>"  ec2-user@<ip of client> "sudo hadoop fs -rm /{};".format(k)') 
				print("successfully deleted a.txt")
			elif int(ch1) == 5:
				print("Please specify the name of the file(along with location) you want to upload")
				pyttsx3.speak("Please specify the name of the file along with location you want to upload")
				k=input()
				print(r'Please specify the size of the block in "bytes" with which you want to upload the file')
				pyttsx3.speak("Please specify the size of the block in bytes with which you want to upload the file")
				l=input()
				m=int(l)
				sb.getoutput('ssh -i "<keyname>"  ec2-user@<ip of client> "sudo hadoop fs -Ddfs.block.size={} -put {} /;".format(m,k)') 
				print("{} file with size {} bytes uploaded in the cluster".format(k,m))
			elif int(ch1) == 6:
				pyttsx3.speak("closing the program")
				exit()
			else:
				pyttsx3.speak("Please choose a valid option")
				print("option does not support!!")	
			input("enter to continue...")
			os.system("cls")

	else:
		print("please check again...")
		pyttsx3.speak("please check your command and try again")