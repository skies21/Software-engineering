# TrainingBot
Это телеграмм бот для помощи отслеживания съеденных калорий. В котором реализован сбор основной информации о пользователе, анализ его текущего рациона, составление программы похудения и разного рода напоминания.  
На данный момент осталось реализовать построение программы для вариантов удержания и набора веса.  
`https://t.me/f1ttnesBot`

## Installation

Clone the repository and go to it on the command line:

```
git clone https://github.com/skies21/Software-engineering.git
```

```
cd TrainingBot/TrainingBot
```

`Create a file .env in the directory at the docker-compose level.yaml in the likeness of example.env`  

Launch a project:

```
docker build -t <nickname>/training_bot:latest .  
docker push <nickname>/training_bot:latest  

docker compose up -d
```
