from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app):
    origins = [
        "https://fakenewscombat.com",
        "https://www.fakenewscombat.com",
        "https://fake-news-combat-agency.onrender.com/healthz",
        "https://fakenewscombat.com/anime-building",
        "http://localhost:4200",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",

    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
