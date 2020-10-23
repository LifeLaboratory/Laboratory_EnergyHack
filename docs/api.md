# API:
### Работа с пользователем
```python
-> GET /api/user # получение списка пользователей
response:
{
  'users': [
    {
      'id_user': int,
      'login': str
    }
  ]
}

-> GET /api/user/profile  # получение своего профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'count_game': int,  # Количество игр
  'max_point': int,  # Максимальное количество очков
  'pic': str,
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'health': float,   # Здоровье
      'food': float,     # Питание
      'leisure': float,  # Досуг
      'communication': float,   # Общение
      'point': int # Количество очков, заработанных за игру.
    }
  ]
}

-> GET /api/user/<int:id_user> # получение профиля пользователя
response:
{
  'id_user': int,
  'login': str,
  'rating': int,  # какое место пользователь занимает в общем рейтинге
  'count_game': int,  # количество игр
  'max_point': int,  # Максимальное количество очков
  'pic': str,
  'game_history': [
    {
      'id_game': int,
      'time': str,
      'round': int, # Номер раунда игры
      'health': float,   # Здоровье
      'food': float,     # Питание
      'leisure': float,  # Досуг
      'communication': float,   # Общение
      'point': int # Количество очков, заработанных за игру.
    }
  ]

}

-> POST /api/user/login # авторизация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}

-> POST /api/user/register #  регистрация пользователя
{
  'login': str,
  'password': str
}
response:
{
  'session': str # сессия, с которой пользователь подключен
}
```
