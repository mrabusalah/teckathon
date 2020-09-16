# Facial Features to Measure student's Attention

FutureAmazonians team consists of 3 students :
    - [`Abdullah A. AbuSalah`](https://github.com/mrabusalah)
    - [`Fuad A. Daoud`](https://github.com/Fox-Immortal)
    - [`Yousef R. Hammad`](https://github.com/youhammad)

# Project Name

    Facial Features to Measure student's Attention
### Problem statement

In a traditional learning, there are different methods to get student's attention. Teachers could ask about some unexpected thing to catch students’ attention, or he can increase his voice to collect eye sights. But this is not the case in e-learning. Attracting students’ attention in online learning is a challenge and the more challenging is to calculate their attention during online session. The only available way these days through answering some online activities such as quiz or assignment. The teacher has no other evidence to know about the student status during online session, if he is watching the lesson with full attention, or he is not caring about the online content, just open his mobile or laptop with looking into screen.

### Solution Proposal
By analyzing student's facial features such as eyes direction, mouth states, chin position, eyebrows and many other features, we can calculate the student's attention.
The idea is to ask the student to open his web/mobile camera during online session (Required a device with a camera).
And start monitoring his attention by analyzing facial features that will be used to calculate the student's attention. The system will generate reports to course teacher based on student performance.


### Benefits
* Provide indicator about student attention during online session.
* Develop learning ways from a feed-back results.
* Find incomprehensible subjects from courses.
* Increase a student’s attention and improve learning performance of students.

### The main technologies we have been used
- Backend / JAVA (Spring freamwork)
- Frontend / Angular
- Proccess / Python
- Database / MySql


### Installation
first of all you should clone this project and open it in JetBrains intellij idea.
and then add the 1.8 java SDK to project structure & languate level 8 - Lambdas.
the IDE will notice you that there is an angular project if you want to Enable the angular plugin , please accept it.

now you should connect the data basae:
kindly install mySQL [workbench](https://www.mysql.com/products/workbench/) database management system or any other DBMS.
read application.properties file in src/main/resources path to see the configuration for database


Run the POM.xml dependencies and generate the target folder.

```sh
$ mvn clean install
```

For angular environments .

```sh
$ npm install
```

### python

we used alot of pyhton libs 
| Lib | link |
| ------ | ------ |
| numpy | https://numpy.org |
| opencv-python | https://pypi.org/project/opencv-python/ |
| dlib | https://pypi.org/project/dlib/ |
| sklearn | https://pypi.org/project/scikit-learn/ |
| tensorflow | https://pypi.org/project/tensorflow/ |
| keras | https://pypi.org/project/Keras/ |
| screeninfo | https://pypi.org/project/screeninfo/ |
| imutils | https://pypi.org/project/imutils/ |

now go to your browser and open this link
```sh
http://localhost:4200
```

