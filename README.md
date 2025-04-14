# 📜 DiscordDailyQuotes

A lightweight, containerized Python bot that sends a daily inspirational quote to a Discord channel using a webhook. Runs automatically every morning on a Kubernetes CronJob hosted on a Raspberry Pi cluster.

---

## 💡 Features

- 🌅 Sends a fresh quote every morning
- 🔌 Uses [ZenQuotes API](https://zenquotes.io/) for random inspirational quotes
- 💬 Posts to a specified Discord channel via webhook
- 🐳 Runs in a self-contained Docker container
- ⏰ Scheduled via Kubernetes CronJob (e.g., daily at 7:00 AM)

---

## 🚀 How It Works

1. Python script (`main.py`) fetches a quote from the ZenQuotes API
2. The message is formatted and sent to Discord via a webhook
3. A Kubernetes CronJob runs the container daily on a Raspberry Pi worker node

---

## 📦 Technologies Used

- Python 3.11
- `requests` + `python-dotenv`
- Docker
- Kubernetes (k3s)
- Raspberry Pi

---

## 🔧 Setup & Deployment

### 1. Clone the Repository

```bash 
git clone git@github.com:DaltonSchwanke/DiscordDailyQuotes.git
cd DiscordDailyQuotes
```

### 2. Create .env and Add Discord Webhook
```bash
DISCORD_WEBHOOK=https://discord.com/api/webhooks/your/actual/webhook
```

### 3. Build and Push the Docker Image
```bash
docker build -t <USERNAME>/discord-daily-quotes:latest .
docker push <USERNAME>/discord-daily-quotes:latest
```

### 4. Create, Deploy and Test with Kubernetes
```bash
nano quote-cronjob.yaml
kubectl apply -f quote-cronjob.yaml
kubectl create job --from=cronjob/discord-daily-quote manual-test
kubectl logs job/manual-test
```
