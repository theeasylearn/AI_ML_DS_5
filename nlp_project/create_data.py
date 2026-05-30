import json

def get_entity_positions(text, entity):
    start = text.find(entity)
    if start == -1:
        return None
    end = start + len(entity)
    return [start, end, "COURSE"]

TRAINING_DATA = [
    {
        "text": "Learn Python, Data Science and Web Development at The Easylearn Academy.",
        "entities": [
            get_entity_positions("Learn Python, Data Science and Web Development at The Easylearn Academy.", "Python"),
            get_entity_positions("Learn Python, Data Science and Web Development at The Easylearn Academy.", "Data Science"),
            get_entity_positions("Learn Python, Data Science and Web Development at The Easylearn Academy.", "Web Development")
        ]
    },
    {
        "text": "Our new DevOps and Kubernetes bootcamp is now enrolling.",
        "entities": [
            get_entity_positions("Our new DevOps and Kubernetes bootcamp is now enrolling.", "DevOps"),
            get_entity_positions("Our new DevOps and Kubernetes bootcamp is now enrolling.", "Kubernetes")
        ]
    },
    {
        "text": "Join our Machine Learning and Artificial Intelligence course today.",
        "entities": [
            get_entity_positions("Join our Machine Learning and Artificial Intelligence course today.", "Machine Learning"),
            get_entity_positions("Join our Machine Learning and Artificial Intelligence course today.", "Artificial Intelligence")
        ]
    },
    {
        "text": "We teach React, Node.js, Django and Flutter development.",
        "entities": [
            get_entity_positions("We teach React, Node.js, Django and Flutter development.", "React"),
            get_entity_positions("We teach React, Node.js, Django and Flutter development.", "Node.js"),
            get_entity_positions("We teach React, Node.js, Django and Flutter development.", "Django"),
            get_entity_positions("We teach React, Node.js, Django and Flutter development.", "Flutter")
        ]
    },
    {
        "text": "Excel, PowerPoint and SQL are in high demand.",
        "entities": [
            get_entity_positions("Excel, PowerPoint and SQL are in high demand.", "Excel"),
            get_entity_positions("Excel, PowerPoint and SQL are in high demand.", "PowerPoint"),
            get_entity_positions("Excel, PowerPoint and SQL are in high demand.", "SQL")
        ]
    },
    {
        "text": "Enroll in our JavaScript, TypeScript and Angular bootcamp.",
        "entities": [
            get_entity_positions("Enroll in our JavaScript, TypeScript and Angular bootcamp.", "JavaScript"),
            get_entity_positions("Enroll in our JavaScript, TypeScript and Angular bootcamp.", "TypeScript"),
            get_entity_positions("Enroll in our JavaScript, TypeScript and Angular bootcamp.", "Angular")
        ]
    },
    {
        "text": "The Full Stack Web Development program starts next month.",
        "entities": [[4, 32, "COURSE"]]
    },
    {
        "text": "Learn Digital Marketing, SEO and Social Media Marketing.",
        "entities": [
            get_entity_positions("Learn Digital Marketing, SEO and Social Media Marketing.", "Digital Marketing"),
            get_entity_positions("Learn Digital Marketing, SEO and Social Media Marketing.", "SEO"),
            get_entity_positions("Learn Digital Marketing, SEO and Social Media Marketing.", "Social Media Marketing")
        ]
    },
    {
        "text": "Our Cyber Security and Ethical Hacking course is very popular.",
        "entities": [
            get_entity_positions("Our Cyber Security and Ethical Hacking course is very popular.", "Cyber Security"),
            get_entity_positions("Our Cyber Security and Ethical Hacking course is very popular.", "Ethical Hacking")
        ]
    },
    {
        "text": "Become a Data Analyst with our comprehensive course.",
        "entities": [[11, 23, "COURSE"]]
    },
    {
        "text": "We offer AWS, Azure and Google Cloud certification training.",
        "entities": [
            get_entity_positions("We offer AWS, Azure and Google Cloud certification training.", "AWS"),
            get_entity_positions("We offer AWS, Azure and Google Cloud certification training.", "Azure"),
            get_entity_positions("We offer AWS, Azure and Google Cloud certification training.", "Google Cloud")
        ]
    }
]
with open("training_data.json", "w") as f:
    json.dump(TRAINING_DATA, f, indent=2)
print(f"Created {len(TRAINING_DATA)} good training examples")