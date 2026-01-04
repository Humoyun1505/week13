import requests


def get_users(count):
    url = "https://randomuser.me/api/"
    params = {"results": count}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["results"]
    except requests.exceptions.RequestException:
        print("Error fetching user data.")
        return []


def display_users(users):
    if not users:
        print("No users found.")
        return

    print("\n Random Users\n")

    for user in users:
        name = user["name"]["first"] + " " + user["name"]["last"]
        email = user["email"]
        country = user["location"]["country"]

        print("Name:", name)
        print("Email:", email)
        print("Country:", country)
        print()


def save_to_file(users):
    file = open("users_results.txt", "w")

    for user in users:
        name = user["name"]["first"] + " " + user["name"]["last"]
        country = user["location"]["country"]
        file.write(name + " - " + country + "\n")

    file.close()


def main():
    try:
        count = int(input("How many users to display?: "))
    except ValueError:
        print(" Please enter a number.")
        return

    users = get_users(count)
    display_users(users)
    save_to_file(users)

    print(" Results saved to users_results.txt")


main()
