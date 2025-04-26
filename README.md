<h1 align="center">

<img src="https://img.shields.io/static/v1?label=PORTAL%20DAS%20BANDAS&message=Discover%20Music&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center">Portal das Bandas - Discover New Music</p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>
-----
<p> The objective of this project is to provide a personalized music discovery experience. Users can input their favorite band or artist, and the system will suggest similar bands, generate a custom playlist, provide a "nerd" travel comparing artists to Marvel or Star Wars characters, and even create fictional album covers. The tool uses Groq's API for natural language generation and external search tools for YouTube and Google Images.</p>

>> <h3> Glossary </h3>

Fields	                                                  | Type       |    Description                                         |
----------------------------------------------------------|:----------:|:------------------------------------------------------:|
`banda`                                                     | string     | Name of the favorite band or artist                    |
`opiniao`                                                   | string     | Generated opinion about the band                       |
`sugestoes`                                                | string     | List of similar bands and their styles                 |
`playlist`                                                 | list       | Generated playlist with song names and YouTube links    |
`viagem`                                                   | string     | "Nerdy" travel comparison (e.g. Marvel or Star Wars)    |
`descricao_capa`                                           | string     | Fictional album cover description generated            |
`link_imagens`                                             | string     | Link for Google Images to visualize band-inspired art  |

---

>> <h3> Technologies </h3>
-----
- [Streamlit](https://streamlit.io/) - Framework for building interactive Python apps.
- [Groq API](https://groq.com/) - LLaMA models for text generation.
- [Requests](https://docs.python-requests.org/en/latest/) - HTTP requests for Groq API and external searches.
- [Google Images](https://images.google.com/) - Searching for band-related images.
- [YouTube Search](https://www.youtube.com/results) - Generating playlist links to YouTube videos.

---

>> <h3> How to Run the Project Locally </h3>
-----
1. Clone the repository:
   ```bash
   git clone https://github.com/batestin1/agente_portal_bandas.git
   cd agente_portal_bandas
   ```
----
2. To create a environment:
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
----

3. Install dependencies:
    ```pip install -r requirements.txt ```
--- 
4. Run the app
    ``` streamlit run main.py ``` 

