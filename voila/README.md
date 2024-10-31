## Steps
- python3 -m venv venv
- source venv/bin/activate
- pip install pandas numpy matplotlib scikit-learn voila ipywidgets
- voila app.ipynb --port=8866 --no-browser --enable_nbextensions=True
https://github.com/voila-dashboards/voila/blob/main/notebooks/basics.ipynb

Working basics.ipynb

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voilà App</title>
    <script>
        async function callApi() {
            const response = await fetch('https://your-api-id.execute-api.region.amazonaws.com/invoke');
            const data = await response.json();
            console.log(data);
        }
    </script>
</head>
<body>
    <h1>Call Voilà App</h1>
    <button onclick="callApi()">Invoke Voilà</button>
</body>
</html>
```
