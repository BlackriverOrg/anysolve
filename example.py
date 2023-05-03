import os
from anysolve import AnySolve

client = AnySolve(os.environ.get("ANYSOLVE_API_KEY"))

result = client.run(
    "intern-translation-free",
    "1.0.0",
    {
        "source_language": "de",
        "text": "Das ist ein rotes Haus.",
        "target_language": "en",
    },
)

print(result)
