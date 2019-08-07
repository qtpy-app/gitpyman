# gitpyman
Manager your github : add comment for your response, stars, following use local language.
With the growth of stars and follwing, sometimes it's easy to forget why you care about them.

### Interface

![image.png](https://i.loli.net/2019/07/23/5d3688f11811917513.png)

### Use
- method 1: if you is a pythoner, you can :
```python
# you can clone repo and use `python setup.py install`
# or 
#`pip install gitpyman`
# after, use command `gitpyman` in console.
```

method 2: or download from :
...



### User Guide

![image.png](https://i.loli.net/2019/07/23/5d3685331e93078582.png)
(In this page , after you write website, username, password , click `Login/Update` button, will auto write to web ,so you can skip step 1.)
1. First Time , need login `github.com` (after will cache, No more login required) 
1. Everytime run software, must be click `Login/Update` button for get User authentication. 
1. `double click` can open url to reop; 

![image.png](https://i.loli.net/2019/07/23/5d3686270f75f26396.png)
1. filter keywords(user The blank space split) 

![image.png](https://i.loli.net/2019/07/23/5d3686b06295016538.png)

### How to Contribute

1. clone repo;
1. in pycharm set `gitpyman` folder as `Sources Root`;
1. in `Client.py` set `DEBUG = True` (about line 65);

### TODO:
- write tests(Sorry, I don't konw how to write unittest);
- support pyside2;
- add UML file;
- add doc;
- (add hook star/watch);
- add release;
- add backup .db --can't upload github,because has pwd;
- (add Multiple page); 
- change .db path --bug;

