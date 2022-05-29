from database import topic_dict


def update_topic():
    while True:
        try:
            option = input('''
     __________________________
    |                          |
    |          UPDATE          |
    |                          |
    |  1- List Topics          |
    |  2- Update Title         |
    |  3- Update Description   |
    |  4- Update Subject       |
    |  5- Return               |
    |__________________________|

>>> ''')
            match option:
                case "1":
                    try:
                        if topic_dict:
                            for topic in topic_dict:
                                print(f"{topic_dict[topic].name} - {topic_dict[topic].subject}")
                    except:
                        print("There are no topics registered!")
                case "2":
                    try:
                        topic = input("Enter topic title: ")
                        topic = topic_dict[topic]
                        new_name = input("Enter new topic title: ")
                        topic.name = new_name
                        print(f"New title {topic.name} successfully applied!")
                    except:
                        print("Topic not found!")
                case "3":
                    try:
                        topic = input("Enter topic title: ")
                        topic = topic_dict[topic]
                        new_description = input("Enter new description: ")
                        topic.description = new_description
                        print(f"New description {topic.name} successfully applied!")
                    except:
                        print("Topic not found!")
                case "4":
                    try:
                        topic = input("Enter topic title: ")
                        topic = topic_dict[topic]
                        new_subject = input("Enter new subject: ")
                        topic.subject = new_subject
                        print(f"New subject {topic.name} successfully applied!")
                    except:
                        print("Topic not found!")
                case "5":
                    break
                case _:
                    print("Please enter a valid option!")
        except:
            print("\nPlease enter a valid option")
