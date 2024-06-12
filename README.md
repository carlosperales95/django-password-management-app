# Django-password-manager-with-authentication
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Django Password Manager</h3>

  <p align="center">
    An awesome simple Python + Django project that makes your life more secure!
    <br />
    <br />
    <a href="">View Demo</a>
    ·
    <a href="https://github.com/carlosperales95/django-password-management-app/issues">Report Bug</a>
    ·
    <a href="https://github.com/carlosperales95/django-password-management-app/issues/">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

PROJECT DESCRIPTION

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![SQLite][SQLite]][SQLite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Make sure that the following requirements are satified before starting with the setup process
* python3
* pip

### Installation

_The below might vary depending on the specific OS you are using. Please note that the pre-existing scripts are only valid for Unix based OS (e.g. Linux, Mac)_

1. Clone the repo
   ```sh
   git clone https://github.com/carlosperales95/django-password-management-app.git
   ```
2. Move into the project folder
   ```sh
   cd django-password-management-app/
   ```
3. Set your environment variables

> [!CAUTION]  
> All steps are quite simple until this point. Depending on your lazyness (and trust), there is a scripted way and a manual way to proceed from this point on.
> Please follow the steps for the way you prefer.

<details> 
 <summary><h2>Scripted way</h2></summary>
 
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
 <summary><h2>Manual way</h2></summary>
 
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

> [!IMPORTANT]  
> When the application will no longer be in use (`Ctrl/Cmd + C`), always remember to deactivate the virtual environment:
>   ```sh
>    deactivate
>   ```

Now the server should be up and running, and visible at ![localhost](http://127.0.0.1:8000) !

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

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
