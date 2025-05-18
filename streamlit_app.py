import streamlit as st
import pandas as pd


st.sidebar.title("Sommaire")
st.sidebar.markdown("""
- [À propos](#a-propos)
- [Compétences](#competences)
- [Portfolio](#portfolio)
- [Formation](#formation)
- [Bénévolat](#benevolat)
- [Langues](#langues)
- [Veille et projets](#veille-et-projets)
""", unsafe_allow_html=True)

# Header
st.title("Fetra RAMANANTSOA")
st.subheader("Développeur Backend")

# About
st.header("À propos")
st.write(
    "Développeur backend passionné, spécialisé dans la conception d’API, l’intégration de services cloud, "
    "et l’architecture de solutions robustes. Expérience sur de nombreux projets dans des secteurs variés."
)

# Skills as table without index
st.header("Compétences")
skills = {
    "Langages": "TypeScript, JavaScript, Python",
    "Frameworks / CMS / APIs": "NestJS, Flask, FastAPI",
    "Serveurs web": "Node.js, Gunicorn, Uvicorn",
    "Bases de données": "PostgreSQL, MySQL, MongoDB",
    "Tests": "Jest, PyTest",
    "Versioning": "Git, SVN",
    "CI/CD": "Gitlab CI, Jenkins",
    "Méthodologies": "Scrum, Kanban",
    "IDE": "VSCode, WebStorm, PyCharm",
    "OS": "Debian, Ubuntu, Manjaro, Windows 10"
}
skills_df = pd.DataFrame(list(skills.items()), columns=["Catégorie", "Compétences"])
st.dataframe(skills_df, hide_index=True)

# Experience
st.header("Portfolio")
experiences = [
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Janvier 2024 - Septembre 2024",
        "projet": "IA interne pour collaborateurs",
        "secteur": "Technologies de l'information",
        "stack": ["GCP", "Docker", "Ollama", "Open WebUI"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Avril 2024 - Septembre 2024",
        "projet": "App mobile pour infirmiers",
        "secteur": "Médical",
        "stack": ["Typescript", "Jenkins", "NestJS", "Prisma", "PostgreSQL", "Stripe"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Juillet 2023 - Décembre 2023",
        "projet": "Services LLM",
        "secteur": "Médical",
        "stack": ["Python", "FastAPI", "Langchain", "OpenAI", "AWS"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Janvier 2023 - Juin 2023",
        "projet": "Création plateforme e-commerce",
        "secteur": "Quincaillerie",
        "stack": ["NodeJS", "MongoDB", "MySQL", "Terraform", "AWS"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Juillet 2022 - Décembre 2022",
        "projet": "Maintenance plateforme e-commerce",
        "secteur": "Quincaillerie",
        "stack": ["NodeJS", "MongoDB", "MySQL", "Terraform", "AWS"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Février 2022 - Juin 2022",
        "projet": "Maintenance plateforme de recensement gouvernemental",
        "secteur": "Gouvernemental",
        "stack": ["Typescript", "NestJS", "Prisma", "PostgreSQL"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Janvier 2022",
        "projet": "Recensement de sinistrés du cyclone",
        "secteur": "Gouvernemental",
        "stack": ["Java", "Spring", "PostgreSQL"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Septembre 2020 - Décembre 2021",
        "projet": "Plateforme de marketing télécom",
        "secteur": "Télécommunications",
        "stack": ["Java", "Quarkus", "MongoDB", "PostgreSQL"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Octobre 2019 - Août 2020",
        "projet": "Réseau social sportif",
        "secteur": "Sportif",
        "stack": ["Flask", "Python", "MongoDB", "Firebase", "Paypal API"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Novembre 2018 - Septembre 2019",
        "projet": "Plateforme de matchmaking",
        "secteur": "Divertissements",
        "stack": ["PHP", "Symfony", "MySQL", "LDAP", "Openfire", "Neo4J", "Elasticsearch"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Août 2018 - Octobre 2018",
        "projet": "Plateforme e-commerce",
        "secteur": "Sécurité",
        "stack": ["PHP", "Symfony", "AJAX", "JQuery", "MySQL", "Stripe"]
    },
    {
        "entreprise": "Etech Consulting",
        "poste": "Ingénieur Développeur",
        "dates": "Janvier 2018 - Juillet 2018",
        "projet": "Application de gestion de plantations",
        "secteur": "Industrie du tabac",
        "stack": ["PHP", "MySQL"]
    },
]
for exp in experiences:
    st.markdown(
        f"**{exp['poste']}** chez *{exp['entreprise']}* ({exp['dates']})  \n"
        f"Projet : {exp['projet']} ({exp['secteur']})  \n"
        f"Stack : {', '.join(exp['stack'])}"
    )

# Education
st.header("Formation")
st.markdown(
    "**Master II** – Institut Supérieur Polytechnique de Madagascar (2015)  \n"
    "Spécialisation : Informatique Multimédia, Technologies de l’Information et de la Communication, Intelligence Artificielle  \n"
    "Evaluation comparative de diplômes : Diplôme d'Etudes Supérieures Spécialisées (DESS) en Génie Informatique et Construction des Ordinateurs"
)
st.markdown(
    "**Licence III** – Institut Supérieur Polytechnique de Madagascar (2013)  \n"
    "Spécialisation : Informatique Multimédia, Technologies de l’Information et de la Communication, Intelligence Artificielle  \n"
    "Evaluation comparative de diplômes : Baccalauréat (BAC) en Génie Informatique et Construction des Ordinateurs"
)

# Bénévolats
st.header("Bénévolat")
st.markdown(
    "**Membre actif** – *Montréal-Python* (2025)  \n"
    "Organisation d’événements et de meetups pour la communauté Python à Montréal.  \n"
    "- Organisation de conférences et d'ateliers  \n"
    "- Promotion de l'utilisation de Python dans divers domaines  \n"
    "- Partage de connaissances et d'expériences avec d'autres développeurs  \n"
    "- Diffusion en direct des conférences"
)

# Languages as table without index
st.header("Langues")
langues_df = pd.DataFrame([
    ["Français", "C1 (TEF Canada)"],
    ["Anglais", "C1 (IELTS)"]
], columns=["Langue", "Niveau"])
st.dataframe(langues_df, hide_index=True)

# Interests & Projects
st.header("Veille et projets")
st.markdown(
    f"- GitHub : [@f-ramanantsoa](https://github.com/f-ramanantsoa)\n"
    "- Événements : Montréal-Python\n"
    "- Veille : Stack Overflow, Slashdot"
)
