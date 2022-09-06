# nglibrary
Web application in Django using API of Open Library. This app also has its own API.

The app is deployed at https://nglib.herokuapp.com

__Features:__
- user can search for the author's published books,
- results are collected through API of the Open Library,
- results can be exported to a CSV file,
- statistics about viewed authors in this app are collected in SQL database,
- statistics can be read via Admin Panel,
- statistics are also available via API:
  - all authors: .../api/authors/
  - first x authors: .../api/authors/?limit=x/
  - specific author by name and surname: .../api/author/Name%20Surname/

\
__Example screenshots:__

* Webapp:

![image](https://user-images.githubusercontent.com/76916353/187300349-0b0afc0a-b928-464d-b20c-42af92ed6c71.png)

* Admin Panel:

![image](https://user-images.githubusercontent.com/76916353/188738546-ba1e3e4a-ff18-4264-aac7-c98c2a2ce9a6.png)

* API results using Postman for http://127.0.0.1:8000/api/authors/

![image](https://user-images.githubusercontent.com/76916353/188307388-f1c865c8-3325-4a45-b5f0-46b46a65aab7.png)

* API results using Postman for http://127.0.0.1:8000/api/authors/?limit=3/

![image](https://user-images.githubusercontent.com/76916353/188307729-a7180e8d-4856-437d-bb2f-9e28d730c945.png)

* API results using Postman for http://127.0.0.1:8000/api/author/Paulo%20Coelho/

![image](https://user-images.githubusercontent.com/76916353/188307652-3817d5f5-7b7c-4ba5-b346-79eeaee7da20.png)
