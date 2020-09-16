### News_Headlines

#### Author

[robajillo](https://github.com/robajillo)

#### Description
This is an application that will help people who want to get realtime news . The website will show news articles from several sources and news sources that a user can click to see more news. The  application consumes news from the [News API](https://newsapi.org/)

#### Live Demo

Click [Link](https://news-top-headlines.herokuapp.com/) to visit the site



#### User Story

1. A user would see various news sources on the homepage of the application.
2. A user would also be able to select a news source and see all news articles from the selected news source in the application.
3. A user will be able to see the image, description and the time a news article was created from the News-Articles tab.
4. A click on an article and read the full article on the source website.


#### Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  git clone https://github.com/robajillo/Python-IP2.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd news
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export API_KEY='{Enter your News Api Key}'
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


#### Technology used

* [Python3.6](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


#### Contact Information 

If you have any question or contributions, please email me at [rjillo@yahoo.com] or [rjillo259@gmail.com]

#### License
* *MIT License:*
* Copyright (c) 2020 **Roba Jillo**