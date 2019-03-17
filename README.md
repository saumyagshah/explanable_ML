# Explanable_ML
We built a **web application** through which people can explain the predictions of various classifiers on different datasets
using *LIME* as well as *aLIME*
They needn’t have any expertise in programming or machine learning.
We’ve made the entire cumbersome process end to end.
The user just needs to upload the dataset in a rectangular format consisting only numerical entries with no entries missing.
Then she needs to type in various *features* and *class labels* that the dataset comprises of.

After that she can select various parameters like the explainer, classifier, number of top features, etc.

## How to use ##
1. Clone the repository
2. Run ```pip3 install -r requirements.txt``` in the terminal
3. Run ```python3 manage.py runserver```
4. Go to a Web Browser and type ```http://localhost:8000/lime/upload```

Some sample screenshots of the process are shown in the figure below. 

![Upload](https://github.com/ritesh99rakesh/explanable_ML/blob/master/images/upload.png)
![Feature Selection](https://github.com/ritesh99rakesh/explanable_ML/blob/master/images/feature.png)
![Class label Selection](https://github.com/ritesh99rakesh/explanable_ML/blob/master/images/label.png)
![Parameter Selection](https://github.com/ritesh99rakesh/explanable_ML/blob/master/images/parameter.png)
![Classifiers available](https://github.com/ritesh99rakesh/explanable_ML/blob/master/images/feature_particular.png)
![Results](https://github.com/ritesh99rakesh/explanable_ML/blob/master/images/result.png)
