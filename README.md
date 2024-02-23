# FUNDSROOM_PROJECT_

**What is the problem?** 
The problem lies in the inefficiencies of the current food delivery system, where orders are dispatched individually without considering the geographic proximity of customers and customers consent if they are willing to go for group delivery.<br><br>
**Who is experiencing it?** 
Users face longer wait times for their orders, resulting in a less satisfactory experience whereas delivery personnel navigate suboptimal routes, affecting their efficiency and potentially leading to delays.Users will also have option for group delivery or individual delivery also for group delivery user will get discount as compared to the individual delivery.<br><br>
**How will you solve it?**
The proposed solution utilizes geospatial technology to identify customers in the same neighborhood and strategically assigns a common delivery person for their orders if the order gets placed in 15 mins with the customer's consent.<br><br>
**Why is your solution better?**
This project offers a systematic approach to neighborhood-based delivery, providing a more efficient and quicker service with customer's consent and time constraint of 15 mins. By consolidating orders in the same area, it minimizes travel times for delivery personnel, resulting in cost savings and reduced environmental impact.<br><br>

**Main Objectives of the Project:**
The project aims to enhance our food delivery app by introducing a geographically optimized functionality. The project leverages geospatial technology to identify and group customers in the same neighbourhood, assigning a common delivery person for their orders.
Project Objectives:<br><br>
1)	Optimize Delivery Operations: Implement a system that strategically groups orders in the same geographic area with the user’s choice minimizing travel distances for delivery personnel and optimizing overall delivery operations.<br><br>
2)	Enhance Customer Satisfaction: Improve the customer experience by offering more efficient and quicker deliveries, and implementing a discount mechanism for orders experiencing delays, demonstrating a commitment to customer satisfaction.<br><br>
3)	Competitive Advantage: Position our food delivery app as a leader in the industry by introducing a unique and innovative feature that sets us apart from competitors, contributing to increased market share and user loyalty.<br><br>
4)	Operational Efficiency: Streamline delivery processes, reduce operational costs, and ensure a smooth integration of the project functionality with our existing technology infrastructure, enhancing overall operational efficiency.<br><br>

**Requirements:**
Version >= 2.0.0 of django-pagedown requires Django 2.1.0 or above (previous versions should support Django all the way back to around 1.1).<br><br>

**Install and run:**
Get the code:
pip install django
pip install psycopg2
cd swiggy1
python manage.py makemigrations
python manage.py makemigrate
python manage.py runserver
-->starting the development server on port 8000

POSTMAN:
To create user:
POST : http://127.0.0.1:8000/user/create/

To create Restaurant:
POST : http://127.0.0.1:8000/restaurant/create/

To create New order:
POST : http://127.0.0.1:8000/neworder/create2/

To fetch group orders for delivery partners:<br><br>
GET: http://127.0.0.1:8000/partner/orders/<int:restaurant_id>/

**I have maintained referential integrity between the userprofile,restaurant and neworder app.**
It means that without Restaurant id or user id user cannot place order.


