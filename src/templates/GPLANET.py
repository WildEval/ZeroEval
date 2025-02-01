# GPLANET Template

GPLANET = """**Task Description:** You are required to complete a simple task within a room.


**Instructions:**
1. **Examine the objects in the room:** Review the list of objects provided below. Each object includes attributes such as id, object_type, position, rotation, and parent_receptacle.
2. **Understand the task:** Carefully read the task description to determine what needs to be accomplished.
3. **Analyze the candidate actions:** A set of candidate actions is provided. **There are exactly ***two*** actions that do not need to appear in the final sequence.** These irrelevant actions should be ignored.
4. **Select and order the actions:** Identify the correct actions needed to complete the task and arrange them in the proper sequence.
5. **Provide your answer:** You are allowed to include your reasoning process, but **after giving the answer sequence, you should end the generation**. Your final answer must start with ### and end with END, formatted like ### (A) (B) (C) END.


**Objects in the room:**
[
    {
        "id": "0",
        "object_type": "Agent",
        "position_x": "1.25",
        "position_y": "0.900",
        "position_z": "0.5",
        "rotation_x": "0",
        "rotation_y": "0",
        "rotation_z": "0",
        "parent_receptacle": ""
    },
    {
        "id": "8",
        "object_type": "Watch",
        "position_x": "-0.862",
        "position_y": "0.552",
        "position_z": "-0.192",
        "rotation_x": "0",
        "rotation_y": "270",
        "rotation_z": "0",
        "parent_receptacle": "30"
    },
    {
        "id": "30",
        "object_type": "CoffeeTable",
        "position_x": "-0.711",
        "position_y": "0.002",
        "position_z": "-0.364",
        "rotation_x": "0",
        "rotation_y": "180",
        "rotation_z": "0",
        "parent_receptacle": ""
    },
    {
        "id": "36",
        "object_type": "SideTable",
        "position_x": "1.807",
        "position_y": "0.000",
        "position_z": "0.326",
        "rotation_x": "0",
        "rotation_y": "270",
        "rotation_z": "0",
        "parent_receptacle": ""
    },
    {
        "id": "14",
        "object_type": "Statue",
        "position_x": "1.807",
        "position_y": "0.880",
        "position_z": "0.537",
        "rotation_x": "0",
        "rotation_y": "270",
        "rotation_z": "0",
        "parent_receptacle": "36"
    },
    {
        "id": "15",
        "object_type": "Statue",
        "position_x": "1.682",
        "position_y": "0.880",
        "position_z": "0.220",
        "rotation_x": "0",
        "rotation_y": "90",
        "rotation_z": "0",
        "parent_receptacle": "36"
    }
]


**Task Instruction:**
Move the wristwatch from the coffee table to the dresser.


**Candidate Actions:**
(A) Turn right and walk towards the bookshelf.
(B) Put the wristwatch down on the dresser to the right of the grey statue.
(C) Pick up a book from the coffee table.
(D) Turn left and walk to the dresser with statues on it.
(E) Pick up the wristwatch from the coffee table.
(F) Turn left and walk to the coffee table.


**Assistant's Response:**


To move the wristwatch from the coffee table to the dresser, perform the following actions:


1. **Turn left and walk to the coffee table.** (Action F)
2. **Pick up the wristwatch from the coffee table.** (Action E)
3. **Turn left and walk to the dresser with statues on it.** (Action D)
4. **Put the wristwatch down on the dresser to the right of the grey statue.** (Action B)


The irrelevant actions are:


- (A) Turn right and walk towards the bookshelf.
- (C) Pick up a book from the coffee table.


### (F) (E) (D) (B) END


**Objects in the room:**
{objects_str}


**Task Instruction:**
{task}


**Candidate Actions:**
{actions}
"""
