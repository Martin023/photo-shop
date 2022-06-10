# tesagram
A minimalistic instagram clone 

## About tesagram
This is an instagram clone that where users can:
* Upload photots
* Follow other users
* Like photos
* Commenting on photos
* Viev posts by other users.


## Getting Started

To get started on running tesagram on your local machine :
You may fork this repository then clone the application or directly clone from this repository:
git clone 

Install requirements : pip install -r requirements.txt

You can create your own database and replace environment variables with your own values
for example database name, and password.

### Prerequisites
The pre-requisites include
- Having python installation (latest version is a plus).
- A python code editor eg pycharm or visual-studio.
- postgresql server optional if you want to use a different database.

I have attached links to these softwares if you do not have any of the above here:

* https://www.python.org/downloads/ python download
* https://visualstudio.microsoft.com/downloads/ Visual-studio
* https://www.jetbrains.com/pycharm/download/ Py-charm code editor
* https://www.postgresql.org/download/ postgresql database and server

### Installing
After a successful clone and installation of the pre requisites.
Navigate to the parent folder of the application.
cd < location-folder-on-your-machine >/tesagram .

Open with visual-studio 
code .

Install the requirements
pip install -r requirements.txt

Create your database
1. Run psql
2. CREATE DATABASE <your database name of choice> <preferred username> <preffered password>

Read more about postgress databases 
https://www.postgresql.org/docs/
  
Finnaly set-up your envirnment variables
* Create a .env file in the main app folder.
using terminal : touch .env 
* Replace variables with our own values for example.
BD_USER='your database name'.
TIP : Ensure no spacing between the = assignment symbol.

* Run your application:
python3 manage.py runserver
  
A demo result of the above.
![Screenshot from 2022-06-10 05-19-10](https://user-images.githubusercontent.com/36125591/172978627-2b4f9b27-a5d2-41b4-b2be-6064cdfd3708.png


## Deployment

kindly checkout this decumentation for a comprehensive guide to deployment.
[documentation](https://gist.github.com/Martin023/7480301120aef8b7546130ed3ce6db69)

## Built With

* [Django](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [pip](https://maven.apache.org/) - pip package installer
* [python](https://rometools.github.io/rome/) - python

## Contributing

Open a new 

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

