"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append(
            {
                "id": uuid.uuid4(),
                "sent_at": sent_at,
                "sent_by": random.choice(users_ids),
                "reply_for": random.choice(
                    [
                        None,
                        (
                            random.choice([m["id"] for m in messages])
                            if messages
                            else None
                        ),
                    ],
                ),
                "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
                "text": lorem.sentence(),
            }
        )
    return messages


if __name__ == "__main__":
    print(generate_chat_history())


def user_with_most_messages(chat_history):
    dict_of_users = {}
    for message in chat_history:
        user_id = message["sent_by"]
        if user_id not in dict_of_users:
            dict_of_users[user_id] = 1
        else:
            dict_of_users[user_id] += 1
    max_value = max(dict_of_users, key=dict_of_users.get)
    return max_value


def get_most_replied_user(chat_history):
    dict_of_replies = {}
    for message in chat_history:
        reply_message_id = message["reply_for"]
        if reply_message_id is not None:
            if reply_message_id not in dict_of_replies:
                dict_of_replies[reply_message_id] = 1
            else:
                dict_of_replies[reply_message_id] += 1
    max_replies_id = max(dict_of_replies, key=dict_of_replies.get)
    for message in chat_history:
        if max_replies_id == message["id"]:
            return message["sent_by"]
            break


def get_user_with_unique_viewers(chat_history):
    dict_of_views = {}
    for message in chat_history:
        seen_by_user = message["seen_by"]
        message_id = message["id"]
        if message_id not in dict_of_views:
            dict_of_views[message_id] = []
        for user in seen_by_user:
            if user not in dict_of_views[message_id]:
                dict_of_views[message_id].append(user)
    max_viewed_message = max(dict_of_views, key=lambda x: len(dict_of_views[x]))
    number_of_unique_viewers = len(dict_of_views[max_viewed_message])
    list_of_unique_users = []
    for message in chat_history:
        if len(dict_of_views[message["id"]]) == len(dict_of_views[max_viewed_message]):
            list_of_unique_users.append(message["sent_by"])
    user_list_str = ", ".join(map(str, list_of_unique_users))
    result = f"Aйди пользователей {user_list_str} сообщения которых видело больше всего уникальных пользователей: {number_of_unique_viewers}"
    return result


def get_most_common_time_message(chat_history):
    dict_of_time = {"утром": 0, "днем": 0, "вечером": 0}
    for message in chat_history:
        message_time = message["sent_at"]
        if 0 <= message_time.hour < 12:
            dict_of_time["утром"] += 1
        elif 12 <= message_time.hour < 18:
            dict_of_time["днем"] += 1
        else:
            dict_of_time["вечером"] += 1
    max_number_time_messages = max(dict_of_time, key=dict_of_time.get)
    result = f"Максимальное количество сообщений в чате приходит {max_number_time_messages}: {dict_of_time[max_number_time_messages]}"
    return result


def get_id_with_longest_thread(chat_history):
    dict_of_threads = {}
    for message in chat_history:
        id_for_reply = message["reply_for"]
        if id_for_reply is not None:
            if id_for_reply not in dict_of_threads:
                dict_of_threads[id_for_reply] = 1
            else:
                dict_of_threads[id_for_reply] += 1

    max_thread_id = max(dict_of_threads, key=dict_of_threads.get)
    result = f"Самая длинная цепочка ответов у сообщения с id {max_thread_id}: {dict_of_threads[max_thread_id]} раз было отвечено на данное сообщение"
    return result


chat_history = generate_chat_history()

print(f" \n 1. Вывести айди пользователя, который написал больше всех сообщений.\n ")
fun1 = user_with_most_messages(chat_history)
print(fun1)
print(
    f"\n 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.\n"
)
fun2 = get_most_replied_user(chat_history)
print(fun2)
print(
    f"\n 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.\n"
)
fun3 = get_user_with_unique_viewers(chat_history)
print(fun3)
print(
    f"\n 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).\n"
)
fun4 = get_most_common_time_message(chat_history)
print(fun4)
print(
    f"\n 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).\n"
)
fun5 = get_id_with_longest_thread(chat_history)
print(fun5)
