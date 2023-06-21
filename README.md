# 🧰 Dlib facial recognition system

This is a DEMO system that uses Django, PostgreSQL, OpenCV and Dlib to perform facial recognition.

The dataset used for the tests is the [LFW](http://vis-www.cs.umass.edu/lfw/)

### 🏷️ Stack

- **[Django](https://www.djangoproject.com/)** - Python web framework
- **[OpenCV](https://opencv.org/)** - Computer Vision library
- **[Dlib](http://dlib.net/)** - Modern C++ toolkit containing machine learning algorithms
- **[Postsgresql](https://www.postgresql.org/)** - (with CUBE extension) - Open source object-relational database


### 📚 Theory

**The training mode**

For the "training" of a person's face, a photo is uploaded to the system.
If there is a face in the image, 128 points (features) are extracted from that face.
This array of points are then stored in the database.

**Facial recognition**

To recognize a person's face, we pass a photograph to the system.
The system will extract a matrix of 128 points from the face and then it will try to locate in the database which
previously trained face has the matrix of points closest to the searched face.
To do this search in the PostgreSQL database
the [CUBE](https://www.postgresql.org/docs/current/cube.html) extension is used.
This extension provides a function that calculates the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)
of the face points with the points saved in the database.
The query returns the id of the face with the closest array of points to the points of the queried face.

### 🛠️ Prerequisites
To run this demo it is necessary have [DOCKER](https://www.docker.com/) and [DOCKER COMPOSE](https://docs.docker.com/compose/) installed on your machine.

If you don't have docker, just follow the step by step according to your operating system at this [LINK](https://docs.docker.com/get-docker/).

### 👐🏽‍️ Hands-on

Clone repository

```
git clone XXXX
```


Starting the system
```
 docker compose -f 'docker/dev/docker-compose.yml' up
```

**⚠️ ATTENTION**
- *The container image creation step takes some time.* **(~5 minutes** 😴)

- *If you wish, it is not necessary to load and train images from the LFW
dataset. The training is a **very slow process**, there are more than 5000 images to extract
the points matrix and save it in the database. On my personal computer, this **process takes
an average of 90 minutes** , so if you choose to go this route while the images are being
processed, you can walk away a bit, grab a coffee* ☕ *, etc... On the other hand, if you choose not to
import the dataset there is an option in django-admin to register and train your personal images for testing.*

Extract and loading the LFW dataset into database.
```
docker compose -f 'docker/dev/docker-compose.yml' run --rm django bash -c "python src/manage.py load_lfw"
```

Training / extract points from images **(more time needed... 💤)**
```
docker compose -f 'docker/dev/docker-compose.yml' run --rm django bash -c "python src/manage.py training_photos"
```

Test system on browser in http://localhost:8000/ with the credentials below.
```
user: demo@demo.com
password: demo
```

**Adding new persons**

For add a new person go to **persons list** in http://localhost:8000/admin/recognizer/person/ and click **add person** button
on top right corner.

**Training new persons**

Select the person you want to train the images from the **persons list**
in http://localhost:8000/admin/recognizer/person/  and choose the action
**"Training person(s) photo(s)"** and then click the go button.

**Test facial recognition**

On persons list http://localhost:8000/admin/recognizer/person/  click in **facial recognition** button on top right corner

 😎 Enjoy !!!


---

### 💡 Tips and Ticks

- Facial recognition is more effective with more trained photos of the person you are looking for.
This helps to avoid false positives. Some people in the LFW dataset only have a single photo.
- Images with more than one face cannot be trained on this system.
- To register a new user or recover password, you can access this link http://localhost:8025 (mailhog) to verify
the emails received.

### ✏️ Notes

This project is for educational purposes only and must not be used under any circumstances for other purposes.
