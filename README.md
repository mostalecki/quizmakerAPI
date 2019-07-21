# quizmakerAPI
Web API for my other project - [quizmaker](https://www.github.com/mostalecki/quizmaker), created using Django REST framework.

Api consists of 3 endpoints that take/return data in json format:
<ul>
    <li>GET /quizzes/ - list of all quizzes (id, title, details url)</li>
    <li>GET /quizzes/&lt;int:pk&gt;/ - details of a quiz of given id</li>
    <li>POST /quizzes/create/ - takes in quizz data and, if validated correctly, saves it to database</li>
</ul>
