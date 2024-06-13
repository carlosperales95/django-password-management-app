<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/carlosperales95/sekurata-django">
    <img src="https://github.com/carlosperales95/sekurata-django/assets/8956411/f1dbbfab-b07f-4f86-8f4a-920ff0ec1697" alt="Logo" width="80" height="80">
  </a>
  <img src="https://github.com/carlosperales95/sekurata-django/assets/8956411/04414894-58e8-4e78-9b92-53d2b62e89a1" alt="appName" width="auto" height="auto">
  <p align="center">
    An awesome simple Python + Django project that makes your life more secure
    <br />
<!--     <br />
    <a href="">View Demo</a>
    · -->
    <a href="https://github.com/carlosperales95/sekurata-django/issues">Report Bug</a>
    ·
    <a href="https://github.com/carlosperales95/sekurata-django/issues/">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <br />
  <ol>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>
<br />


## Built With

[![Python][Python]][Python-url]
[![Django][Django]][Django-url]
[![SQLite][SQLite]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ABOUT THE PROJECT -->
## About The Project
![photo-collage png](https://github.com/carlosperales95/sekurata-django/assets/8956411/e7302035-9ec7-4332-85b2-753c8e03584a)

This Password Manager is a secure and efficient application built using Python and Django. Designed for individuals who prefer to avoid cloud-based services due to security concerns, this app offers robust password management functionality, entirely on your local machine. By running the application locally, users can eliminate the risks associated with cloud service breaches, ensuring their sensitive information remains private and secure.

<br />

### Key Features:
  * **Local Hosting:** The application runs on your local machine, negating the need for cloud storage and minimizing exposure to potential online threats.
  * **User Authentication:** Access to the app is protected by a user login system, ensuring only you can view and manage your passwords.
  * **Password Encryption:** All stored passwords are securely encrypted, providing an additional layer of security.
  * **Password dice:** The app includes a feature to generate strong, random passwords instantly.
  * **User-Friendly Interface:** Designed with simplicity in mind, the app offers an intuitive interface for easy password management.

<br />

### Benefits:
  * **One Password:** You will only only need to remember a single master password to access the app, reducing the need to be remembering multiple passwords.
  * **No more duplicates:** Thanks to the password dice, you no longer need to come up with your own passwords. Our app allows you to set your own password if you wish so, but thanks to the password dice, you can generate unique and secure passwords instantly. This avoids password duplicates, and ensures you always use strong and secure passwords without the hassle of creating them.
  * **Enhanced Security:** By keeping passwords stored locally and encrypted, users are protected from potential breaches common in cloud-based services.
  * **Control and Privacy:** You have full control over your password data, with no dependency on third-party services.
  * **Convenience:** Simplifies the process of generating and storing complex passwords, making it easier to maintain strong security practices.
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Below you can find the instructions on setting up this project locally.
To get a local copy up and running follow these steps.

### Prerequisites

Make sure that the following requirements are satified before starting with the setup process:
* python3
* pip
<br />

### Installation

> [!CAUTION]  
> _The below might vary depending on the specific OS you are using.
> Please note that the pre-existing scripts are only valid for Unix based OS (e.g. Linux, Mac)_

1. Clone the repo
   ```sh
   git clone https://github.com/carlosperales95/sekurata-django
   ```
2. Move into the project folder
   ```sh
   cd sekurata-django
   ```
3. Copy the `.env.example` file as `.env` in the same folder (main project folder)

4. Set the values for `SECRET_KEY` and `ENCRYPT_KEY`. `SECRET_KEY` is your personal Django key, which you can generate using your console (if you are tech savvy), or simply in a site like [Djecrety][Djecrety-url]. `ENCRYPT_KEY` is your personal Fernet encryption key, which you can generate using your console (if you are tech savvy), or simply in a site like [Fernet Key Generator][Fernet-keygen-url]
  ```.env
  SECRET_KEY = <YOUR_SECRET_KEY_VALUE>
  ENCRYPT_KEY = <YOUR_SECRET_KEY_VALUE>
  ```
  > [!WARNING]  
  > If you ever fork or reupload this project, please never upload these keys to a public repository.
  > People otherwise will know your keys!
  > Also avoid uploading other sensitive stuff like your sqlite3 DB file  


<br />

> [!TIP]  
> All steps are quite simple until this point. Depending on your lazyness (and trust), there is a scripted way and a manual way to proceed from this point on.
> Please follow the steps for the way you prefer.

<details> 
 <summary><h2>Scripted Setup</h2></summary>
 
1. Give permissions to the script files
   ```sh
   chmod +x setup.sh
   chmod +x start.sh
   ```
2. Run `setup.sh`. This creates the virtual environment and installs all requirements
   ```sh
   ./setup.sh
   ```
   
4. Run `start.sh`. This migrates the database and starts the application
   ```sh
   ./start.sh
   ```
</details>


<details> 
 <summary><h2>Manual Setup</h2></summary>
 
1. Create virtual environment and `pip` install requirements
   ```sh
    python3 -m venv pass_manage_venv
    source pass_manage_venv/bin/activate
    pip3 install -r ./requirements.txt
   ```
2. Run migrations and start application
   ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
   ```
</details>

Now the server should be up and running, and visible at [localhost](http://127.0.0.1:8000) !
<br />

### Create Django Admin User
Django admin gives you access to the admin panel in `localhost/admin`, really useful if you want to have more visibility. In order to create an admin user, the Django command would be as follows:
```sh
py manage.py createsuperuser
```
<br />


> [!IMPORTANT]  
> When the application will no longer be in use (`Ctrl/Cmd + C`), always remember to deactivate the virtual environment:
>   ```sh
>    deactivate
>   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<br />


<!-- USAGE EXAMPLES -->
## Usage
![image](https://github.com/carlosperales95/sekurata-django/assets/8956411/7797f63a-2603-4bca-bb42-a5fa31cf86c5)
![](https://github.com/carlosperales95/sekurata-django/assets/8956411/e65d5673-0d24-470e-b062-82fcb0650481)
![image](https://github.com/carlosperales95/sekurata-django/assets/8956411/2a2d8ee6-57b8-4a91-aa04-74cd5213df2f)
![image](https://github.com/carlosperales95/sekurata-django/assets/8956411/2280b08e-82b1-49f4-9219-ad1590e967c8)
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[SQLite]: https://img.shields.io/badge/SQLite-05678F?style=for-the-badge&logo=sqlite&logoColor=white
[Python-url]: https://www.python.org/
[Django-url]: https://www.djangoproject.com/
[SQLite-url]: https://sqlite.org/
[Djecrety-url]: https://djecrety.ir/
[Fernet-keygen-url]: https://fernetkeygen.com/
