Pokémon Battle Project

Features

- Pokémon Battle: Initiate battles between two Pokémon based on their attack stats and type advantages.
- Asynchronous Task Processing: Uses Celery and Redis to handle battle simulations in the background.

Installation

Prerequisites

- Python 3.8 or higher
- Docker (for containerization -> not mandatory)

Setup

1. Clone the Repository

   git clone https://github.com/Nishant20231667/pokemon_battle.git
   use development branch


2. Create a Virtual Environment

3. Install Dependencies

   pip install -r requirements.txt

4. Apply Migrations

   python manage.py makemigrations
   python manage.py migrate

6. Run the Server

   python manage.py runserver

7. Start Celery Worker

   Open a new terminal window and run:

   celery -A pokemon_battle worker --loglevel=info

API Endpoints CURL (use the port being used)

1. API 1 -> for listing of pokemon
- curl --location 'http://127.0.0.1:9068/api/pokemon/?page=3'

2. API 2 -> to start battle
- curl --location 'http://127.0.0.1:9068/api/battle/' \
    --header 'Content-Type: application/json' \
    --data '{
        "pokemon_a": "Wartortle",
        "pokemon_b": "Kakuna"
    }'

3. API 3 -> to get battle status
- curl --location 'http://127.0.0.1:9068/api/battle_status/' \
    --header 'Content-Type: application/json' \
    --data '{
        "battle_id": "c6be9dd6-5414-48e6-b67e-03a5dc5be65d"
    }'

Docker

To containerize the application using Docker, follow these steps:

1. Build the Docker

   docker compose up -d --build
