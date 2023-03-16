# Smart Parking System

#### Description
The main design and development of a parking management system, including vehicle management and billing management two parts.
1. Entry time of vehicles shall be recorded while exit time of vehicles shall be calculated.
2. Long-term card vehicles pay an annual or monthly fee. Calculate and pay the parking fee when the temporary vehicle comes out.
3. Parking management, real-time display of the total number and status of parking Spaces, the number of idle parking Spaces.
4. Parking fee inquiry and statistics.
5. Incoming vehicles and time will be generated randomly.
6. Package List：
Flask
Flask-Bootstrap
Flask-SQLAlchemy
Flask-Script
Flask-WTF
Jinja2
Markdown
MarkupSafe
PyMysQL
PyYAMLSQLAlchemy
WTForms
Werkzeug
#### Software Architecture
The backend architecture description
- code
  - controller   <!--Basic Method of Database-->
    - __init__.py
    - carsController.py
    - parkingController.py
  - models      <!--Database Object-->
    - __init__.py
    - cars.py
    - parking.py
  - service     <!--Database Operation Method-->
    - __init__.py
    - service
  - __init__.py
- config        <!--Configuration File-->
  - config.py
  - __init__.py
- utils         <!--Common Methods-->

The frontend architecture description



