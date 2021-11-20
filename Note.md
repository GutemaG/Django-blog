to check if user is auth
``` python
if request.user.is_authenticated():
    pass
# In Template
{% if user.is_authenticated %}
{%else%}
{% endif %}
```


# When you upload file to form: 
    * Don't forget enctype
  <form action="{% url 'create-blog' %}" method="POST" enctype="multipart/form-data">
    
  </form>