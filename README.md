# FastApi Introduction  
## Descrição do Projeto
   TODO: FastApi introduction using SqlAlchemy, Alembic, Pydantic and JWT.

# Introduction 

Embrace the Future of Web Development with FastAPI!

In the ever-evolving landscape of web development, staying ahead of the curve is not just an advantage; it's a necessity. Welcome to the world of FastAPI – the cutting-edge web framework that redefines how we build APIs and web applications.

Imagine a framework that seamlessly combines speed, simplicity, and scalability. FastAPI does exactly that, and more. It's not just another framework; it's a paradigm shift. With its intuitive design and automatic documentation capabilities, FastAPI empowers developers to create robust APIs and web applications with unprecedented ease and efficiency.

Why FastAPI?

Speed: FastAPI lives up to its name. It's one of the fastest Python frameworks out there, making it ideal for high-performance applications where every millisecond counts.

Type Safety: Say goodbye to runtime errors. FastAPI leverages Python type hints to provide real-time feedback and catch errors before they become issues, ensuring your code is as reliable as possible.

Automatic Documentation: Documentation is often an afterthought, but not with FastAPI. It automatically generates interactive API documentation, making collaboration between developers, testers, and stakeholders a breeze.

Asynchronous Support: Modern applications demand asynchronous programming. FastAPI embraces asynchronous programming, allowing you to write efficient, non-blocking code for seamless user experiences.

Simplicity: FastAPI's intuitive syntax and easy-to-understand concepts reduce the learning curve, enabling both beginners and seasoned developers to dive in and start building powerful applications quickly.

Your Journey Begins Here!

Embarking on a FastAPI project isn't just about writing code; it's about embracing a mindset. It's about pushing boundaries, exploring new possibilities, and creating solutions that make a difference. Whether you're a seasoned developer looking to optimize your workflow or a newcomer eager to learn, FastAPI welcomes you.

Let's transform your ideas into reality, one endpoint at a time. Get ready to revolutionize the way you think about web development. FastAPI is not just a framework; it's a catalyst for innovation.

Are you ready to embark on this exciting journey? Fasten your seatbelt and let's build the future of web development together!

Happy coding! 🚀

# Getting Started
TODO: Guidance on how to upload the project:

1. Installation process
   1. Create your environment variables according to .env file.
   2. Installation by container:
      1. See next chapter for system dependencies.
      2. After installing the dependencies, run the command.
         1. `docker-compose` up or `docker-compose up -d`.
   3. Depedences manual install:
      1. In begin project set commands:
         1. pip install fastapi
         2. pip install uvicorn
         3. pip install alembic
         4. pip install SQLAlchemy-Utils
         5. pip install fastapi-jwt-auth
         6. pip install redis
         7. pip install asyncpg
         8.  pip install pydantic[email]
      2. Commands executions:
         1. Upgrade SqlAlchemy version to actual
         2. alembic init -t async migrations 
   4. Install locally:
      1. See next chapter for system dependencies.
      2. Create your virtual env.
         1. [Click here to tutorial access ](https://blog.debugeverything.com/pt/ambientes-virtuais-com-python-virtualenv/)
      3. Install project requirements with commands.
         1. To create requirements file use this command `pip freeze > requirements.txt`
         2. `pip install -r requirements.txt` ou `pip3 install -r requirements.txt`.
      4. Running migrations.
         1. `alembic upgrade head` -> to create and feed the tables with initial data.
         2. `alembic revision --autogenerate -m "name migration"` -> to create a new migration.
         3. For more information read the readme inside migrations in this [site](https://alembic.sqlalchemy.org/en/latest/tutorial.html).
      5. Start the project
         1. `python main.py` or `python3 main.py`
      
# Software dependencies
   TODO: Before carrying out the installation, it is necessary to have the following software installed on your machine.

   1. Install locally:
      1. [Postgres](https://www.postgresql.org/)
      2. [Redis](https://redis.io/)
      3. Python >= 3.82. Software dependencies 

   2. Installation by container:  
      1. `Docker`
      2. `Docker-Compose`
         1. This for install container in development ambient


# Documentation
1. [FastAPI](https://fastapi.tiangolo.com/pt/)
2. [FastAPI JWT Auth](https://indominusbyte.github.io/fastapi-jwt-auth/)
3. [FastAPI Mail](https://sabuhish.github.io/fastapi-mail/)
4. [FastAPI Async Tests](https://fastapi.tiangolo.com/advanced/async-tests/)
5. [SqlAlchemy](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
6. [SqlAlchemy Utils](https://sqlalchemy-utils.readthedocs.io/en/latest/)
7. [Pydantic](https://pydantic-docs.helpmanual.io/)
8. [Alembic](https://alembic.sqlalchemy.org/en/latest/)
