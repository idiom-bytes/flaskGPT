# Deploy on Vercel
Use this flow to yolo deploy to Vercel.

## Deploy directly from github
1. Clone/Fork the repostory and deploy automatically on Vercel.
2. Go to your Vercel application and configure the Environment Variables by setting
```
OPEN_API_KEY=your-api-key
```
3. Curl your endpoint and test your server!
```
curl -X POST https://flaskgpt-your-account-vercel.app/api/prompt -H "Content-Type: application/json" -d "{\"prompt\": \"What is the funniest joke you've ever heard?\"}"
```
4. Have fun!

# Deploy locally
Use this flow to run the server locally and test it.

## Terminal #1 - Setup your server
1. Clone/Fork the repository and onto your local filesystem.
2. Configure your .env by setting
```
OPEN_API_KEY=your-api-key
```
3. Setup your venv and activate it
```
python3 -m venv venv
source venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Start your server
```
python3 flaskGPT.py
```

## Terminal #2 - Test your server
6. Start a new terminal
7. In your 2nd terminal, curl your server
```
curl -X POST https://flaskgpt-your-account-vercel.app/api/prompt -H "Content-Type: application/json" -d "{\"prompt\": \"What is the funniest joke you've ever heard?\"}"
```
8. Have fun!
