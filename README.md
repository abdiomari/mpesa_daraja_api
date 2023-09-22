This is Safaricom's Daraja API: a simple way to integrate Mpesa payments online.

**Introduction**

This project explores how to use the Mpesa Daraja API using Python and the Django framework to develop a simple payment platform. The Mpesa Daraja API is a RESTful API that allows developers to interact with the Mpesa mobile money service in Kenya.

**Mpesa API**

The Mpesa API provides a variety of endpoints for performing different tasks, such as:

* **Lipa Na Mpesa Online (STK Push)**: This endpoint allows developers to initiate a payment request from a customer's phone. The customer will then receive a prompt to enter their Mpesa PIN to authorize the payment.
* **B2C Payment**: This endpoint allows developers to make payments from their business Mpesa account to a customer's personal Mpesa account.
* **C2B Payment**: This endpoint allows developers to receive payments from a customer's personal Mpesa account to their business Mpesa account.
* **Balance Inquiry**: This endpoint allows developers to check the balance of an Mpesa account.
* **Transaction Status**: This endpoint allows developers to check the status of an Mpesa transaction.

**How the Mpesa API works**

To use the Mpesa API, developers must first register for an Mpesa developer account. Once they have an account, they will be able to generate a consumer key and consumer secret. These credentials are required to authenticate all requests to the Mpesa API.

Once a developer has authenticated their request, they can then call the appropriate API endpoint to perform the desired task. For example, to initiate a Lipa Na Mpesa Online payment, the developer would call the `/stkpush/v1/processrequest` endpoint.

The Mpesa API will then return a response to the developer. The response will contain the status of the request, as well as any other relevant information, such as the transaction ID.

**Developing a simple payment platform with Python and Django**



1. Create a new Django project.
2. Install the `mpesa` Django package.
3. Create a new Django app for the payment platform.
4. Add the `mpesa` app to the `INSTALLED_APPS` setting in the project's `settings.py` file.
5. Create a view that will handle payment requests.
6. In the view, use the `mpesa` package to initiate a Lipa Na Mpesa Online payment request.
7. Once the payment request has been initiated, redirect the user to the Mpesa website to complete the payment.
8. Once the payment has been completed, Mpesa will redirect the user back to the payment platform website.
9. In the payment platform website, check the status of the payment using the `mpesa` package.
10. If the payment was successful, update the payment status in the database and display a success message to the user.
11. If the payment was unsuccessful, display an error message to the user.

**Conclusion**
To run a Django app from GitHub, you can follow these steps:

1. Clone the GitHub repository to your local machine.
2. Create a virtual environment.
3. Activate the virtual environment.
4. Install the requirements.txt file.
5. Migrate the database.
6. Run the Django development server.

Here are the steps in more detail:

1. **Clone the GitHub repository to your local machine.**

```
git clone https://github.com/<username>/<repository>.git
```

2. **Create a virtual environment.**

```
python3 -m venv .venv
```

3. **Activate the virtual environment.**

```
source .venv/bin/activate
```

4. **Install the requirements.txt file.**

```
pip install -r requirements.txt
```

5. **Migrate the database.**

```
python manage.py migrate
```

6. **Run the Django development server.**

```
python manage.py runserver
```

Once you have run the Django development server, you can access your Django app at `http://localhost:8000` in your web browser.

**Additional tips:**

* If you are using a code editor such as Visual Studio Code, you can use the built-in terminal to run the above commands.
* If you are using a cloud-based IDE such as GitHub Codespaces, you can run the above commands in the terminal window.
* If you are using a production server, you will need to deploy your Django app to the server before you can run it.
