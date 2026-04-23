# Another example for you with files :

src /
├── contexts /
│   ├── billing /
│   │   ├── domain /
│   │   │   ├── entities /
│   │   │   ├── value_objects /
│   │   │   ├── repositories /
│   │   │   └── services /
│   │   │
│   │   ├── application /
│   │   │   ├── use_cases /
│   │   │   ├── commands /
│   │   │   ├── queries /
│   │   │   └── dtos /
│   │   │
│   │   ├── infrastructure /
│   │   │   ├── persistence /
│   │   │   ├── external_services /
│   │   │   └── config /
│   │   │
│   │   └── api /
│   │       ├── routers /
│   │       └── schemas /
│   │
│   ├── orders /
│   │   ├── domain /
│   │   │   ├── entities /
│   │   │   ├── value_objects /
│   │   │   ├── repositories /
│   │   │   └── services /
│   │   │
│   │   ├── application /
│   │   │   ├── use_cases /
│   │   │   ├── commands /
│   │   │   ├── queries /
│   │   │   └── dtos /
│   │   │
│   │   ├── infrastructure /
│   │   │   ├── persistence /
│   │   │   ├── external_services /
│   │   │   └── config /
│   │   │
│   │   └── api /
│   │       ├── routers /
│   │       └── schemas /
│
├── shared /
│   ├── kernel /
│   │   ├── base_entity.py
│   │   ├── value_object.py
│   │   └── aggregate_root.py
│   │
│   ├── exceptions /
│   │   └── domain_exceptions.py
│   │
│   └── utils /
│       └── helpers.py
│
├── infrastructure /
│   ├── database /
│   │   ├── connection.py
│   │   └── session.py
│   │
│   ├── messaging /
│   │   └── broker.py
│   │
│   └── config /
│       └── settings.py
│
├── api /
│   ├── routers /
│   │   └── main_router.py
│   │
│   ├── dependencies /
│   │   └── container.py
│   │
│   └── middlewares /
│       └── error_handler.py
│
├── main.py
