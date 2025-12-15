from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "chemistry": {
                "name": "Combustion Club",
                "description": "Handles the explosives and other chemical-based reactions in fireworks. Please do not laugh at the data.",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Room 8-D",
                "advisor": "Ms. Andry",
                "members": 69,
                "category": "Academic"
            },
            "physics": {
                "name": "Physics Club",
                "description": "For students good at projectile motion. Will focus on calculating firework trajectories.",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "Courtyard",
                "advisor": "Mr. Inferno",
                "members": 47,
                "category": "Academic"
            },
            "engineering": {
                "name": "Engineering Club",
                "description": "This club focuses on building the fireworks, launchers, and control panels.",
                "meeting_time": "Every Tuesday 3:45-5:30 PM",
                "location": "Rooftop",
                "advisor": "Mr. Ramirez",
                "members": 80,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "Plan and create whatever design you can think of, then blow it up and watch it paint the skies!",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Fireproofed Art Room",
                "advisor": "Ms. Alotaya",
                "members": 39,
                "category": "Arts"
            }
        }
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """

    display(output, target="club-info")

